from sys import stdin
input = stdin.readline

def makeMat(n):
    tmp = [0 for _ in range(n)]
    for i in range(n):
        tmp[i] = list(map(int, input().split()))
    return tmp

def printMat(mat):
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            print(mat[i][j], end = ' ')
        print()

n, m = map(int, input().split())
a = makeMat(n)
m, k = map(int, input().split())
b = makeMat(m)

answer = [[0 for _ in range(k)] for _ in range(n)]

for i in range(n):
    for j in range(k):
        for p in range(m):
            answer[i][j] += a[i][p]*b[p][j]
printMat(answer)