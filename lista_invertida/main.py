from diretorio import Diretorio
from cadastro import Cadastro

cadastro = Cadastro()

dir_profissao = Diretorio("profissao", tipo= "discreto")
dir_salario = Diretorio("salario", tipo= "continuo")
dir_cidade = Diretorio("cidade", tipo= "discreto")

def carregar_dados():

dic_total = [
    {"id": "1", "nome" : "safado", "cidade": "Lages", "profissao": "Médico", "salario": 5000},
    {"id": "2", "nome": "Bruno", "cidade": "Criciúma", "profissao": "Analista", "salario": 2200},
    {"id": "3", "nome": "Carla", "cidade": "Florianópolis", "profissao": "Engenheiro", "salario": 4500}
]

dic_profissão = Diretorio("profissao", tipo= "discreto")
dic_salario = Diretorio("salario", tipo= "continuo")
dic_cidade = Diretorio("cidade", tipo= "discreto")




print("Bem-Vindo! O que gostaria de fazer?")