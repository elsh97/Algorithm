def solution(n):
    if n==1 or n==2:
        return 1
    elif n==0:
        return 0
    else:
        return solution(n-1)+solution(n-2)

n=int(input())
print(solution(n))