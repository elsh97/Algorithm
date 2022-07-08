n,m=map(int, input().split())
nums=[i for i in range(1,n+1)]
s=[]

def permutation_with_overlap(s, nums, m):
    if m==0:
        print(' '.join(list(map(str, s))))
    else:
        for idx, n in enumerate(nums):
            permutation_with_overlap(s+[n],nums,m-1)

permutation_with_overlap(s, nums, m)