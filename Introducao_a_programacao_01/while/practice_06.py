# Build and display a list of integers from zero through the entered number.

num = int(input('Digite um numero: '))
contador = 0
lista = []


while contador != num + 1:
    lista.append(contador)
    contador = contador +1

print(lista)