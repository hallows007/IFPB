# This code compares the age, height, salary, and weight of two individuals
# and displays which one has the higher value for each attribute.

def comparador(valor1, valor2):
    if valor1 > valor2:
        return valor1
    else:
        return valor2

idade1 = int(input('Idade:'))
altura1 = float(input('Altura: '))
peso1 = float(input('Peso: '))
salario1 = float(input('Salário: '))

idade2 = int(input('Idade:'))
altura2 = float(input('Altura: '))
peso2 = float(input('Peso: '))
salario2 = float(input('Salário: '))

maior_idade = comparador(idade1, idade2)
maior_altura = comparador(altura1, altura2)
maior_peso = comparador(peso1, peso2)
maior_salario = comparador(salario1, salario2)

print(f'a maior idade é {maior_idade}')
print(f'A maior altura é {maior_altura}')
print(f'O maior peso é {maior_peso}')
print(f'O maior salario é {maior_salario}')