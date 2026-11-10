# This program reads multiple pairs of integers entered by the user.
# Both numbers must be positive (greater than zero).
# If either number is zero or negative, the program stops.
# At the end, it displays the total

num1 = int(input('Número: '))
num2 = int(input('Número: '))

if num1 != 0 and num2 != 0 and num1 != num2:
    while True:
        print('Eita')
        num1 = int(input('Número: '))
        num2 = int(input('Número: '))

        if num1 == 0 or num2 == 0 or num1 == num2:
            break

print(num1, num2)