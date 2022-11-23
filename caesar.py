def encypt_func(txt, s):  
    result = ""  
    for i in range(len(txt)):  
        char = txt[i]  
        if(char.isalpha()):
            if (char.isupper()):  
                result += chr((ord(char) + s - ord('A') ) % 26 + ord('A'))  
            else:  
                result += chr((ord(char) + s - ord('a')) % 26 + ord('A'))  
        else:
            result += char
    return result
    
num = int(input())
txt = input()
print(encypt_func(txt, num%26))