from collections import Counter
from unittest import TestLoader

n = int(input())
cards = Counter(list(map(int, input().split())))
m = int(input())
test = list(map(int, input().split()))

for t in test:
    print(cards[t], end=' ')
print()