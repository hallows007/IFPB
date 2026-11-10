# Read pairs of numbers until they match or both are nonpositive, then display the final pair.



num1 = int(input('Número: '))
num2 = int(input('Número: '))

while True:
    print('Eita')

    if num1 == num2:
        break

    num1 = int(input('Número: '))
    num2 = int(input('Número: '))

    if num1 <= 0 and num2 <=0:
        break



print(num1, num2)