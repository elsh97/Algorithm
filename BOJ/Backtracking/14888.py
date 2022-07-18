n = int(input())
num = list(map(int, input().split()))
add,sub,mul,div = list(map(int, input().split()))
answer = []

def solution(depth, total, add, sub, mul, div):
    if depth==n:
        answer.append(total)
        return
    
    if add:
        solution(depth+1, total+num[depth],add-1,sub,mul,div)
    if sub:
        solution(depth+1, total-num[depth],add,sub-1,mul,div)
    if mul:
        solution(depth+1, total*num[depth],add,sub,mul-1,div)
    if div:
        if total<0:
            solution(depth+1, ((total*-1)//num[depth])*-1,add,sub,mul,div-1)
        else:
            solution(depth+1, total//num[depth],add,sub,mul,div-1)

solution(1, num[0], add, sub, mul, div)
answer.sort()
print(answer[-1])
print(answer[0])