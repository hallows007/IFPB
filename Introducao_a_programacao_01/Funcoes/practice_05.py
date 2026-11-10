# Compare two numbers and return a value indicating their relative order.

''' This code compares two numbers and shows the larger one '''

def comparador(num1, num2):
    if num1 > num2:
        return -1
    elif num1 < num2:
        return 1
    else:
        return 0

valor1 = float(input('Digite um valor: '))
valor2 = float(input('Digite um valor: '))

resultado = comparador(valor1, valor2)
print(resultado)