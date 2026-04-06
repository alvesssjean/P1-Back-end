from fastapi import FastAPI
from app.routes.bank_routes import router

app = FastAPI()

app.include_router(router)

@app.get("/")
def home():
    return {"P1 Backend": "CRUD de transações bancárias."}
