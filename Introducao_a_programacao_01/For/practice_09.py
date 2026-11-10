# Generate Fibonacci terms using the two preceding values.

n = int(input('Termos: '))
anterior = 0
ultimo = 1
for i in range(n-2):
    proximo = anterior+ultimo
    print(f'{proximo}', end=' ')
    anterior = ultimo
    ultimo = proximo