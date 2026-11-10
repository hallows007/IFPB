# Repeatedly print integers from one to the entered number until zero is entered.

while True:
    num = int(input('Digite um numero: '))
    if num ==0:
        break

    for i in range(1, num+1):
        print(i, end=' ')
    print()