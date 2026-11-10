# Compute and print each intermediate factorial value up to the entered number.

num = int(input("Digite qualquer numero: "))
fatorial = 1
for i in range(1, num+1):
    fatorial = fatorial * i
    print(fatorial)