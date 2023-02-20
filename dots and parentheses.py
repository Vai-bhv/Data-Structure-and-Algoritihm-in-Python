import sys

final_result = []

def encode(n):
    if n == 0:
        return "."
    p = "("
    for i in range(2, n + 1):

        if is_prime[i]:
            value = 0
            while n % i == 0:
                value += 1
                n //= i
            if value == 0:
                p += "."
            else:
                p += f"{encode(value)}"

        if n == 1:
            break
    return p + ')'

n = 0

for i in sys.stdin:
    k = i.split()
    if (k[0]).isdecimal() and int(i) >= 0:
        final_result.append(int(i))
        n = max(n, int(i))
    else:
        print()
        exit()

is_prime = [True] * (n + 1)

for i in range(2, n + 1):
    if is_prime[i]:
        for j in range(i + i, n + 1, i):
            is_prime[j] = False

for i in range(len(final_result)):
    final_result[i] = encode(final_result[i])

for j in range(len(final_result)):
    sys.stdout.write(final_result[j])
    sys.stdout.write('\n')