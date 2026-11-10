# 3. Implement an International Purchase Converter to calculate the
# cost of a purchase made abroad, converting US Dollars (USD) to
# Brazilian Reais (BRL).

# First, implement the following functions:

# 1. Calculate the total purchase amount in USD.
#    Parameters: Unit price in USD and quantity purchased.
#    Returns: Total purchase amount in USD.

# 2. Convert USD to BRL.
#    Parameter: Purchase amount in USD.
#    Returns: Converted amount in BRL.
#    Exchange rate: 1 USD = 5.00 BRL.

# 3. Calculate the import tax in BRL.
#    Parameter: Purchase amount in BRL.
#    Returns: Import tax in BRL.
#    Tax rates:
#    - 20% for purchases up to 50 USD (Remessa Conforme program).
#    - 60% for purchases above 50 USD.

# 4. Calculate the final purchase cost.
#    Parameter: Purchase amount in BRL.
#    Returns: Final purchase cost in BRL, including import tax.

# Note: ICMS (Brazilian state tax) is excluded to simplify calculations.

# Write a program that reads the unit price of a product in USD
# and the quantity purchased.

# The program must display:
# - Total purchase amount in USD and BRL, excluding import tax.
# - Import tax amount in BRL.
# - Final purchase cost in BRL, including import tax.

def total_dolar(unidade, quantidade):
    total = unidade * quantidade
    return total

def conversao(unidade, quantidade):
    valor_dolar = total_dolar(unidade,quantidade)
    total_real = valor_dolar * 5
    return total_real

def calculo_imposto(unidade, quantidade):
    valor_dolar = total_dolar(unidade, quantidade)
    if valor_dolar <= 50:
        imposto_dolar = valor_dolar * 0.2
    else:
        imposto_dolar = valor_dolar * 0.6
    imposto_real = imposto_dolar * 5
    return imposto_real

def valor_final(quantidade, unidade):
    valor_real = conversao(quantidade, unidade)
    imposto_real = calculo_imposto(quantidade, unidade)
    valor_total = valor_real + imposto_real
    return valor_total
    


uni = int(input("Digite o valor unitario do item: "))
qnt = int(input('Digite a quantidade de itens: '))
compra_dolar = total_dolar(qnt, uni)
compra_real = conversao(qnt, uni)
impostos_real = calculo_imposto(qnt, uni)
valor_total_real = valor_final(qnt, uni)
print(f'O total da compra em dolar é (sem impostos): {compra_dolar}')
print(f'O total da compra em real é (sem impostos): {compra_real}')
print(f'O total em real de impostos é {impostos_real}')
print(f'O total da compra em real com os impostos incluidos é {valor_total_real}')