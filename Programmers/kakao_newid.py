def solution(new_id):
    answer=''
    new_id = new_id.lower()
    
    flag=False
    for c in new_id:
        if c.isalpha() or c=='-' or c=='_' or c.isdigit():
            answer+=c
            flag=False
        elif c=='.':
            if flag is True:
                continue
            else:
                answer+=c
                flag = True
        else:
            continue
    
    if 0<len(answer) and answer[0]=='.':
        answer = answer[1:]
    if 0<len(answer) and answer[-1]=='.':
        answer = answer[:-1]
    
    if len(answer)==0:
        answer='a'
    
    if 16<=len(answer):
        answer = answer[:15]
        if answer[-1]=='.':
            answer = answer[:-1]
    
    while len(answer)<3:
        answer += answer[-1]
    
    return answer