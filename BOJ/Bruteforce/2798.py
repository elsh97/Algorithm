n,m = map(int, input().split())
cards = list(map(int,input().split()))

cards = sorted(cards, reverse=True)

sums = []
for i in range(len(cards)-2):
    for j in range(i+1,len(cards)):
        for k in range(j+1, len(cards)):
            if cards[i]+cards[j]+cards[k]<=m:
                sums.append(cards[i]+cards[j]+cards[k])

print(max(sums))