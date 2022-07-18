s=list(input())
subsets=[]
for i in range(len(s)):
    for j in range(len(s)-i):
        subsets.append(''.join(s[j:j+i+1]))
print(len(set(subsets)))