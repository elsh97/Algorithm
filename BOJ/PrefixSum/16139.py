from sys import stdin
input = stdin.readline

s = list(input())
q = int(input())

"""
Score : 100
  1. Can reduce the number of iteration by saving data alphabetically
  2. The time of accessing array vertical is faster than accessing horizontal 
"""
d = [[0]*26 for _ in range(len(s)+1)]
for i in range(1, len(s)+1):
    x = ord(s[i-1])-ord('a')
    for j in range(26):
        if j==x:
            d[i][j] = d[i-1][j]+1
        else:
            d[i][j] = d[i-1][j]

for _ in range(q):
    buf = input().split()
    t = ord(buf[0])-ord('a')
    start, end = int(buf[1]), int(buf[2])+1
    print(d[end][t]-d[start][t])
    
"""
Score : 50
for _ in range(q):
    buf = input().split()
    t, start, end = buf[0], int(buf[1]), int(buf[2])+1
    s_t = [1 if l==t else 0 for l in s]
    ps = [0]*(len(s)+1)
    for i in range(1, len(s)+1):
        ps[i] = ps[i-1] + s_t[i-1]
    print(ps[end]-ps[start])
"""