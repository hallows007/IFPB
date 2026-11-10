# This code reads forty students' grades and displays the class average,
# the number of students who passed, failed, or need to take a final exam.

soma = 0
aprovados = 0
final = 0
reprovados = 0
for i in range(40):
    nota = int(input('Digite a nota: '))
    soma += nota
    if nota >=70:
        aprovados += 1
    elif nota >=40:
        final +=1
    else:
        reprovados += 1

media = soma / (i + 1)
print(f'A media da turma é {media}')
print(f'Quantidade de alunos aprovados {aprovados}')
print(f'Quantidade de alunos que estão na final {final}')
print(f'Quantidade de alunos reprovados {reprovados}')