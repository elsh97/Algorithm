from sys import stdin
input = stdin.readline

n = int(input())
paper = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    paper[i] = list(map(int, input().split()))
p, z, m = 0,0,0

def solution(x, y, n):
    global p,z,m
    sign = paper[x][y]
    for i in range(n):
        for j in range(n):
            if sign!=paper[x+i][y+j]:
                solution(x, y, n//3)
                solution(x+n//3, y, n//3)
                solution(x+2*n//3, y, n//3)
                solution(x, y+n//3, n//3)
                solution(x, y+2*n//3, n//3)
                solution(x+n//3, y+n//3, n//3)
                solution(x+n//3, y+2*n//3, n//3)
                solution(x+2*n//3, y+n//3, n//3)
                solution(x+2*n//3, y+2*n//3, n//3)
                return
    if sign==1:
        p+=1
    elif sign==0:
        z+=1
    else:
        m+=1
solution(0,0,n)
print(m)
print(z)
print(p)