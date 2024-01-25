from typing import List, Dict

class Produtos:
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

    def list_products(self):
        return self.produtos
    
    def find_products(self, id):
        for produto in self.produtos:
            if produto["id"] == id:
                return produto
        return {"Status":404, "Mensagem":"Produto não localizado."}
    
    def add_product(self, produto):
        self.produtos.append(produto)
        return produto