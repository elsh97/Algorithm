def solution(dartResult):
    time_dict = {'S':1, 'D':2, 'T':3}
    tmp = []
    for _ in range(3):
        score = -1
        time = -1
        option = ''
        
        if dartResult[:2].isdigit():
            score = int(dartResult[:2])
            dartResult = dartResult[2:]
        else:
            score = int(dartResult[0])
            dartResult = dartResult[1:]
        
        time = time_dict[dartResult[0]]
        dartResult = dartResult[1:]
        
        if 0<len(dartResult) and not dartResult[0].isdigit():
            option=dartResult[0]
            dartResult=dartResult[1:]
        

        tmp.append(score**time)

        if option == '#':
            tmp[-1] *= -1
        elif option == '*':
            if 1<len(tmp):
                tmp[-2] *= 2
            tmp[-1] *= 2
        else:
            pass
    
    answer = sum(tmp)

    return answer

"""
while parsing the list..
let tmp = [1]
tmp[-2:] = [1] -> it doesn't make an error

but tmp[-2] -> occurs IndexError
"""