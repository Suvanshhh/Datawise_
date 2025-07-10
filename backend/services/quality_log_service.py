import os
from pymongo import MongoClient
from datetime import datetime
from bson import ObjectId
from urllib.parse import urlparse

# Get MongoDB URI from environment
mongo_uri = os.environ.get("MONGO_URI")
client = MongoClient(mongo_uri)

# Function to extract DB name from URI or fallback to env/default
def get_db_name(uri):
    parsed = urlparse(uri)
    if parsed.path and parsed.path != '/':
        return parsed.path.lstrip('/')
    return os.environ.get("MONGO_DB_NAME", "datawise")

db_name = get_db_name(mongo_uri)
db = client[db_name]
quality_logs = db.quality_logs

def add_quality_log(dataset_id, data):
    data['dataset_id'] = ObjectId(dataset_id)
    data['timestamp'] = datetime.utcnow()
    result = quality_logs.insert_one(data)
    return str(result.inserted_id)

def get_quality_logs(dataset_id):
    return list(quality_logs.find({'dataset_id': ObjectId(dataset_id)}))
