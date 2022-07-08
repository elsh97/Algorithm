n, m = map(int, input().split())
nums = [i for i in range(1,n+1)]
s = []

def permutation_conditioned(s, nums, m):
    if m==0:
        print(' '.join(list(map(str, s))))
    else:
        for idx, i in enumerate(nums):
            if 0<len(s) and i<=s[-1]:
                continue
            else:
                s.append(i)
                permutation_conditioned(s, nums[:idx]+nums[idx+1:], m-1)
                s.pop()

permutation_conditioned(s, nums, m)