# Add swimming, cycling, and running times and display the total duration.

hora_natacao = int(input('Digite a quantidade de horas na natação: '))
min_natacao = int(input('Digite a quantidade de minutos na natação: '))
seg_natacao = int(input('Digite a quantidade de segundos na natação: '))
tempo_natacao = (hora_natacao * 3600) + (min_natacao * 60) + seg_natacao

hora_bike = int(input('Digite a quantidade de horas no ciclismo: '))
min_bike = int(input('Digite a quantidade de minutos no ciclismo: '))
seg_bike = int(input('Digite a quantidade de segundos no ciclismo: '))
tempo_bike = (hora_bike * 3600) + (min_bike * 60) + seg_bike

hora_corrida = int(input('Digite a quantidade de horas na corrida: '))
min_corrida = int(input('Digite a quantidade de minutos na corrida: '))
seg_corrida = int(input('Digite a quantidade de segundos na corrida: '))
tempo_corrida = (hora_corrida * 3600) + (min_corrida * 60) + seg_corrida

soma_total = tempo_natacao + tempo_bike + tempo_corrida

hora_total = soma_total // 3600
min_total = (soma_total % 3600) // 60
seg_total = (soma_total % 3600) % 60

print(f'O tempo de prova for de {hora_total} horas {min_total} minutos e {seg_total} segundos')