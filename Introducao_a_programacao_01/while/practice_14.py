# Adjust a running total through an increase, decrease, or exit menu.

num = 0

while True:
    print('A - Aumentar')
    print('D - Diminuir')
    print('S - Sair')

    codigo = input('Informe o código: ')
    if codigo =='S':
        break
    unidades = int(input('Digite a quantidade de unidades: '))

    if codigo =='A':
        num += unidades
    elif codigo =='D':
        num -= unidades
    elif codigo =='S':
        break
    else:
        print('Codigo invalido')

print(f'Valor final: {num}')