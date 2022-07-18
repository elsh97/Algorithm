from sys import stdin

h, m = map(int, stdin.readline().rstrip('\n').split())

if 45<=m:
    m-=45
else:
    m += 15
    if h==0:
        h=23
    else:
        h-=1
print(h,m)
