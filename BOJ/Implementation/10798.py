from sys import stdin
s = []
for i in range(5):
    s.append(list(stdin.readline().rstrip('\n')))

max_len = 0
for ss in s:
    if max_len<len(ss):
        max_len = len(ss)
# print(max_len)

answer = ''
for i in range(max_len):
    for j in range(5):
        if len(s[j])<=i:
            continue
        answer += s[j][i]
print(answer)