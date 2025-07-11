class Cadastro:
    def __init__(self):
        self.dados = {}  #Nosso dicionário principal/maior

    def inserir(self, registro): 
        self.dados[registro["id"]] = registro  #Pega o id do registro (dicionário menor) e passa como chave ao dicionário maior, associando o valor do registro também ao dicionário maior

    def buscar(self, id):
        return self.dados.get(id)

    def remover(self, id):
        return self.dados.pop(id, None)

    def listar_todos(self):
        return list(self.dados.values())