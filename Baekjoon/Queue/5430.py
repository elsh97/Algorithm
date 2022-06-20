from sys import stdin
from collections import deque

t = int(stdin.readline())

for _ in range(t):
    p = deque(stdin.readline().rstrip('\n'))
    n = int(stdin.readline())
    if n!=0:
        nums = deque(map(int, stdin.readline().lstrip('[').rstrip(']\n').split(',')))
    else:
        stdin.readline()
        if 'D' in p:
            print('error')
        else:
            print('[]')
        continue
    answer = ''
    flag = True

    while 0<len(p):
        f = p.popleft()

        if f=='R':
            if 0<len(p) and p[0]=='R':
                p.popleft()
                continue
            else :
                flag = not flag
        else:
            if len(nums)==0:
                answer += 'error'
                break
            elif flag :
                nums.popleft()
            else:
                nums.pop()

    if 'error' in answer:
        print(answer)
    else:
        if not flag:
            nums = list(reversed(nums))
        answer+='['
        for num in nums:
            answer+=( str(num) + ',')
        answer=answer.rstrip(',')+']'
        print(answer)