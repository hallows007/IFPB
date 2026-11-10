# Run a limited-attempt number guessing game with hints and input validation.

import random

def validar_numero(valor: int) -> bool:
    if valor >= menor and valor <= maior:
        return True
    else:
        return False


def verificar_acerto(valor: int) -> bool:
    if valor == sorteio:
        return True
    else:
        return False


# Main

menor, maior = random.randint(0, 10), random.randint(90, 100)

sorteio = random.randint(menor, maior)

tentativas = 5

num = int(input(f'Número ({menor}-{maior}): '))

while verificar_acerto(num) != True and validar_numero(num) == True and tentativas > 1:

    tentativas -= 1

    if num > sorteio:
        maior = num - 1
        print('Errou: Seu chute foi maior.')
    else:
        menor = num + 1
        print('Errou: Seu chute foi menor.')

    print(f'Tentativas restantes: {tentativas}')
    num = int(input(f'Número ({menor}-{maior}): '))


if verificar_acerto(num) == True:
    print('Acertou:', num)

elif tentativas == 1:
    print('Suas tentativas acabaram!')
    print('O número sorteado era:', sorteio)

else:
    print('Chute inválido!')