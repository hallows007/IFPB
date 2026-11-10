# Check an entered password against length and character composition rules.

''' 
Escreva um programa, em Python, para solicitar ao usuário a criação de uma senha e
verifica se ela atende a um conjunto de critérios de segurança pré-definidos, a seguir:
• Ter no mínimo 8 caracteres;
• Conter pelo menos uma letra maiúscula;
• Conter pelo menos duas letra minúscula;
• Conter pelo menos um número;
• Conter pelo menos dois caractere especial.'''

def verificador_quantidade(senha):

    if len(senha) >= 8:
        return True
    else:
        return False

def verificador_maiusculo(senha):
    for i in senha:
        if ord(i) >= ord('A') and ord(i) <= ord('Z'):
            letra_maiuscula = True
            break
    return letra_maiuscula

def verificador_minusculo(senha):
    qtd_minuscula = 0
    for i in senha:
        if ord(i) >= ord('a') and ord(i) <= ord('z'):
            qtd_minuscula += 1
    if qtd_minuscula >= 2:
        return True
    else:
        return False

def verificador_numero(senha):
    for i in senha:
        if ord(i) >= ord('0') and ord(i) <= ord('9'):
            return True
            break

def verificador_caractere_especial(senha):
    qtd = 0
    for i in senha:
        if ord(i) <= 47 or 64>= ord(i) >= 58 or 96 >= ord(i) >= 91 or ord(i) >= 123:
            qtd += 1
    if qtd >= 2:
        return True


senha = input("Digite sua nova senha: ")



if (verificador_quantidade(senha) == True and verificador_maiusculo(senha) == True and verificador_minusculo(senha) == True and verificador_numero(senha) == True and verificador_caractere_especial(senha) == True):
    print('Senha cadastrada com sucesso')
else:
    print('Erro!')