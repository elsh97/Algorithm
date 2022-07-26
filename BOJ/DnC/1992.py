from sys import stdin
input = stdin.readline

n = int(input())
px = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    px[i] = list(input().rstrip())
answer=''

def solution(x, y, n):
    global answer
    pixel = px[x][y]
    for i in range(n):
        for j in range(n):
            if px[x+i][y+j]!=pixel:
                answer+='('
                solution(x,y,n//2)
                solution(x,y+n//2,n//2)
                solution(x+n//2, y,n//2)
                solution(x+n//2, y+n//2, n//2)
                answer+=')'
                return
    if pixel == '1':
        answer+='1'
    else :
        answer+='0'

solution(0,0,n)
print(answer)