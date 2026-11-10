# Collect names until the user enters the sentinel value and print the list.

nomes = []

while True:
    nome = input('Digite um nome: ')
    if nome == "fim":
        break
    else:
        nomes.append(nome)

print(nomes)