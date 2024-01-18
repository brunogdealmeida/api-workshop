from fastapi import FastAPI
from .schema import ProdutosSchema
from .data import Produtos

app = FastAPI()
list_of_products = Produtos()

#Recebe requisições Get e retorna uma mensagem
@app.get("/") 
def hello_world():
    return {"Hello": "World"}

#recebe uma requisição e retorna uma lista como resultado
@app.get("/produtos", response_model = list[ProdutosSchema])
def list_products():
    return list_of_products.list_products()

@app.get("/produtos/{id}", response_model = ProdutosSchema)
def find_product(id: int):
    return list_of_products.find_product(id)