from diretorio import Diretorio
from cadastro import Cadastro

cadastro = Cadastro()

dir_cargo = Diretorio("profissao", tipo= "discreto")
dir_salario = Diretorio("salario", tipo= "continuo")
dir_cidade = Diretorio("cidade", tipo= "discreto")

def carregar_dados():

    dic_total = [
        {"id": "1", "nome" : "safado", "cidade": "Lages", "cargo": "Médico", "salario": 5000},
        {"id": "2", "nome": "Bruno", "cidade": "Criciúma", "cargo": "Analista", "salario": 2200},
        {"id": "3", "nome": "Carla", "cidade": "Florianópolis", "cargo": "Engenheiro", "salario": 4500}
    ]

    for i in dic_total:
        cadastro.inserir(i)
        dir_cidade.adicionar(i)
        dir_salario.adicionar(i)
        dir_cargo.adicionar(i)

def incluirFuncionario():
    id = input("ID: ")
    nome = input("Nome: ")
    cidade = input("Cidade: ")
    cargo = ("Cargo: ")
    salario = ("Salário: ")

    funcionario = {
        "id": id,
        "nome": nome,
        "cidade": cidade,
        "cargo": cargo,
        "salario": salario
    }

    cadastro.inserir(funcionario)
    dir_cidade.adicionar(funcionario)
    dir_cargo.adicionar(funcionario)
    dir_salario.adicionar(funcionario)

def buscar_por_ID():
    id = input("Digite a ID: ")
    funcionario = cadastro.buscar(id)
    print(funcionario if funcionario else "Funcionario não encontrado.")

def remover_funcionario():
    id = input("Digite o id para remover: ")
    funcionario = cadastro.remover(id)
    if funcionario:
        dir_cidade.remover(funcionario)
        dir_cargo.remover(funcionario)
        dir_salario.remover(funcionario)
        print("Removido com sucesso.")
    else:
        print("Funcionário não encontrado.")

def consulta_simples():
    campo = input("Campo para busca (cidade, cargo, salario): ")
    valor = input("Valor do campo: ")
    if campo == "salario":
        valor = float(valor)

    if campo == "cidade":
        ids = dir_cidade.buscar(valor)
    elif campo == "cargo":
        ids = dir_cargo.buscar(valor)
    elif campo == "salario":
        ids = dir_salario.buscar(valor)
    else:
        print("Campo inválido.")
        return

    for id in ids:
        print(cadastro.buscar(id))

