import json
class Cliente:
    def __init__(self, id, nome, email, fone):
        self.id = id   #atributo da instancia
        self.nome = nome
        self.fone = fone
        self.email = email
    def __str__(self):
        return f"{self.id} - {self.nome} - {self.email} - {self.fone}"


class Clientes: #para usar o dao
    objetos = [] #atributo de classe / estatico

    @classmethod
    def inserir(cls, obj):  #obj = cliente
        cls.objetos.append(obj)

class UI:
    @staticmethod
    def menu():
        print("Cadastro de clientes")
        return int(input("1 - Inserir; 2 - Listas; 3 - Atualizar; 4 -  Excluir  ")) 
    @staticmethod
    def main():
        op = 0
        clientes = []
        while op != 9:
            op = UI.menu()
            if op == 1: UI.cliente_inserir()
            if op == 2: UI.cliente_listar()
    @staticmethod
    def cliente_inserir():
        id = int(input("Informe o ID do Cliente: "))
        nome = (input("Informe o nome do Cliente: "))
        email = (input("Informe o email do Cliente: "))
        fone = int(input("Informe o telefone do Cliente: "))
        c = Cliente(id, nome, email, fone)
        Clientes.inserir(c)
    @staticmethod
    def cliente_listar():
       for c in Clientes.:print(c)  #arrumar depois
UI.main()