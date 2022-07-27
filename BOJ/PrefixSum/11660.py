from sys import stdin
input = stdin.readline

n, m = map(int, input().split())
sum_matrix = [[0]*(n+1) for _ in range(n)]
for i in range(n):
    num = list(input().split())
    for j in range(1, n+1):
        sum_matrix[i][j] = sum_matrix[i][j-1] + int(num[j-1])

for _ in range(m):
    x1,y1,x2,y2 = map(int, input().split())
    answer = 0 
    for i in range(x1, x2+1):
        answer = answer + sum_matrix[i-1][y2] - sum_matrix[i-1][y1-1]
    print(answer)

# sleep(0.5)
# print()
# for i in range(n):
#     for j in range(n+1):
#         print(sum_matrix[i][j], end=' ')
#     print()