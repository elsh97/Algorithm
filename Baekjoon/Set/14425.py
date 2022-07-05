n, m = map(int, input().split())
s=set()
for _ in range(n):
    s.add(input())

answer = 0
for _ in range(m):
    if input() in s:
        answer+=1
print(answer) 