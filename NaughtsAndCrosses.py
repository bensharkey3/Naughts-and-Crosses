# naughts and crosses game

board = [' 'for i in range(9)]

def displayboard():
    '''displays the board'''
    row1 = " {} | {} | {} ".format(board[0], board[1], board[2])
    mid1 = "-----------"
    row2 = " {} | {} | {} ".format(board[3], board[4], board[5])
    mid2 = "-----------"
    row3 = " {} | {} | {} ".format(board[6], board[7], board[8])
    
    print('')
    print(row1)
    print(mid1)
    print(row2)
    print(mid2)
    print(row3)
    print('')
        
while True:
    displayboard()
    choice = int(input('Enter your move (1-9): '))
    if board[choice-1] == ' ':
        board[choice-1] = 'X'
    else:
        print()
        print('That move is already taken!')