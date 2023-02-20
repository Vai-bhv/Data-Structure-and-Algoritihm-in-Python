def pair_sum(arr,k):
    seen = set()
    output = set()
    target = 0
    for num in arr:
        target = k - num
        if target not in seen:
            seen.add(num)
        else:
            output.add( ((min(num, target)) , max(target,num)))
    print(len(output))
                              


arr1 = [1,2,2,3]
k = int(input())
pair_sum(arr1,k)