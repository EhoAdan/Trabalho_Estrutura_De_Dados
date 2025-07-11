class Cadastro:
    def __init__(self):
        self.dados = {}  #Nosso dicionário principal/maior

    #Pega o id do registro (dicionário menor),
    #passa como chave ao dicionário maior,
    #associando o valor do registro também ao dicionário maior
    #Essa é uma estrutura que vamos seguir várias vezes em todo o código

    def inserir(self, registro): 
        self.dados[registro["id"]] = registro

    def buscar(self, id):
        return self.dados.get(id)

    def remover(self, id):
        return self.dados.pop(id, None)

    def listar_todos(self):
        return list(self.dados.values())