# Reverse a list of names in place by swapping elements from both ends.

nomes = ["ana", "maria","caua","Clara"]

n, m = 0, len(nomes) -1

while n < m:
    nomes[n], nomes[m] = nomes[m], nomes[n]

    n += 1
    m -= 1

print(nomes)