def are_shift_equivalent(list1, list2):
    # Check if the lists are not the same length
    if len(list1) != len(list2):
        return False
    
    # Check if the lists are the same
    if list1 == list2:
        return True
    
    # Try all possible shifts
    for i in range(len(list2)):
        # Shift the list to the right
        shifted = list2[-i:] + list2[:-i]
        
        # Check if the shifted list is equal to the first list
        if shifted == list1:
            return True
        
    # Return False if no shift was successful
    return False

# Read the first list
list1 = []
while True:
    n = int(input())
    if n == -1:
        break
    list1.append(n)

# Read the second list
list2 = []
while True:
    n = int(input())
    if n == -1:
        break
    list2.append(n)

# Check if the lists are shift-equivalent
if are_shift_equivalent(list1, list2):
    # Find the required shift
    for i in range(len(list2)):
        # Shift the list to the right
        shifted = list2[-i:] + list2[:-i]
        
        # Check if the shifted list is equal to the first list
        if shifted == list1:
            print(i)
            break
else:
    print(-1)
