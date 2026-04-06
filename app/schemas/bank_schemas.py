from pydantic import BaseModel

class BankTransations(BaseModel):
    tipo: str
    valor: int
    destinatario: str
    remetente: str