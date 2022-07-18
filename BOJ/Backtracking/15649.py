answer = []

def permutation(cur, nums, m):
    if m==0:
        answer.append(cur)
    else:
        for idx, n in enumerate(nums):
            permutation(cur+[n], nums[:idx]+nums[idx+1:], m-1)

n,m=map(int, input().split())
nums = [i for i in range(1,n+1)]

cur=[]
permutation(cur, nums, m)
for row in answer:
    for a in row:
        print(a, end=' ')
    print()