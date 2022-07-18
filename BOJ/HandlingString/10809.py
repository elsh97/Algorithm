s = input()
answer = [-1]*26

for i in range(97, 123):
    if chr(i) in s:
        answer[i-97] = s.index(chr(i))

for i in answer:
    print(i, end=' ')