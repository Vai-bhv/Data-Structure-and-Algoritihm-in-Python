import math

def cycles(permutation):
    n = len(permutation)
    visited = [False] * n
    cycles = []
    for i in range(1, n + 1):
        if not visited[i - 1]:
            cycle = []
            j = i
            while not visited[j - 1]:
                visited[j - 1] = True
                cycle.append(j)
                j = permutation[j - 1]
            cycles.append(cycle)
    return cycles


n = int(input().strip())
f = [tuple(map(int, input().strip().split())) for _ in range(n)]
visited = []
for i in range(n+1):
    visited.append(False)

permutation = []
for elem in f:
  permutation.append(elem[1])

# print(permutation)
disjointCycles = cycles(permutation)
# print(disjointCycles)

def lcm(numbers):
    lcm = numbers[0]
    for i in range(1, len(numbers)):
        lcm = lcm * numbers[i] // math.gcd(lcm, numbers[i])
    return lcm

lengths = []
for cycle in disjointCycles:
   lengths.append(len(cycle))

# print(lengths)
print(lcm(lengths))

