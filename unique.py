string = "aaabcde"

seen = set()

for char in string:
    if char not in seen:
        seen.add(char)
    else:
        print("not unique")
        break

if len(string) == len(seen):
    print("its unique")