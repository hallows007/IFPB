# This program reads multiple pairs of integers entered by the user.
# Both numbers must be positive (greater than zero).
# If either number is zero or negative, the program stops.
# At the end, it displays the total

num1, num2 = 0, 0
qnt = 0

while True:
    num1 = float(input('Digite um numero: '))
    num2 = float(input('Digite outro numero: '))
    if num1 == num2:
        qnt += 1
    if num1 <0 or num2<0:
        break

print(f'os numeros foram iguais {qnt} vezes')