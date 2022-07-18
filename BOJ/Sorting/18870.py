n=int(input())
arr=list(map(int, input().split()))
arr1=arr.copy()
arr1.sort()
i=0
dic = {}
for a in arr1:
    if a in dic:
        pass
    else:
        dic[a]=i
        i+=1
for idx, a in enumerate(arr):
    print(dic[a], end=' ')
print()