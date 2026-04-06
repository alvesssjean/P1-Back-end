from app.schemas.bank_schemas import BankTransations
from fastapi import APIRouter
from database import transations_collection

from bson import ObjectId

router = APIRouter()

#GET ALL
@router.get("/transations")
def list_transations():
    transations = []

    for transation in transations_collection.find():
        transation["_id"] = str(transation["_id"])
        transations.append(transation)

    return transations

#POST - CREATE TRANSATION
@router.post("/transations")
def create_transation(transation: BankTransations):
    transations_dict = transation.model_dump()
    result = transations_collection.insert_one(transations_dict)

    return {
        "message" :"transation created",
        "id": str(result.inserted_id)
    } 

#GET - TRANSATION BY ID

@router.get("/transations/{transation_id}")
def get_transation(transation_id: str):
    from bson import ObjectId

    transation = transations_collection.find_one({"_id": ObjectId(transation_id)})

    if transation:
        transation["_id"] = str(transation["_id"])
        return transation
    return {"error": "transation not found"}


#UPDATE
@router.put("/transations/{transation_id}")
def update_transation(transation: BankTransations, transation_id: str):
    transation_dict = transation.model_dump()
    result = transations_collection.update_one(
        {"_id": ObjectId(transation_id)},
        {"$set": transation_dict}
    )
    if result.matched_count ==0:
        return {"error": "transation not found"}
    else:
        return {"message": "user updated succesfly"}

#DELETE
@router.delete("/transations/{transation_id}")
def delete_transation(transation_id: str):
    result = transations_collection.delete_one(
        {"_id": ObjectId(transation_id)}
    )
    if result.deleted_count == 0:
        return {"error": "transation not found"}
    return {"message":"user deleted"}