s=list(input())
key = ['=','-','j']

answer = len(s)

for idx,c in enumerate(s):
    if c=='=':
        answer-=1
        if ''.join(s[idx-2:idx])=='dz':
            answer-=1
    elif c=='-':
        answer-=1
    elif c=='j' and (s[idx-1]=='l' or s[idx-1]=='n'):
        answer-=1
    else:
        pass
print(answer)