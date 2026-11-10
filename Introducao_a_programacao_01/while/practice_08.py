# Repeatedly print and sum the integers between two positive inputs.

while True:
    m = int(input('N: '))
    n = int(input('M: '))

    if m <=0 or n <=0:
        break


    if m > n:
        m,n=n,m

    soma = 0
    for i in range(m,n+1):
        print(i, end=" + ")
        soma +=i

    print(f' Sum = {soma}')
