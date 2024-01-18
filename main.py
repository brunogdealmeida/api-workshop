from fastapi import FastAPI
from typing import List, Dict

produtos: List[Dict[str, any]] = [
    {
        "id": 1,
        "nome":"Notebook",
        "preco": 15.00
    },
    {
        "id": 2,
        "nome":"Celular",
        "preco": 10.00
    },
    {
        "id": 3,
        "nome":"Mesa",
        "preco": 1.00
    },
    {
        "id": 4,
        "nome": "Fone",
        "preco": 2.00
    }

]

app = FastAPI()

@app.get("/") #Recebe requisições Get
def hello_world():
    return {"Hello": "World"}

@app.get("/produtos")
def list_products():
    return produtos