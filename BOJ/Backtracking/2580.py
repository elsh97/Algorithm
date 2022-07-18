from sys import stdin

sudoku = []
for _ in range(9):
    s = list(map(int, stdin.readline().split()))
    sudoku.append(s)

blank = []
for x in range(9):
    for y in range(9):
        if sudoku[x][y] == 0:
            blank.append([x,y])

def playing_sudoku(board, blank):
    if len(blank)==0:
        for row in board:
            for a in row:
                print(a,end=' ')
            print()
        exit()
    x,y = blank[0][0], blank[0][1]
    num = [1,2,3,4,5,6,7,8,9]
    for i in range(9):
        try:
            num.remove(board[x][i])
        except:
            pass
        try:
            num.remove(board[i][y])
        except:
            pass
    for i in range(3):
        xx = (x//3)*3 + i
        for j in range(3):
            yy = (y//3)*3+j
            try:
                num.remove(board[xx][yy])
            except:
                pass
    if len(num)==0:
        return
    for n in num:
        board[x][y]=n
        playing_sudoku(board, blank[1:])
        board[x][y]=0

playing_sudoku(sudoku, blank)