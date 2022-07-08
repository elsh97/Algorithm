n,m=map(int, input().split())
nums=[i for i in range(1,n+1)]
s=[]

def permutation_not_descending(s, nums, m):
    if m==0:
        print(' '.join(list(map(str, s))))
    else:
        for idx, n in enumerate(nums):
            if 0<len(s) and n<s[-1]:
                continue
            permutation_not_descending(s+[n],nums,m-1)

permutation_not_descending(s,nums,m)