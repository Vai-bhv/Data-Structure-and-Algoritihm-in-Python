arr1 = [1 ,2 ,3 ,-2,5]
current_sum = max_sum = arr1[0]
# cont = 0
for i in arr1[1:]:
    current_sum += i
    max_sum = max(max_sum,current_sum)
    print(max_sum)

print(max_sum)