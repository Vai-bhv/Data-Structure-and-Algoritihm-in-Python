import math
import fileinput


def prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def prime_set(n):
    primes = set()
    for i in range(2, n + 1):
        if prime(i):
            primes.add(i)
    return primes 


def find_prime_factors(num):
    factors = []
    while num % 2 == 0:
        factors.append(2)
        num //= 2

    for i in range(3, int(math.sqrt(num)) + 1, 2):
        while num % i == 0:
            factors.append(i)
            num //= i

    if num > 2:
        factors.append(num)

    return factors


def output(num):
    if num == 0:
        return '.'
    if num == 1:
        return "()"
    factors = find_prime_factors(num)
    max_factor = max(factors)
    primes = prime_set(max_factor)
    outputN = ""
    for prime in primes:
        if prime in factors:
            for i in range(factors.count(prime)):
                outputN += "("
            for i in range(factors.count(prime)):
                outputN += ")"
        else:
            outputN += "."
    return '(' + outputN + ')'


numbers = []

for line in fileinput.input():
    numbers.append(int(line))

for num in numbers:
    print(output(num))