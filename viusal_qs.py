def quick_Sort(a, low, high, depth):
    if low >= high:
        return
    pivot = lomouto_partition(a, low, high)
    output_partition(a, low, high + 1, pivot, depth)
    quick_Sort(a, low, pivot - 1, depth + 1)
    quick_Sort(a, pivot + 1, high, depth + 1)


def lomouto_partition(a, low, high):
    pivot = a[high]

    i = (low - 1)
    for j in range(low, high):
        if (a[j] <= pivot):
            i += 1
            a[i], a[j] = a[j], a[i]
    a[i + 1], a[high] = a[high], a[i + 1]
    return (i + 1)

def output_partition(a, lo, hi, pivot, depth):
    if pivot == 0:
        print(f"{depth:02d}:", end="")
    else:
        print(f"{depth:02d}: ", end="")
    for i in range(0, hi):
        if i < lo:
            if i + 1 == pivot:
                print(end=" " * 2)
            else:
                print(end=" " * 3)
        elif i == pivot:
            print(f"[{a[i]:02d}]", end="")
        elif i + 1 == pivot:
            print(f"{a[i]:02d}", end="")
        else:
            print(f"{a[i]:02d}", end=" ")
    print()

a = [int(x) for x in input().split()]

output_partition(a, 0, len(a), len(a), 0)
quick_Sort(a, 0, len(a) - 1, 1)
output_partition(a, 0, len(a), len(a), 0)