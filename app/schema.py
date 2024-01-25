from pydantic import BaseModel, PositiveInt

class ProdutosSchema(BaseModel):
    id: int
    nome: str
    preco: PositiveInt
