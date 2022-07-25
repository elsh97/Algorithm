import sys
input = sys.stdin.readline

n = int(input())
paper = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    paper[i] = list(map(int, input().split()))

w,b = 0,0

def solution(x,y,n):
    global w
    global b
    color = paper[x][y]
    for i in range(n):
        for j in range(n):
            if paper[x+i][y+j]!=color:
                solution(x,y,n//2)
                solution(x,y+n//2,n//2)
                solution(x+n//2,y,n//2)
                solution(x+n//2,y+n//2,n//2)
                return
    if color == 0:
        w+=1
    else :
        b+=1
solution(0,0,n)
print(w)
print(b)