# Read five grades and report their sum, extrema, and counts above or below five.

notas = []
soma = 0
maior = 0
menor = 0
qtd_maior_cinco = 0
qtd_menor_cinco = 0
for i in range(5):
    nota = int(input('Digite a nota: '))
    notas.append(nota)
    soma += nota
maior = nota
menor = nota

for x in notas:
    if x > maior:
        maior = x
    elif x < menor:
        menor = x
    if x >=5:
        qtd_maior_cinco += 1
    else:
        qtd_menor_cinco += 1


print(notas)
print(soma)
print(maior)
print(menor)
print(qtd_maior_cinco)
print(qtd_menor_cinco)