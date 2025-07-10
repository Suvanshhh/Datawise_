import os
from pymongo import MongoClient
from datetime import datetime
from bson import ObjectId
from urllib.parse import urlparse

mongo_uri = os.environ.get("MONGO_URI")
client = MongoClient(mongo_uri)

def get_db_name(uri):
    parsed = urlparse(uri)
    if parsed.path and parsed.path != '/':
        return parsed.path.lstrip('/')
    return os.environ.get("MONGO_DB_NAME", "datawise")

db_name = get_db_name(mongo_uri)
db = client[db_name]
datasets = db.datasets

def create_dataset(data):
    data['created_at'] = data['updated_at'] = datetime.utcnow()
    data['is_deleted'] = False
    result = datasets.insert_one(data)
    return str(result.inserted_id)

def get_datasets(filters):
    query = {'is_deleted': False}
    if 'owner' in filters:
        query['owner'] = filters['owner']
    if 'tag' in filters:
        query['tags'] = filters['tag']
    return list(datasets.find(query))

def get_dataset(dataset_id):
    return datasets.find_one({'_id': ObjectId(dataset_id), 'is_deleted': False})

def update_dataset(dataset_id, data):
    data['updated_at'] = datetime.utcnow()
    result = datasets.update_one({'_id': ObjectId(dataset_id)}, {'$set': data})
    return result.modified_count

def soft_delete_dataset(dataset_id):
    result = datasets.update_one({'_id': ObjectId(dataset_id)}, {'$set': {'is_deleted': True}})
    return result.modified_count
