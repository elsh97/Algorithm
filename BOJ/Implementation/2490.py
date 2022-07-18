from sys import stdin

yut_dict = {1:'A', 2:'B', 3:'C', 4:'D', 0:'E'}
for _ in range(3):
    yuts=list(stdin.readline().rstrip('\n').split())
    outcome = yut_dict[yuts.count('0')]
    print(outcome)