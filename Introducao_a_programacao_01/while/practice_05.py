# Prompt for a positive number and exit the loop once one is entered.

numero = int(input('Digite um numero positivo (ou 0 para sair): '))

while True:
    print(f'Você digitou: {numero}')
    if numero <0:
        print('Numero negativo não é permitido')
        numero = int(input('Digite um numero positivo (ou 0 para sair): '))
    if numero >0:
        break

print('Encerrando o loop')