from diretorio import Diretorio
from cadastro import Cadastro

cadastro = Cadastro() #Nosso cadastro/dicionário principal

dir_profissao = Diretorio("profissao", "discreto") #Estes são 3 dicionários diferentes, vindos da mesma classe Diretorio
dir_cidade = Diretorio("cidade", "discreto") #Aqui especificamos o nosso "filtro" e qual o tipo de dicionário
dir_salario = Diretorio("salario", "continuo")

def carregar_dados(): #Carga de Dados pedida pelo Prof

    dic_total = [ #Uma lista de dicionários
        {"id": "1", "nome" : "George", "cidade": "Balneário Camboriú", "cargo": "Gerente", "salario": 5000},
        {"id": "2", "nome": "Bruno", "cidade": "São José", "cargo": "Analista", "salario": 2200},
        {"id": "3", "nome": "Carla", "cidade": "Florianópolis", "cargo": "Engenheiro", "salario": 4500}
    ]

    for i in dic_total: #Cada i aqui é um dicionário da lista acima
        cadastro.inserir(i)
        dir_cidade.adicionar(i)
        dir_salario.adicionar(i)
        dir_profissao.adicionar(i)
