import os
from pymongo import MongoClient
from datetime import datetime
from bson import ObjectId

client = MongoClient(os.environ.get("MONGO_URI"))
db = client.get_default_database()
quality_logs = db.quality_logs

def add_quality_log(dataset_id, data):
    data['dataset_id'] = ObjectId(dataset_id)
    data['timestamp'] = datetime.utcnow()
    result = quality_logs.insert_one(data)
    return str(result.inserted_id)

def get_quality_logs(dataset_id):
    return list(quality_logs.find({'dataset_id': ObjectId(dataset_id)}))
