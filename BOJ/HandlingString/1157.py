"""
단순 Dictionary 사용
"""
s=input().lower()
d=dict()
for c in s:
    if c in d:
        d[c] +=1
    else:
        d[c] = 1

answer = [a for a in d.keys() if max(d.values())==d[a]]
if 1<len(answer):
    print('?')
else:
    print(answer[0].upper())




"""
Collections-Counter 사용한 풀이
"""
# from collections import Counter
# s=input().lower()
# c = Counter(s)
# answer = [a for a in c.keys() if c[a]==max(c.values())]
# if 1<len(answer):
#     print('?')
# else:
#     print(answer[0].upper())