# Collect votes for three companies and display each company's vote count.

empresas = []
votos = []
for i in range(3):
    empresa = input(f'Digite o nome da {i+1}º empresa: ')
    empresas.append(empresa)

for r in range(3):
    print(f'{r+ 1} - {empresas[r]}')

for p in range(10):
    voto = int(input('Digite o numero que representa a empresa que você deseja votar: '))
    votos.append(voto)

for l in range(3):
    quantidade = votos.count(l + 1)
    print(f'{empresas[l]} recebeu {quantidade} voto(s).')