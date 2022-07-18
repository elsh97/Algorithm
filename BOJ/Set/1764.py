n,m = map(int, input().split())
nohear = set()
nosee = set()

for _ in range(n):
    nohear.add(input())
for _ in range(m):
    nosee.add(input())

com = list(nohear.intersection(nosee))
com.sort()
print(len(com))
for c in com:
    print(c)