from re import L


t = int(input())
for _ in range(t):
    n = int(input())
    dic = {}
    for _ in range(n):
        k,v = input().split()
        if v in dic:
            dic[v].append(k)
        else:
            dic[v] = [k]
    answer=1
    for k in dic.keys():
        answer *= (len(dic[k])+1)
    print(answer-1)