class Diretorio:
    def __init__(self, campo, tipo="discreto"):
        self.campo = campo
        self.tipo = tipo
        self.indice = {}

    def adicionar(self, registro):
        chave = registro[self.campo]
        if chave not in self.indice:
            self.indice[chave] = set()
        self.indice[chave].add(registro["id"])

    def buscar(self, valor):
        chave = valor
        return self.indice.get(chave, set())
