def solution(board, moves):
    box = []
    answer=0
    cart = []*len(board)
    for i in range(len(board)):
        cart.append([])
    for row in board:
        for idx, d in enumerate(row):
            if d==0:
                continue
            else:
                cart[idx].append(d)
    
    for mv in moves:
        if len(cart[mv-1])==0:
            continue
        else:
            box.append(cart[mv-1][0])
            cart[mv-1]=cart[mv-1][1:]
        
        if 2<=len(box) and box[-2]==box[-1]:
            box.pop()
            box.pop()
            answer+=2
    return answer