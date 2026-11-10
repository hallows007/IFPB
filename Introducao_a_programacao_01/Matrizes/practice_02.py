linhas = int(input("Indique a quantidade de linhas: "))
colunas = int(input("Indique a quantidade de colunas: "))

# Declarar a matriz
matriz = []
for i in range(linhas):
    matriz.append([0] * colunas)

# Preencher a matriz
for i in range(linhas):
    for j in range(colunas):
        matriz[i][j] = float(input(f"Elemento [{i}][{j}]: "))

# Soma dos elementos por linha da matriz
for i in range(linhas):
    soma= 0
    for j in range(colunas):
        soma += matriz[i][j]
    print(f'Linha {i} = {soma}')

# Somató dos elementos por coluna da matriz
for j in range(colunas):
    soma = 0
    for i in range(linhas):
        soma += matriz[i][j]
    print(f'Coluna {j} = {soma}')