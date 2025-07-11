dic_total = {
    1: ["Maria", "Florianópolis", "Analista", 2000],
    2: ["Luíza", "Florianópolis", "Gerente", 3000],
    3: ["José", "Florianópolis", "Médico", 3500],
    4: ["João", "Inbituba", "Analista", 4000],
    5: ["José", "Inbituba", "Gerente", 4500],
    6: ["Ayrton", "Inbituba", "Médico", 5000],
    7: ["Camilo", "Jaraguá do Sul", "Analista", 9000],
    8: ["Maria", "Jaraguá do Sul", "Gerente", 12000],
    9: ["Gustavo", "Jaraguá do Sul", "Médico", 15000]
    }

dic_profissao = {}
dic_salario = {}
dic_cidade = {}

print(dic_total[1])

def inserir(nome, cidade, profissao, salario):
    dic_total.update({nome: [cidade, profissao, salario]})

def busca_cidade(cidade):
    print(dic_profissao[cidade])

def busca_profissão(profissao):
    print(dic_profissao[profissao])

def busca_salario(salario):
    print(dic_profissao[salario])