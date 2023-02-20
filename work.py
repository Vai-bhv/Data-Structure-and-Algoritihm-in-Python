
def isPalindrome(s: str) -> bool:
    k=""
    # s = s.isalpha()
    for char in s:
        if s.isalpha():
            k +=s
    print(k)
    p = k[::-1]
    if p == k :
        return True
    else:
        return False

isPalindrome("race a car")