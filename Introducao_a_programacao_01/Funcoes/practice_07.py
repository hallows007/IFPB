# Calculate a car rental price based on category, duration, insurance, and a discount.

def calcula_aluguel(categoria, dias):
    if dias >30:
        return -1

    if categoria == 'economico':
        valor = dias * 120
    elif categoria == 'intermediario':
        valor = dias * 180
    else:
        valor = dias * 250

    taxa_seguro = valor * 0.08

    if dias >= 7:
        valor = valor * 0.9

    return valor + taxa_seguro

categoria = input('Digite a categoria do carro, as opçoes são "economico" "intermediario" "suv": ')
dias = int(input('Digite a quantidade de dias que você ira passar com o carro: '))

total = calcula_aluguel(categoria,dias)


if total != -1:
    print(f'O valor a pagar é de R${total}')
else:
    print('Não é possivel você alugar o veiculo por esse quantidade de dias')