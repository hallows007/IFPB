# This code gets the current date from the computer and checks
# whether the expiration date entered by the user has passed or is still valid.

from datetime import datetime

agora = datetime.now()

dia = agora.day
mes = agora.month
ano = agora.year

def validador(ano_v, mes_v, dia_v):
    if ano_v > ano:
        return True
    elif ano_v == ano:
        if mes_v > mes:
            return True
        elif mes_v == mes:
            if dia_v > dia:
                return True
            else:
                return False
        else:
            return False
    else:
        return False

validade_ano = int(input('Digite o ano da validade do produto: '))
validade_mes = int(input('Digite o mes (em numero) da validade do produto: '))
validade_dia = int(input('Digite o dia da validade do produto: '))

validade = validador(validade_ano, validade_mes, validade_dia)

if validade == True:
    print('O produto está no prazo de validade')
else:
    print('O produto esta fora do prazo de validade')