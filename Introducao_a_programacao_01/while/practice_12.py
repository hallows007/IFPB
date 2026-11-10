# Repeatedly calculate factorials for positive inputs until a nonpositive number is entered.

while True:
    num = int(input('Digite um numero positivo: '))
    if num <=0:
        break
    fatorial = 1
    for i in range(1, num+1):
        fatorial *= i
    print(fatorial)