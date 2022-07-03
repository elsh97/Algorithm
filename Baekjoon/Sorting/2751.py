from sys import stdin
a = int(stdin.readline())
arr = []
for _ in range(a):
    arr.append(int(stdin.readline()))
arr.sort()
for i in arr:
    print(i)