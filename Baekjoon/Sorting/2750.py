a = int(input())
arr = []
for _ in range(a):
    arr.append(int(input()))
arr.sort()
while arr:
    print(arr.pop(0))