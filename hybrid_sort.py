import sys

arr1 = sys.stdin.readline().split(" ")
arr1 = [int(x) for x in arr1]

fs = '    '
def merge(arr1, d, e, f, t):
    a = arr1[d:e]  
    b = arr1[e:f]  

    i = 0 
    j = 0 
    if (a[-1] <= b[0]):
        print(fs*t+"skipped merge!")
    else:
        print(fs*t+"merged a["+str(d)+":"+str(e)+"] + a["+str(e)+":"+str(f)+"] -> a["+str(d)+":"+str(f)+"]")
        for k in range(d, f):
            if i == len(a):  
                arr1[k] = b[j]
                j += 1
            elif j == len(b):  
                arr1[k] = a[i]
                i += 1
            elif a[i] < b[j]:
                arr1[k] = a[i]
                i += 1
            else:
                arr1[k] = b[j]
                j += 1



def merge_sort_range(a, i, j, t):
    if j-i < 2:
        return
    elif j - i <= 10:
        insertion_sort(a, i, j, t+1)
        return

    mid = (i + j) // 2
    print(fs*t+"sorting a["+str(i)+":"+str(mid)+"] = "+printArr(a,i,mid))
    merge_sort_range(a, i, mid, t+1)  
    print(fs*t+"sorted a["+str(i)+":"+str(mid)+"] = "+printArr(a,i,mid))
    print(fs*t+"sorting a["+str(mid)+":"+str(j)+"] = "+printArr(a,mid,j))
    merge_sort_range(a, mid, j, t+1) 
    print(fs*t+"sorted a[" + str(mid) + ":" + str(j) + "] = " + printArr(a, mid, j))
    merge(a, i, mid, j, t)  



def merge_sort(a):
    print("sorting a["+str(0)+":"+str(len(a))+"] = "+printArr(a,0,len(a)))
    merge_sort_range(a, 0, len(a), 1)
    print("sorted a[" + str(0) + ":" + str(len(a)) + "] = " + printArr(a, 0, len(a)))

def insertion_sort(a, i1, j1, k):
    count = 0
    for i in range(i1,j1):
        t = a[i]
        j = i - 1
        while j >= i1:
            count += 1      
            if a[j] <= t:
                break      
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = t
    print(fs*k+'insertion sort ('+str(count)+' compares)')

def printArr(a,i1,j1):
    res = "["
    if(len(a[i1:j1])>10):
        for i in range(i1,i1+5):
            res+=str(a[i])+" "
        res+="... "
        for i in range(j1-5,j1):
            res+=str(a[i])+" "
        return res[:-1]+"]"
    else:
        for i in range(i1,j1):
            res+=str(a[i])+" "
        return res[:-1]+"]"
merge_sort(arr1)