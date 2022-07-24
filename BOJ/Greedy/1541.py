from sys import stdin
input = stdin.readline

answer = 0
ss = input().rstrip().split('-')
answer = 0
for idx, s in enumerate(ss):
    pp = s.split('+')
    tmp = 0
    for p in pp:
        tmp+=int(p)
    if idx==0:
        answer+=tmp
    else:
        answer-=tmp
print(answer)