from diretorio import Diretorio
from cadastro import Cadastro

cadastro = Cadastro() #Nosso cadastro/dicionário principal

dir_cargo = Diretorio("cargo", tipo= "discreto") #Estes são 3 dicionários diferentes, vindos da mesma classe Diretorio
dir_cidade = Diretorio("cidade", tipo= "discreto")  #Aqui especificamos o nosso "filtro" e qual o tipo de dicionário
dir_salario = Diretorio("salario", tipo= "continuo")

def carregar_dados(): #Carga de Dados pedida pelo Prof

    dic_total = [  #Uma lista de dicionários
        {"id": "1", "nome": "Ana", "cidade": "Florianópolis", "cargo": "Gerente", "salario": 5200},
        {"id": "2", "nome": "Bruno", "cidade": "São José", "cargo": "Analista", "salario": 2400},
        {"id": "3", "nome": "Carla", "cidade": "Palhoça", "cargo": "Desenvolvedor", "salario": 3300},
        {"id": "4", "nome": "Diego", "cidade": "Biguaçu", "cargo": "Analista", "salario": 2800},
        {"id": "5", "nome": "Eva", "cidade": "São José", "cargo": "Técnico", "salario": 1900},
        {"id": "6", "nome": "Fábio", "cidade": "Palhoça", "cargo": "Desenvolvedor", "salario": 3100},
        {"id": "7", "nome": "Gisela", "cidade": "Florianópolis", "cargo": "Gerente", "salario": 5600},
        {"id": "8", "nome": "Hugo", "cidade": "São José", "cargo": "Analista", "salario": 2500},
        {"id": "9", "nome": "Irene", "cidade": "Biguaçu", "cargo": "Técnico", "salario": 2100},
        {"id": "10", "nome": "João", "cidade": "Florianópolis", "cargo": "Técnico", "salario": 2000},
    ]

    for i in dic_total: #Cada i aqui é um dicionário da lista acima
        cadastro.inserir(i)
        dir_cidade.adicionar(i)
        dir_salario.adicionar(i)
        dir_cargo.adicionar(i)


def incluir_funcionario(): #Pede os dados do novo funcionário ao usuário
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

def consulta_composta():
    campo1 = input("Primeiro campo para busca (cidade, cargo, salario): ")
    valor1 = input("Valor do primeiro campo: ")
    if campo1 == "salario":
        valor1 = float(valor1)

    campo2 = input("Segundo campo para busca (cidade, cargo, salario): ")
    valor2 = input("Valor do segundo campo: ")
    if campo2 == "salario":
        valor2 = float(valor2)

    dir_map = {
        "cidade": dir_cidade,
        "cargo": dir_cargo,
        "salario": dir_salario
    }

    IDs1 = dir_map[campo1].buscar(valor1)
    IDs2 = dir_map[campo2].buscar(valor2)

    interseccao = IDs1 & IDs2
    for id in interseccao:
        print(cadastro.buscar(id))

def exibir_todos():
    for funcionario in cadastro.listar_todos():
        print(funcionario)

def menu():
    while True:
        print("\n1. Carga de dados")
        print("2. Incluir novo funcionário")
        print("3. Buscar por ID")
        print("4. Remover por ID")
        print("5. Consulta simples")
        print("6. Consulta composta")
        print("7. Exibir todos")
        print("0. Sair")

        opc = input("Opção: ")

        if opc == "1":
            carregar_dados()
        elif opc == "2":
            incluir_funcionario()
        elif opc == "3":
            buscar_por_ID()
        elif opc == "4":
            remover_funcionario()
        elif opc == "5":
            consulta_simples()
        elif opc == "6":
            consulta_composta()
        elif opc == "7":
            exibir_todos()
        elif opc == "0":
            break
        else:
            print("Opção inválida.")

menu()