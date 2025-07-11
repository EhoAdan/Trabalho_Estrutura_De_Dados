# Lista
minha_lista = [10, 20, 30, 40, 50]
elemento_removido = minha_lista.pop(2)  # Remove o elemento no índice 2 (valor 30)
print(minha_lista)  # Output: [10, 20, 40, 50]
print(elemento_removido)  # Output: 30

ultimo_elemento = minha_lista.pop() # Remove o último elemento (50)
print(minha_lista) # Output: [10, 20, 40]
print(ultimo_elemento) # Output: 50

# Dicionário
meu_dicionario = {"a": 1, "b": 2, "c": 3}
valor_removido = meu_dicionario.pop("b") # Remove o par "b": 2
print(meu_dicionario) # Output: {'a': 1, 'c': 3}
print(valor_removido) # Output: 2

valor_padrao = meu_dicionario.pop("d", "Chave não encontrada") # "d" não existe, retorna o valor padrão
print(meu_dicionario) # Output: {'a': 1, 'c': 3}
print(valor_padrao) # Output: Chave não encontrada