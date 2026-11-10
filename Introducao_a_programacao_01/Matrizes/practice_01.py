def criar_matriz(linhas: int, colunas: int) -> list:
    matriz = []

    for i in range(linhas):
        matriz.append([0] * colunas)

    return matriz


def preencher_matriz(matriz: list):
    import random

    linhas = len(matriz)
    colunas = len(matriz[0])

    for i in range(linhas):
        for j in range(colunas):
            matriz[i][j] = random.randint(1, 10)


## Main

# Criar Matriz
numeros = criar_matriz(4, 4)

# Preencher com valores aleatórios entre 1 e 10
preencher_matriz(numeros)


# Exibir: Padrão de representação de Python
print("Padrão Python")
print(numeros)
print()

# Exibir: Linha por Linha
print("Linha por Linha")
for i in range(len(numeros)):
    print(f'Linha {i} - {numeros[i]}')
print()

# Exibir: Cada elemento separadamente (um por linha)
print("Um por linha")
for i in range(len(numeros)):
    for j in range(len(numeros[i])):
        print(f'Linha {i} Coluna {j} - {numeros[i][j]}')
print()

# Exibir: Apenas valores da diagonal principal (um por linha)
print("Apenas diagonal principal (um por linha)")
for i in range(len(numeros)):
    print(f'Linha {i} Coluna {i} - {numeros[i][i]}')