# Generate random numbers and print their divisors until an endpoint is drawn.

import random
while True:
    num = random.randint(10,50)
    if num ==10 or num == 50:
        break
    print(num)

    for i in range(1, num+1):
        divisao = num / i
        if num %i ==0:
            print(divisao)