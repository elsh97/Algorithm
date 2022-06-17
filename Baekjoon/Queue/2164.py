from sys import stdin
from collections import deque

n = int(stdin.readline())
cards=deque([i for i in range(1,n+1)])

while 1<len(cards):
    cards.popleft()
    cards.append(cards.popleft())
print(cards[0])