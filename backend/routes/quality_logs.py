from flask import Blueprint, request, jsonify
from models.quality_log_model import QualityLogSchema
from services.quality_log_service import add_quality_log, get_quality_logs
from utils.validation import validate_schema
from flasgger.utils import swag_from

quality_logs_bp = Blueprint('quality_logs', __name__)

@quality_logs_bp.route('/datasets/<dataset_id>/quality-1', methods=['POST'])
@swag_from({...})
def add_log(dataset_id):
    data = request.json
    schema = QualityLogSchema()
    valid_data, errors = validate_schema(schema, data)
    if errors:
        return jsonify({'error': errors}), 400
    log_id = add_quality_log(dataset_id, valid_data)
    return jsonify({'id': log_id}), 201

@quality_logs_bp.route('/datasets/<dataset_id>/quality-1', methods=['GET'])
@swag_from({...})
def list_logs(dataset_id):
    logs = get_quality_logs(dataset_id)
    for l in logs:
        l['_id'] = str(l['_id'])
        l['dataset_id'] = str(l['dataset_id'])
    return jsonify(logs), 200
