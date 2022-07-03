from collections import Counter
n = int(input())
arr = [0]*n
for i in range(n):
    arr[i]=int(input())
arr.sort()
arr_c = Counter(arr)

mode = [k for k,v in arr_c.items() if v==max(arr_c.values())]

#산술평균
print(round(sum(arr)/n))
#중앙값
print(arr[len(arr)//2])
#최빈값
if 1<len(mode):
    print(mode[1])
else:
    print(mode[0])
#범위
print(arr[-1]-arr[0])