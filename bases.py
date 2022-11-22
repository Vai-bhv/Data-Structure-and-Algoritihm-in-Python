import sys

SY2VA = {'0': 0,
         '1': 1,
         '2': 2,
         '3': 3,
         '4': 4,
         '5': 5,
         '6': 6,
         '7': 7,
         '8': 8,
         '9': 9,
         'a': 10,
         'b': 11,
         'c': 12,
         'd': 13,
         'e': 14,
         'f': 15,
         'g': 16,
         'h': 17,
         'i': 18,
         'j': 19,
         'k': 20,
         'l': 21,
         'm': 22,
         'n': 23,
         'o': 24,
         'p': 25,
         'q': 26,
         'r': 27,
         's': 28,
         't': 29,
         'u': 30,
         'v': 31,
         'w': 32,
         'x': 33,
         'y': 34,
         'z': 35}
cur_base = -1
des_base = -1

for txt in sys.stdin:
    
    txt = txt[:-1]
    if('>' in txt):
        tt = txt.split('>')
        cur_base = int(tt[0])
        des_base = int(tt[1])
    else:
        integer = 0
        for character in txt:
            value = SY2VA[character]
            integer *= cur_base
            integer += value
        
        VA2SY = dict(map(reversed, SY2VA.items()))
        array = []
        while integer:
            integer, value = divmod(integer, des_base)
            array.append(VA2SY[value])
        answer = ''.join(reversed(array))
        if(answer == ''):
            answer = 0
        print(answer)
