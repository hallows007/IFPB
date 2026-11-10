# Count names entered before the case-insensitive sentinel FIM.

qtd = 0

nome = input('Nome: ')
while nome != 'FIM' and nome != 'fim':
    nome = input('Nome: ')
    qtd +=1

print(qtd)