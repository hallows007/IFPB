# Play a round of rock-paper-scissors against a random computer choice.

import random


opcoes = ["pedra","tesoura","papel"]

pergunta = input('Digite se você vai jogar pedra, papel ou tesoura: ')
maquina = random.choice(opcoes)
resultado_maquina = print(f'A maquina escolheu: {maquina}')

if pergunta == maquina:
    print(f'Você escolheu {pergunta} e a maquina {maquina}, ouve um empate')
elif pergunta == "pedra" and maquina == "tesoura":
    print(f'Você escolheu {pergunta} e a maquina {maquina}, Você ganhou!')
elif pergunta == "pedra" and maquina == "papel":
    print(f'Você escolheu {pergunta} e a maquina {maquina}, Você perdeu!')
elif pergunta == "papel" and maquina == "tesoura":
    print(f'Você escolheu {pergunta} e a maquina {maquina}, Você perdeu!')
elif pergunta == "pedra" and maquina == "pedra":
    print(f'Você escolheu {pergunta} e a maquina {maquina}, Você ganhou!')
elif pergunta == "tesoura" and maquina == "pedra":
    print(f'Você escolheu {pergunta} e a maquina {maquina}, Você perdeu!')
elif pergunta == "tesoura" and maquina == "papel":
    print(f'Você escolheu {pergunta} e a maquina {maquina}, Você ganhou!')

