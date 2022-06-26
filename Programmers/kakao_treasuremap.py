def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        bin = format(arr1[i]|arr2[i],'b').zfill(n)
        bin = bin.replace('1','#')
        bin = bin.replace('0',' ')
        answer.append(bin)
    print(answer)
    return answer
"""
bin(Integer) -> change Integer into binary "0b0001"
.zfill(n) -> fill blank with 0 to make string size of n
.replace -> return copy of the result
         -> should define with variable (same goes to .sort(), .reverse() , etc.) 
"""


def solution2(n, arr1, arr2):
    answer = []
    for i, j in zip(arr1, arr2):
        a = bin(i|j)[2:]
        a=a.rjust(n, '0')
        a=a.replace('1', '#').replace('0',' ')
        answer.append(a)
    return answer
"""
.rjust(n, character) -> fill blank with character to make string size of n
"""