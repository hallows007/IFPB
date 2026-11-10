# Remove repeated spaces from entered text.

''' Escreva um programa, em Python, para ler um texto e remover todos os espaços em
branco que estão em excesso. Ou seja, deixar apenas um único espaço em branco entre
as palavras do texto.'''


texto = input('Digite qualquer texto: ')
lista = []


for i in range(len(texto)):
    if ord(texto[i]) != 32:
        lista.append(texto[i])
    if ord(texto[i]) == 32:
        if texto[i] == texto[i -1]:
            lista.append('')
        else:
            lista.append(' ')

print(''.join(lista))