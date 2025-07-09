from flask import Blueprint, request, jsonify
from models.dataset_model import DatasetSchema
from services.dataset_service import (
    create_dataset, get_datasets, get_dataset, update_dataset, soft_delete_dataset
)
from utils.validation import validate_schema
from flasgger.utils import swag_from

datasets_bp = Blueprint('datasets', __name__)

@datasets_bp.route('/datasets', methods=['POST'])
@swag_from({
    'tags': ['Datasets'],
    'description': 'Create a new dataset',
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'name': {'type': 'string'},
                    'owner': {'type': 'string'},
                    'description': {'type': 'string'},
                    'tags': {
                        'type': 'array',
                        'items': {'type': 'string'}
                    }
                },
                'required': ['name', 'owner']
            }
        }
    ],
    'responses': {
        201: {'description': 'Dataset created'},
        400: {'description': 'Validation error'}
    }
})
def create():
    data = request.json
    schema = DatasetSchema()
    try:
        valid_data = schema.load(data)
    except Exception as err:
        return jsonify({'error': str(err)}), 400
    dataset_id = create_dataset(valid_data)
    return jsonify({'id': dataset_id}), 201

@datasets_bp.route('/datasets', methods=['GET'])
@swag_from({
    'tags': ['Datasets'],
    'description': 'List all datasets (with optional filters: owner, tag)',
    'parameters': [
        {'name': 'owner', 'in': 'query', 'type': 'string', 'required': False},
        {'name': 'tag', 'in': 'query', 'type': 'string', 'required': False}
    ],
    'responses': {
        200: {'description': 'List of datasets'}
    }
})
def list_datasets():
    filters = request.args.to_dict()
    datasets = get_datasets(filters)
    for d in datasets:
        d['_id'] = str(d['_id'])
    return jsonify(datasets), 200

@datasets_bp.route('/datasets/<dataset_id>', methods=['GET'])
@swag_from({
    'tags': ['Datasets'],
    'description': 'Get details of a dataset',
    'parameters': [
        {'name': 'dataset_id', 'in': 'path', 'type': 'string', 'required': True}
    ],
    'responses': {
        200: {'description': 'Dataset details'},
        404: {'description': 'Not found'}
    }
})
def get_one(dataset_id):
    dataset = get_dataset(dataset_id)
    if not dataset:
        return jsonify({'error': 'Not found'}), 404
    dataset['_id'] = str(dataset['_id'])
    return jsonify(dataset), 200

@datasets_bp.route('/datasets/<dataset_id>', methods=['PUT'])
@swag_from({
    'tags': ['Datasets'],
    'description': 'Update a dataset',
    'parameters': [
        {'name': 'dataset_id', 'in': 'path', 'type': 'string', 'required': True},
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'name': {'type': 'string'},
                    'owner': {'type': 'string'},
                    'description': {'type': 'string'},
                    'tags': {
                        'type': 'array',
                        'items': {'type': 'string'}
                    }
                }
            }
        }
    ],
    'responses': {
        200: {'description': 'Updated'},
        404: {'description': 'Not found or not updated'}
    }
})
def update(dataset_id):
    data = request.json
    count = update_dataset(dataset_id, data)
    if count == 0:
        return jsonify({'error': 'Not found or not updated'}), 404
    return jsonify({'message': 'Updated'}), 200

@datasets_bp.route('/datasets/<dataset_id>', methods=['DELETE'])
@swag_from({
    'tags': ['Datasets'],
    'description': 'Soft delete a dataset',
    'parameters': [
        {'name': 'dataset_id', 'in': 'path', 'type': 'string', 'required': True}
    ],
    'responses': {
        200: {'description': 'Deleted'},
        404: {'description': 'Not found or already deleted'}
    }
})
def delete(dataset_id):
    count = soft_delete_dataset(dataset_id)
    if count == 0:
        return jsonify({'error': 'Not found or already deleted'}), 404
    return jsonify({'message': 'Deleted'}), 200
