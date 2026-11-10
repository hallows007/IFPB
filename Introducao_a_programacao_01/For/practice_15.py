# Count votes for three companies and display the company with the most votes.

empresas = []
votos = []
votos_empresa = []

for i in range(3):
    empresa = input(f'Digite o nome da {i+1}º empresa: ')
    empresas.append(empresa)

for i in range(5):
    voto = input('Digite o nome que representa a empresa que você deseja votar: ')
    votos.append(voto)

for i in range(3):
    quantidade = 0

    for voto in votos:
        if voto == empresas[i]:
            quantidade += 1

    votos_empresa.append(quantidade)
    #print(f'{empresas[l]} recebeu {quantidade} votos.')

maior_votacao = votos_empresa[0]
indice = 0

for i in range(1, len(votos_empresa)):
    if votos_empresa[i] > maior_votacao:
        maior_votacao = votos_empresa[i]
        indice = i


print(empresas)
print(votos_empresa)
print(f'Com {maior_votacao} votos, a empresa ganhadora é a {empresas[indice]}')
