t = int(input())
count=0

for _ in range(t):
    s=list(input())
    flag=True
    for idx, c in enumerate(s):
        k=0
        while idx+k<len(s) and c==s[idx+k]:
            k+=1
        if 0<s[idx+k+1:].count(c):
            flag=False
            break
    if flag:
        count+=1
print(count)