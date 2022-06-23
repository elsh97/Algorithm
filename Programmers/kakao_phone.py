def solution(numbers, hand):
    answer = ''
    
    if hand == 'left':
        hand='L'
    else:
        hand='R'
    lh, rh = 10,12
    for n in numbers:
        if n in [1,4,7]:
            answer+='L'
            lh = n
        elif n in [3,6,9]:
            answer+='R'
            rh=n
        else:
            if n==0:
                n=11
            ld = abs(n-lh)-3*(abs(n-lh)//3) + abs(n-lh)//3
            rd = abs(n-rh)-3*(abs(n-rh)//3) +abs(n-rh)//3
            print(n,ld,lh,rd,rh)
            if ld>rd:
                answer+='R'
                rh = n
            elif ld<rd:
                answer+='L'
                lh=n
            else:
                answer+=hand
                if hand=='L':
                    lh=n
                else:
                    rh=n
                
    return answer