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
    prime_set = set(i for i in range(2, max_factor+1))
    prime_list = []
    prime_flags = [True] * (max_factor+1)
    prime_flags[0] = prime_flags[1] = False
    # for i in range(len(prime_flags)):
    #     print(i,prime_flags[i])
    # print((int(max_factor ** 0.5)+1), "bdsfb")
    # print(max_num, max_factor,int(max_factor ** 0.5) + 1 , "line 32"); 
    # for i in range(2, int(max_factor ** 0.5) + 1):
        # print(max_num, max_factor, i, "line 34")
    # for i in range(2, int(max_factor ** 0.5) + 1):
    for i in range(2, max_factor  + 1):
        if prime_flags[i]:
            # print(max_num, max_factor, i, "line 35")
            prime_list.append(i)
            for j in range(i*i, max_factor+1, i):
                # print(i,j)
                prime_flags[j] = False
    # print(prime_list)
    # print(prime_set)
    # print(int(max_factor ** 0.5) +1, max_factor + 1 ,"line 44" )
    # for i in range(2, int(max_factor ** 0.5) + 1):
    #     if i in prime_set:
    #         prime_set -= set(range(i*i, max_factor+1, i))
    # print(prime_set)
    # prime_list = sorted(prime_set)
    # print(prime_list)
    ekString = ''
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

