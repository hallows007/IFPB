# Display printable ASCII characters with their decimal and binary codes.

'''Escreva um programa, em Python, exibir a tabela ASCII contendo os símbolos
numéricos, letras maiúsculas e letras minúsculas. Com o seguinte formato:
Símbolo – código decimal – código binário'''

for i in range(32, 127):
    print(f'{chr(i)} - {i} - {bin(i)}')