from pydantic import BaseModel

class ProdutosSchema(BaseModel):
    id: int
    nome: str
    preco: float
