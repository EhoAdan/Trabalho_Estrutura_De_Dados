class Diretorio:
    def __init__(self, campo, tipo): #Ao ter o "filtro" recebido como parametro, sabemos o que adicionar, remover e buscar no dicionário menor
        self.campo = campo
        self.tipo = tipo
        self.indice = {} #Nosso dicionário menor (cada um dos objetos instanciados na main, terão um dicionário desses)

    def adicionar(self, registro):
        valor = registro[self.campo]
        chave = self._normalizar(valor)
        if chave not in self.indice:
            self.indice[chave] = set()
        self.indice[chave].add(registro["id"])

    def buscar(self, valor):
        chave = self._normalizar(valor)
        return self.indice.get(chave, set())
    
    def remover(self, registro):
        valor = registro[self.campo]
        chave = self._normalizar(valor)

        if chave in self.indice:
            self.indice[chave].discard(registro["id"])
            if not self.indice[chave]:
                del self.indice[chave]

    def _normalizar(self, valor): #Normaliza os valores contínuos dos salários em faixas de salário
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
