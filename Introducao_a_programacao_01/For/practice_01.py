# This program reads five integers entered by the user.
# At the end, it displays the last number entered,
# the largest number, and the total count of numbers.

quantidade = 0

numero = int(input('Numero: '))
maior = numero
for i in range(5):
    numero = int(input('Numero: '))
    if numero > maior:
        maior = numero
    quantidade += 1
print(numero, maior, quantidade)