n=int(input())
arr = [[]]*n
for i in range(n):
    arr[i] = list((map(int, input().split())))
arr.sort(key=lambda x:(x[1],x[0]))
for a in arr:
    print(a[0],a[1])