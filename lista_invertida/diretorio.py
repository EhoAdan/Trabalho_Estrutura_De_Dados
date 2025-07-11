class Diretorio:
    def __init__(self, campo, tipo="discreto"):
        self.campo = campo
        self.tipo = tipo
        self.indice = {}

    def adicionar(self, registro):
        valor = registro[self.campo]
        chave = self._normalizar(valor)
        if chave not in self.indice:
            self.indice[chave] = set()
        self.indice[chave].add(registro["id"])

    def buscar(self, valor):
        chave = valor
        return self.indice.get(chave, set())
    
    def remover(self, aluno):
        valor = aluno[self.campo]
        chave = self._normalizar(valor)

        if chave in self.indice:
            self.indice[chave].discard(aluno["matricula"])
            if not self.indice[chave]:
                del self.indice[chave]

    def _normalizar(self, valor):
        if self.tipo == "continuo":
            if valor < 2000:
                return "0-1999"
            elif valor < 3000:
                return "2000-2999"
            elif valor < 4000:
                return "3000-3999"
            else:
                return "4000+"
        return valor
