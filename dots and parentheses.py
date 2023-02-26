import sys

def prime_factors(num):
    factors = []
    max_factor = 1
    i = 2
    while i * i <= num:
        if num % i:
            i += 1
        else:
            factors.append(i)
            num //= i
            max_factor = i
    if num > 1:
        factors.append(num)
        max_factor = max(max_factor,num)
    return factors, max_factor

def funk(max_num):
    if max_num == 0:
        return '.'
    if max_num == 1:
        return '()'
    factors, max_factor = prime_factors(max_num)
    prime_list = []
    prime_flags = [True] * (max_factor+1)
    for i in range(2, int(max_factor ** 0.5) + 1):
        if prime_flags[i]:
            prime_list.append(i)
            for j in range(i*i, max_factor+1, i):
                prime_flags[j] = False
    ekString =''
    for i in prime_list:
        if(factors.count(i)>0):
            ekString += funk(factors.count(i))
        else:
            ekString += '.'

    return "(" + ekString + ")"

numbers = []
for line in sys.stdin:
    x = int(line)
    numbers.append(x)

for i in numbers:
    print(funk(i))
