def solution(arr):
    if len(arr)<=1:
        return arr
    pivot = arr[len(arr)//2]
    less, equal, greater = [], [], []
    for num in arr:
        if num<pivot:
            less.append(num)
        elif num==pivot:
            equal.append(num)
        else:
            greater.append(num)
    return solution(less)+equal+solution(greater)


test_set = [
    [3,45,6,1,2,5,76,7],
    [21,547,87,3,2,45,7,9],
    [1,2],
    [1,2,3,5],
    [8,24,6,32,4,7,42,5,147,1,35,3]
]

print("-"*10,"Quick Sort","-"*10)
for i,arr in enumerate(test_set):
    print("#{} : {}".format(i, solution(arr)))