# Convert entered text to uppercase by changing character codes.

'''Escreva um programa, em Python, para ler um texto e exibir todos os caracteres desse
texto convertidos para maiúsculo.'''

texto = input('Digite o texto: ')
texto_maiusculo = []

for i in texto:
    if ord(i) != 32:
        conversao = ord(i) - 32
        texto_maiusculo.append(chr(conversao))
    elif ord(i) == 32:
        texto_maiusculo.append(i)

print(''.join(texto_maiusculo))