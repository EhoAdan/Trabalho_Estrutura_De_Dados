class Cadastro:
    def __init__(self):
        self.dados = {} #Nosso dicionário principal/maior

    def inserir(self, registro): #Pega o id do registro (dicionário menor) e passa como chave ao dicionário maior, associando o valor do registro também ao dicionário maior
        self.dados[registro["id"]] = registro
        print(self.dados[registro["id"]])

    def buscar(self, id):
        return self.dados.get(id)

    def remover(self, id):
        return self.dados.pop(id, None)
