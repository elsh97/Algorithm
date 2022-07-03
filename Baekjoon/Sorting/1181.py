n = int(input())
arr = []

for i in range(n):
    s=input()
    if s not in arr:
        arr.append(s)
arr.sort(key=lambda x:(len(x),x))
for a in arr:
    print(a)