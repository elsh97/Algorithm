def draw(n):
    if n==1:
        return ['*']

    stars = draw(n//3)
    answer = []
    for s in stars:
        answer.append(s*3)
    for s in stars:
        answer.append(s+' '*(n//3)+s)
    for s in stars:
        answer.append(s*3)

    return answer

n = int(input())
print("\n".join(draw(n)))
