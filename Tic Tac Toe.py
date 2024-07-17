win = 0
i = 0
# Board With Coordinates 
board = "   0 1 2 \n A  | | \n   _|_|_ \n B  | | \n   _|_|_ \n C  | | \n    | | "
boardL = list(board)
# Establishing Playable Lines 
lineA = "   "
lineB = "   " 
lineC = "   "
listA = list(lineA)
listB = list(lineB)
listC = list(lineC)
# Player Input 
def inputX(Xin): 
    global board, boardL, listA, listB, listC, lineA, lineB, lineC
    while win == 0:
        Xnum = int(Xin[1])
        if Xin[0] == 'A':
            if Xnum == 0:
                listA[Xnum] = 'X'
                lineA = ''.join(listA)
                boardL[13] = 'X'
                board = ''.join(boardL)
                print(board)
                break
            if Xnum == 1:
                listA[Xnum] = 'X'
                lineA = ''.join(listA)
                boardL[15] = 'X'
                board = ''.join(boardL)
                print(board)
                break
            if Xnum == 2:
                listA[Xnum] = 'X'
                lineA = ''.join(listA)
                boardL[17] = 'X'
                board = ''.join(boardL)
                print(board)
                break
            else:
                print("Incorrect Input, Please Try Again (A1, B2, C3).")
                return
        if Xin[0] == 'B':
            if Xnum == 0:
                listB[Xnum] = 'X'
                lineB = ''.join(listB)
                boardL[32] = 'X'
                board = ''.join(boardL)
                print(board)
                break
            if Xnum == 1:
                listB[Xnum] = 'X'
                lineB = ''.join(listB)
                boardL[34] = 'X'
                board = ''.join(boardL)
                print(board)
                break
            if Xnum == 2:
                listB[Xnum] = 'X'
                lineB = ''.join(listB)
                boardL[36] = 'X'
                board = ''.join(boardL)
                print(board)
                break
            else:
                print("Incorrect Input, Please Try Again (A1, B2, C3).")
                return
        if Xin[0] == 'C':
            if Xnum == 0:
                listC[Xnum] = 'X'
                lineC = ''.join(listC)
                boardL[51] = 'X'
                board = ''.join(boardL)
                print(board)
                break
            if Xnum == 1:
                listC[Xnum] = 'X'
                lineC = ''.join(listC)
                boardL[53] = 'X'
                board = ''.join(boardL)
                print(board)
                break
            if Xnum == 2:
                listC[Xnum] = 'X'
                lineC = ''.join(listC)
                boardL[55] = 'X'
                board = ''.join(boardL)
                print(board)
                break
            else:
                print("Incorrect Input, Please Try Again (A1, B2, C3).")
                return
        else:
            print("Incorrect Input, Please Try Again (A1, B2, C3).")
            return
def inputO(Oin):
    global board, boardL, listA, listB, listC, lineA, lineB, lineC
    while win == 0:
        Onum = int(Oin[1])
        if Oin[0] == 'A':
            if Onum == 0:
                listA[Onum] = 'O'
                lineA = ''.join(listA)
                boardL[13] = 'O'
                board = ''.join(boardL)
                print(board)
                break
            if Onum == 1:
                listA[Onum] = 'O'
                lineA = ''.join(listA)
                boardL[15] = 'O'
                board = ''.join(boardL)
                print(board)
                break
            if Onum == 2:
                listA[Onum] = 'O'
                lineA = ''.join(listA)
                boardL[17] = 'O'
                board = ''.join(boardL)
                print(board)
                break
            else:
                print("Incorrect Input, Please Try Again (A1, B2, C3).")
                return
        if Oin[0] == 'B':
            if Onum == 0:
                listB[Onum] = 'O'
                lineB = ''.join(listB)
                boardL[32] = 'O'
                board = ''.join(boardL)
                print(board)
                break
            if Onum == 1:
                listB[Onum] = 'O'
                lineB = ''.join(listB)
                boardL[34] = 'O'
                board = ''.join(boardL)
                print(board)
                break
            if Onum == 2:
                listB[Onum] = 'O'
                lineB = ''.join(listB)
                boardL[36] = 'O'
                board = ''.join(boardL)
                print(board)
                break
            else:
                print("Incorrect Input, Please Try Again (A1, B2, C3).")
                return
        if Oin[0] == 'C':
            if Onum == 0:
                listC[Onum] = 'O'
                lineC = ''.join(listC)
                boardL[51] = 'O'
                board = ''.join(boardL)
                print(board)
                break
            if Onum == 1:
                listC[Onum] = 'O'
                lineC = ''.join(listC)
                boardL[53] = 'O'
                board = ''.join(boardL)
                print(board)
                break
            if Onum == 2:
                listC[Onum] = 'O'
                lineC = ''.join(listC)
                boardL[55] = 'O'
                board = ''.join(boardL)
                print(board)
                break
            else:
                print("Incorrect Input, Please Try Again (A1, B2, C3).")
                return
        else:
            print("Incorrect Input, Please Try Again (A1, B2, C3).")
            return
# Win Check Function
def wincheck():
    global win, lineA, lineB, lineC
    while win == 0:
        if lineA == 'XXX' or lineA == 'OOO':
            win = 1
            return True
        if lineB == 'XXX' or lineB == 'OOO':
            win = 1
            return True
        if lineC == 'XXX' or lineC == 'OOO':
            win = 1
            return True
        if lineA[0] == 'X' and lineB[0] == 'X' and lineC[0] == 'X':
            win = 1
            return True
        if lineA[1] == 'X' and lineB[1] == 'X' and lineC[1] == 'X':
            win = 1
            return True
        if lineA[2] == 'X' and lineB[2] == 'X' and lineC[2] == 'X':
            win = 1
            return True
        if lineA[0] == 'O' and lineB[0] == 'O' and lineC[0] == 'O':
            win = 1
            return True
        if lineA[1] == 'O' and lineB[1] == 'O' and lineC[1] == 'O':
            win = 1
            return True
        if lineA[2] == 'O' and lineB[2] == 'O' and lineC[2] == 'O':
            win = 1
            return True
        if lineA[0] == 'X' and lineB[1] == 'X' and lineC[2] == 'X':
            win = 1
            return True
        if lineA[2] == 'X' and lineB[1] == 'X' and lineC[0] == 'X':
            win = 1
            return True
        if lineA[0] == 'O' and lineB[1] == 'O' and lineC[2] == 'O':
            win = 1
            return True
        if lineA[2] == 'O' and lineB[1] == 'O' and lineC[0] == 'O':
            win = 1
            return True
        else:
            return False
# Welcome
print("Welcome to Tic Tac Toe, Player 1 (X) Will be First to Move. Input the coordinate where you would like to place your first X (A1,B2,etc.).")
print(board)
while win == 0:
    Xin = input("Player 1(X) to move : ")    
    inputX(Xin)
    i = i + 1
    if wincheck():
        print("Player 1 Wins!")
        break
    else:
        pass
    if i == 9:
        print("CAT! Neither Player Wins!")
        break
    else:
        pass
    Oin = input("Player 2(O) to move : ")
    inputO(Oin)
    i = i + 1
    if wincheck():
        print("Player 2 Wins!")
        break
    else:
        pass
    if i == 9:
        print("CAT! Neither Player Wins!")
        break