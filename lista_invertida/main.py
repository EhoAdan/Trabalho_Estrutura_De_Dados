from diretorio import Diretorio
from cadastro import Cadastro

cadastro = Cadastro() #Nosso cadastro/dicionário principal

dir_cargo = Diretorio("profissao", tipo= "discreto") #Estes são 3 dicionários diferentes, vindos da mesma classe Diretorio
dir_cidade = Diretorio("cidade", tipo= "discreto")  #Aqui especificamos o nosso "filtro" e qual o tipo de dicionário
dir_salario = Diretorio("salario", tipo= "continuo")

def carregar_dados(): #Carga de Dados pedida pelo Prof

    dic_total = [  #Uma lista de dicionários
        {"id": "1", "nome" : "safado", "cidade": "Lages", "cargo": "Médico", "salario": 5000},
        {"id": "2", "nome": "Bruno", "cidade": "Criciúma", "cargo": "Analista", "salario": 2200},
        {"id": "3", "nome": "Carla", "cidade": "Florianópolis", "cargo": "Engenheiro", "salario": 4500}
    ]

    for i in dic_total: #Cada i aqui é um dicionário da lista acima
        cadastro.inserir(i)
        dir_cidade.adicionar(i)
        dir_salario.adicionar(i)
        dir_cargo.adicionar(i)

def incluirFuncionario(): #Pede os dados do novo funcionário ao usuário
    id = input("Digite o ID do Funcionário: ")
    nome = input("Digite o NOME do Funcionário: ")
    cidade = input("Digite o CIDADE do Funcionário: ")
    cargo = input("Digite o CARGO do Funcionário: ")
    salario = int(input("Digite o SALÁRIO do Funcionário: "))

    funcionario = {
        "id": id,
        "nome": nome,
        "cidade": cidade,
        "cargo": cargo,
        "salario": salario
    }

    cadastro.inserir(funcionario) #As exatas mesmas funções acima, mas com os dados passados pelo usuário
    dir_cidade.adicionar(funcionario)
    dir_cargo.adicionar(funcionario)
    dir_salario.adicionar(funcionario)

def buscar_por_ID():
    id = input("Digite a ID: ")
    funcionario = cadastro.buscar(id) #Por estarmos usando ID, busca o funcionário direto no dicionário principal
    print(funcionario if funcionario else "Funcionario não encontrado.")

def remover_funcionario():
    id = input("Digite o id para remover: ")
    funcionario = cadastro.remover(id) #Puxa as funções de remoção das classes cadastro e diretorio, já que precisamos excluir de todas elas
    if funcionario:
        dir_cidade.remover(funcionario)
        dir_cargo.remover(funcionario)
        dir_salario.remover(funcionario)
        print("Removido com sucesso.")
    else:
        print("Funcionário não encontrado.")

def consulta_simples():
    campo = input("Campo para busca (cidade, cargo, salario): ") #Testar isso, acredito que o Prof queira uma busca combinada entre dois valores diferentes (cargo e cidade por exemplo)
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

