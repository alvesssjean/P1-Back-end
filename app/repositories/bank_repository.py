from database import transations_collection
from bson import ObjectId

def create_transation(transation_dict):
    return transations_collection.insert_one(transation_dict)

def get_all_transations():
    return list(transations_collection.find())

def get_transation_by_id(transation_id):
    return transations_collection.find_one({"_id": ObjectId(transation_id)})

def update_transation(transation_id, transation_dict):
    return transations_collection.update_one(
        {"_id": ObjectId(transation_id)},
        {"$set": transation_dict}
    )

def delete_transation(transation_id):
    return transations_collection.delete_one(
        {"_id": ObjectId(transation_id)}
    )