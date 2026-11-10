## funcões

# Essa função calcula a media aritimetica 
def media_aritimetica(valor1, valor2, valor3):
    media = (valor1 + valor2 + valor3) / 3
    return media

#Essa função calcula a média ponderada
def media_ponderada(valor1, valor2, valor3):
    media = ((valor1 * 5) + (valor2 * 3) + (valor3 * 2)) / 10
    return media

#Essa função verifica qual tipo de média é maior, se é ponderada ou aritimetica
def calcular_media(valor1, valor2, valor3):
    ma = media_aritimetica(valor1, valor2, valor3)
    mp = media_ponderada(valor1, valor2, valor3)

    if ma > mp:
        return ma
    else:
        return mp

#Essa função verifica se a maior media é maior ou igual a 70, para dizer se o aluno foi aprovaado ou nao
def verificar_aprovado(valor1, valor2, valor3) -> bool:
    media = calcular_media(valor1, valor2, valor3)
    if (media >=70):
        return True
    else:
        return False


#programa principal

nota1 = int(input('Digite a primeira nota: '))
nota2 = int(input('Digite a segunda nota: '))
nota3 = int(input('Digite a terceira nota: '))

ma = media_aritimetica(nota1, nota2, nota3)
mp = media_ponderada(nota1, nota2, nota3)
maior_media = calcular_media(nota1, nota2, nota3)

print(f'A sua média aritimetica é {ma:.2f} e ponderada: {mp:.2f}, a maior entre elas é a {maior_media:.2f}')


aprovacao = verificar_aprovado(nota1, nota2, nota3)

if aprovacao == True:
    print(f'Parabens você foi aprovado!')
else:
    print(f'Infelizmente você foi reprovado')