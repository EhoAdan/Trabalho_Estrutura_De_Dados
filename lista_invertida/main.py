from diretorio import Diretorio
from cadastro import Cadastro

cadastro = Cadastro()

dir_profissao = Diretorio("profissao", "discreto")
dir_cidade = Diretorio("cidade", "discreto")
dir_salario = Diretorio("salario", "continuo")

def carregar_dados():

    dic_total = [
        {"id": "1", "nome" : "George", "cidade": "Balneário Camboriú", "cargo": "Gerente", "salario": 5000},
        {"id": "2", "nome": "Bruno", "cidade": "São José", "cargo": "Analista", "salario": 2200},
        {"id": "3", "nome": "Carla", "cidade": "Florianópolis", "cargo": "Engenheiro", "salario": 4500}
    ]

    for i in dic_total:
        cadastro.inserir(i)
        dir_cidade.adicionar(i)
        dir_salario.adicionar(i)
        dir_profissao.adicionar(i)