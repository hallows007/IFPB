# This program takes two prices for the same product: the original price
# and the discounted price. It checks whether the discount is greater than 10%.
# If the discount is less than 10%, it returns False.

#caso a promoção seja fraude a função irá retornar verdadeiro (sim, é fraude)
def verificador_fraude(valor_antigo, valor_atual):
    if valor_atual >= valor_antigo:
        return True
    else:
        return False

quantidade_fraude = 0
quantidade_desconto = 0
quantidade = int(input('Digite a quantidade de produtos: '))

for i in range(quantidade):
    preco_antigo = float(input('Digite o preço antigo do produto: '))
    preco_atual =  float(input('Digite o preço atual: '))
    verificador = verificador_fraude(preco_antigo,preco_atual)
    if verificador == True:
        quantidade_fraude +=1
    if preco_atual < (preco_antigo * 0.9):
        quantidade_desconto += 1

print(f'{quantidade_fraude} quantidade de fraudes!')
print(f'{quantidade_desconto} itens com desconto igual ou inferior a 10%')