def solution(n):
    if n==0:
        return 1
    return n*solution(n-1)

n = int(input())
print(solution(n))