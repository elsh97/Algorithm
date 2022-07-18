from sys import stdin

t=int(stdin.readline())

for _ in range(t):
    r,s = stdin.readline().split()
    answer = ''
    for c in s:
        answer += c*int(r)
    print(answer)
