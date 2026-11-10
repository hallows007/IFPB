# Find the length of the longest strictly increasing consecutive run in a list.

lista = [1, 2, 3, 5, 7, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5]

sequencia = 1
maior_sequencia = 1

for i in range(1, len(lista)):
    if lista[i] > lista[i - 1]:
        sequencia += 1
    else:
        if sequencia > maior_sequencia:
            maior_sequencia = sequencia
        sequencia = 1

if sequencia > maior_sequencia:
    maior_sequencia = sequencia

print(maior_sequencia)