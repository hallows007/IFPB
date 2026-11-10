# This program reads the marathon finish times of athletes
# and displays the fastest time and the athlete who achieved it.

def conversor(hora,minuto,segundo):
    hora_seg = hora * 3600
    min_seg = minuto * 60
    return hora_seg + min_seg + segundo


atleta_campeao = input('Nome do atleta: ')
hora = int(input('Digite a quantidade de horas: '))
while hora >= 2:
    print('QUANTIDADE INVALIDA!')
    hora = int(input('Digite a quantidade de horas novamente: '))
minutos = int(input('Digite a quantidade de minutos: '))
while minutos >=60:
    print('QUANTIDADE INVALIDA!')
    hora = int(input('Digite a quantidade de minutos novamente: '))
segundos = int(input('Digite a quantidade de segundos: '))
while segundos >= 60:
    print('QUANTIDADE INVALIDA!')
    hora = int(input('Digite a quantidade de segundos novamente: '))
tempo_campeao = conversor(hora,minutos,segundos)


for i in range(2):
    nome = input('Nome do atleta: ')
    hora = int(input('Digite a quantidade de horas: '))
    while hora >= 2:
        print('QUANTIDADE INVALIDA!')
        hora = int(input('Digite a quantidade de horas novamente: '))
    minutos = int(input('Digite a quantidade de minutos: '))
    while minutos >=60:
        print('QUANTIDADE INVALIDA!')
        hora = int(input('Digite a quantidade de minutos novamente: '))
    segundos = int(input('Digite a quantidade de segundos: '))
    while segundos >= 60:
        print('QUANTIDADE INVALIDA!')
        hora = int(input('Digite a quantidade de segundos novamente: '))
    tempo_prova = conversor(hora,minutos,segundos)
    if tempo_prova < tempo_campeao:
        tempo_campeao = tempo_prova
        atleta_campeao = nome

hora_campea = tempo_campeao // 3600
minutos_campeao = (tempo_campeao % 3600) // 60
segundos_campeao = tempo_campeao % 60

print(atleta_campeao)
print(f'{hora_campea}hrs:{minutos_campeao}min:{segundos_campeao}s')