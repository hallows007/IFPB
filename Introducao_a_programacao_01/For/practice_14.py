# Read three names and ages and display people older than the group average.

nomes = []
idades = []
soma_idades = 0

for i in range(3):
    nome = input(f'Digite o {i+1}º nome: ')
    idade = int(input(f'Digite a idade de {nome}: '))
    nomes.append(nome)
    idades.append(idade)
    soma_idades += idade

media = soma_idades/(i+1)

for r in range(len(idades)):
    if idades[r] > media:
        print(f'{media} é a media do grupo')
        print(f'{nomes[r]}, idade: {idades[r]}')