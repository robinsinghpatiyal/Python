
n = int(input())
lst=[]
for i in range(n):
    dig = int(input())
    lst.append(dig)
lst.sort()
mlst = list(dict.fromkeys(lst))
print(mlst[-2])
    

'''
    n = int(input())
    arr = list(map(int, input().split()))
    zes = max(arr)
    i=0
    while(i<n):
        if zes ==max(arr):
            arr.remove(max(arr))
        i+=1
    print(max(arr))
'''