# Classify each of four entered grades as passed, failed, or needing recovery.

def situacao_aluno(media):
    if media >=7:
        return "aprovado"
    elif media <=5:
        return "reprovado"
    else:
        return "recuperação"

notas = []
for i in range(4):
    nota = int(input('Digite a nota: '))
    notas.append(nota)

for x in notas:
    print(situacao_aluno(x))