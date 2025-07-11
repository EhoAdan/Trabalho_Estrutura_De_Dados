class Cadastro:
    def __init__(self):
        self.dados = {}

    def inserir(self, registro):
        self.dados[registro["id"]] = registro

    def buscar(self, id):
        return self.dados.get(id)

    def remover(self, id):
        return self.dados.pop(id, None)