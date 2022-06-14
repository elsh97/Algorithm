def solution(places):
    answer=[]
    for x in range(0,5) :
        answer.append(1)
        waiting_room = []
        for y in range(0,5):
            print(x,y)
            waiting_room.append(list(places[x][y]))
        print(waiting_room)
        
        flag = 1
        for p in range(0,5) :
            for q in range(0,5) :
                print(p,q)
                count=0
                if waiting_room[p][q] == 'P':
                    if (0<p-1 and waiting_room[p-1][q] != 'P') and\
                     (0<q-1 and waiting_room[p][q-1] != 'P') and\
                     (p+1<5 and waiting_room[p+1][q] != 'P') and\
                     (q+1<5 and waiting_room[p][q+1] != 'P') :
                        continue
                    else:
                        flag =0
                        break
                elif waiting_room[p][q] == 'O':
                    if(0<p-1 and waiting_room[p-1][q] == 'P'):
                        count +=1
                    if (0<q-1 and waiting_room[p][q-1] == 'P'):
                        count+=1
                    if (p+1<5 and waiting_room[p+1][q] == 'P'):
                        count+=1
                    if (q+1<5 and waiting_room[p][q+1] == 'P'):
                        count+=1
                    if count>1:
                        flag =0 
                        break

                print(p,q,flag)
            if flag==0:
                break
        if flag==0:
            answer[x]=0
    return answer



places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"] , ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]

solution(places)