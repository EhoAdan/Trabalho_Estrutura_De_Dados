from diretorio import Diretorio
from cadastro import Cadastro

dic_total = [
    {"id": "1", "nome" : "George", "cidade": "Balneário Camboriú", "cargo": "Gerente", "salario": 5000},
    {"id": "2", "nome": "Bruno", "cidade": "São José", "cargo": "Analista", "salario": 2200},
    {"id": "3", "nome": "Carla", "cidade": "Florianópolis", "cargo": "Engenheiro", "salario": 4500}
]

dic_profissão = Diretorio("cargo", tipo= "discreto")
dic_salario = Diretorio("salario", tipo= "continuo")
dic_cidade = Diretorio("cidade", tipo= "discreto")




print("Bem-Vindo! O que gostaria de fazer?")