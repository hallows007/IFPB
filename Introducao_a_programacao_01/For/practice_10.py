# This program reads a number entered by the user,
# calculates the sum of all integers from 1 to that number,
# and displays the result.

def somador(num):
    soma = 0
    for n in range(1, num+1):
        soma +=n
    return soma

for i in range(10):
    num = int(input('Digite um numero: '))
    resultato = somador(num)
    print(resultato)