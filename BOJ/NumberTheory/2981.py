import math

t = int(input())
nums = []
gcd=0
for i in range(t):
    nums.append(int(input()))
    if i==0:
        continue
    elif i==1:
        gcd = abs(nums[1]-nums[0])
    else:
        gcd = math.gcd(nums[i]-nums[i-1],gcd)

answer = []
for i in range(2, int(gcd**0.5)+1):
    if gcd%i==0:
        answer.append(i)
        answer.append(gcd//i)
answer.append(gcd)
answer = list(set(answer))
answer.sort()
for a in answer:
    print(a,end=' ')
print()