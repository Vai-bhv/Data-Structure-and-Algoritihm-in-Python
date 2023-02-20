import math
import sys

def primenumber(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def prime_numbers(n):
    
    # isPrime = n * [True]
    # isPrime[0] = isPrime[1] = False   # 0 and 1 are not prime

    # i = 2
    # while i * i <= n:
    #     if isPrime[i]:
    #         for j in range(2 * i, n, i):
    #             isPrime[j] = False
    #     i += 1
    prime_set = set()
    for i in range(2, n+1):
        if primenumber(i):
            prime_set.add(i)
    return prime_set 

def prime_factors(num):
    factors = []
    while num % 2 == 0:
        factors.append(2)
        num = num // 2

    for i in range(3, int(math.sqrt(num)) + 1, 2):
        while num % i == 0:
            factors.append(i)
            num = num // i
    
    if num > 2:
        factors.append(num)
    
    return factors

def output(num):
    factors = prime_factors(num)
    # print(factors)
    max_factor = max(factors)
    prime_set = prime_numbers(max_factor)
    # print(prime_set)
    output_Number = ""
    for factor in prime_set:
        if factor in factors:
            for i in range(factors.count(factor)):
                output_Number += "("
            for i in range(factors.count(factor)):
                output_Number += ")"
        else:
            output_Number += "."

    return output_Number

numbers = []
for line in sys.stdin:
    x = int(line)
    numbers.append(x)

for num in numbers:
    if num == 0:
        print('.')
    elif num == 1:
        print('()') 
    else:
        print('(' + output(num) + ')')


# ek to 11 = 11
# 11 tak ke saare primne prime_factors 11 = 2,3,5,7,11