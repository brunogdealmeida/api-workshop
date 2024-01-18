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
    }

]

app = FastAPI()

@app.get("/") #Recebe requisições Get
def hello_world():
    return {"Hello": "everybody"}

@app.get("/produtos")
def list_products():
    return produtos