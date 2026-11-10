# Read a matrix of student grades and call functions to display and analyze it.

import practice_03 as funcoes

qtd_alunos = int(input("Indique a quantidade de alunos: "))
qtd_avaliacoes = int(input("Indique a quantidade de avaliações: "))

matriz = []
for i in range(qtd_alunos):
    matriz.append([0] * qtd_avaliacoes)

for i in range(qtd_alunos):
    for j in range(qtd_avaliacoes):
        matriz[i][j] = int(input(f"{j + 1}º nota do {i + 1}º estudante: "))


funcoes.exibir_matriz(matriz)
print()
funcoes.exibir_notas_aluno(matriz)
print()
funcoes.exibir_notas_avaliacoes(matriz)
print()
funcoes.media_estudante(matriz,qtd_avaliacoes)
print()
funcoes.media_avaliacao(matriz,qtd_avaliacoes)
print()
funcoes.exibit_todas_notas(matriz,qtd_avaliacoes)
funcoes.media_todas_notas(matriz,qtd_avaliacoes)
funcoes.maior_nota(matriz,qtd_avaliacoes)
funcoes.menor_nota(matriz,qtd_avaliacoes)