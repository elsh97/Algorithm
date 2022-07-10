n = int(input())
ability=[]
visited=[False for _ in range(n)]
answer=int(1e99)

for _ in range(n):
    ability.append(list(map(int, input().split())))

num = [i for i in range(n)]

def dfs(depth, idx):
    global answer
    if depth==n//2:
        start,link=0,0
        for i in range(n):
            for j in range(n):
                if visited[i] and visited[j]:
                    start +=ability[i][j]
                elif not visited[i] and not visited[j]:
                    link += ability[i][j]
        answer = min(answer, abs(start-link))
        return
    
    for i in range(idx, n):
        if not visited[i]:
            visited[i]=True
            dfs(depth+1, i+1)
            visited[i]=False

dfs(0,0)
print(answer)



# Out of Time
# n = int(input())
# ability=[]
# visited=[False for _ in range(n)]
# answer=[]
# def teaming(start,num):
#     if len(start)==n//2:
#         link = [nn for nn in num if n not in start]
#         start_a, link_a=0,0
#         for x in start:
#             for y in start:
#                 start_a+=ability[x][y]
#         for x in link:
#             for y in link:
#                 link_a+=ability[x][y]
#         answer.append(abs(start_a-link_a))
#         return
    
#     for idx,nn in enumerate(num):
#         if nn not in start:
#             teaming(start+[nn], num[:idx]+num[idx+1:])

# start=[]
# teaming(start, num)
# answer.sort()
# print(answer[0])