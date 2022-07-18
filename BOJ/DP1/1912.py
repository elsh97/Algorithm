n = int(input())
nums = map(int, input().split())
d= []
tmp, answer = -1e99, -1e99

for num in nums:
    if tmp==-1e99 or tmp+num<num:
        tmp=num
    elif 0<tmp+num:
        tmp+=num
    else :
        tmp = -1e99
    
    if answer<tmp:
        answer = tmp
    d.append(answer)

print(d[-1])

"""
Better Solution
"""
n = int(input())
a = [int(i) for i in input().split(" ")]
dp = [0] * n
dp[0] = a[0]
for i in range(1, n):
    dp[i] = max(a[i], dp[i-1] + a[i])
    print(dp)
print(max(dp))
