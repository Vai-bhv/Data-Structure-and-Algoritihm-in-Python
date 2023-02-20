import collections

def finder(arr1,arr2):
    dict = collections.defaultdict(int)

    for num in arr2:
        dict[num] +=1
    
    for num in arr1:
        if dict[num] == 0:
            print(num)
        else:
            dict[num] -= 1


arr1 = [5,5,7,7]
arr2 = [5,7,7]
finder(arr1,arr2)
