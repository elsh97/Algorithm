from sys import stdin
input = stdin.readline

n = int(input())
meeting = [[] for _ in range(n) ]
for i in range(n):
    meeting[i] = list(map(int, input().split()))
meeting.sort(key=lambda x:(x[1],x[0]))

count, end = 1, meeting[0][1]
for m in meeting[1:]:
    if end<=m[0]:
        count+=1
        end = m[1]
print(count)