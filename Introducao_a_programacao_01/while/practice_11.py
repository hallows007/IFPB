# Read three grades and prompt again whenever a grade is outside the valid range.

for i in range(3):
    nota = int(input('Digite uma nota: '))
    while nota >100 or nota<0:
        nota = int(input('Digite uma nota valida: '))