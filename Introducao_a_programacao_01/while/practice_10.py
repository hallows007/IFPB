# Offer a menu to list divisors and test whether a number is prime or perfect.

num = int(input('Digite um número positivo: '))

while True:
    if num <=0:
        break
    print('')
    print('1 - Exibir divisores: ')
    print('2 - Verificar se é um numero primo')
    print('3 - Verificar se é um numero perfeito')
    print('S- Ler o proximo numero: ')

    operacao = input('Digite a operação desejada: ')
    while True:
        if operacao == '1' or operacao == '2' or operacao == '3' or operacao == 'S':
            break
        operacao = input('Digite uma operação valida')
        

    if operacao == '1':
        for i in range(1,num+1):
            divisores = num % i
            if divisores == 0:
                print(i)
    elif operacao == '2':
        quantidade_divisores = 0
        for n in range(1, num+1):
            divisoes = num % n
            if divisoes == 0:
                quantidade_divisores += 1
        if quantidade_divisores ==2:
            print(f'O numero {num} é primo')
        else:
            print(f'O numero {num} não é primo')
    elif operacao == '3':
        soma = 0
        for x in range(1,num):
            divisores = num % x
            if divisores == 0:
                soma += x
        if soma == num:
            print('O numero é perfeito')
        else:
            print('O numero não é perfeito')
    elif operacao == 'S':
        num = int(input('Digite um novo valor positivo: '))
        if num <=0:
            break
            
        