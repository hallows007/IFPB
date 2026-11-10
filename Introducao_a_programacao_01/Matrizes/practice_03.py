# Provide functions to display and summarize grades stored in a matrix.

def exibir_matriz(matriz):
    for i in range(len(matriz)):
        print(matriz[i])

def exibir_notas_aluno(matriz):
    aluno = int(input('Digite o numero do aluno: '))
    print(matriz[aluno - 1])

def exibir_notas_avaliacoes(matriz):
    avaliacao = int(input('Digite a avaliação que deseja puxar as notas: '))
    for i in range(len(matriz)):
        print(matriz[i][avaliacao - 1])

def media_estudante(matriz,colunas):
    for i in range(len(matriz)):
        soma = 0
        for j in range(colunas):
            soma += matriz[i][j]
        media = soma/colunas
        print('Media de cada aluno')
        print(media)

def media_avaliacao(matriz,colunas):
    for i in range(len(matriz)):
        soma=0
        for j in range(colunas):
            soma += matriz[j][i]
        media = soma/colunas
        print('Media das notas de cada avaliação')
        print(media)

def diferentes_notas(matriz,colunas):
    for i in range(len(matriz)):
        for j in range(colunas):
            return matriz[i][j]

def exibit_todas_notas(matriz,colunas):
    notas = []
    for i in range(len(matriz)):
        for j in range(colunas):
            notas.append(matriz[i][j])

    return notas

def media_todas_notas(matriz,colunas):
    notas = exibit_todas_notas(matriz,colunas)
    soma = 0
    for i in range(len(notas)):
        soma += notas[i]
    media = soma/len(notas)

    return media

def maior_nota(matriz,colunas):
    notas = exibit_todas_notas(matriz,colunas)
    maior = notas[0]
    for i in range(len(notas)):
        if notas[i] > maior:
            maior = notas[i]
    return maior

def menor_nota(matriz,colunas):
    notas = exibit_todas_notas(matriz,colunas)
    menor = notas[0]
    for i in range(len(notas)):
        if notas[i] < menor:
            menor = notas[i]
    return menor

