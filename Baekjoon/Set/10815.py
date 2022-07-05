n=int(input())
card = set(map(int, input().split()))
m = int(input())
test = list(map(int, input().split()))

for t in test:
    if t in card:
        print(1, end=' ')
    else:
        print(0, end=' ')
print()