# This program reads the number of yellow and red cards given in each match
# of the Brazilian Football Championship (Brasileirão).
# The championship consists of 38 rounds, with 10 matches per round.
# For each round, the program calculates and displays the total number
# of yellow and red cards given across all 10 matches.

for rodada in range(38):
    amarelo_rodada= 0
    vermelho_rodada = 0
    for partidas in range(10):
        amarelo_partida = int(input(f'Digite a quantidade de cartões amarelos na partida de num {partidas + 1}º: '))
        vermelho_partida = int(input(f'Digite a quantidade de cartões vermelhos na partida de num {partidas + 1}º: '))
        amarelo_rodada += amarelo_partida
        vermelho_rodada += vermelho_partida
    print(f"Cartões amarelos na rodada {rodada + 1}º: {amarelo_rodada}")
    print(f'Cartões vermelhos na rodada {rodada + 1}º: {vermelho_rodada}')