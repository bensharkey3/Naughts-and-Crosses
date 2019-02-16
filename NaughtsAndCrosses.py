### naughts and crosses game

board = [' 'for i in range(9)]
'''creates the board'''


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


def playermove(icon):
    '''modifies the board with the players input'''
    print("Your turn player '{}'".format(icon))
    choice = 'blank'
    while choice not in list(range(1,10)):
        choice = int(input('Enter your move (1-9): '))
    if board[choice-1] == ' ':
        board[choice-1] = icon
    else:
        print()
        print('That move is already taken, wasted turn!')
        

def victory(icon):
    '''checks to see if a voctory has occurred'''
    if (board[0] == icon and board[1] == icon and board[2] == icon) or \
    (board[3] == icon and board[4] == icon and board[5] == icon) or \
    (board[6] == icon and board[7] == icon and board[8] == icon) or \
    (board[0] == icon and board[3] == icon and board[6] == icon) or \
    (board[1] == icon and board[4] == icon and board[7] == icon) or \
    (board[2] == icon and board[5] == icon and board[8] == icon) or \
    (board[0] == icon and board[4] == icon and board[8] == icon) or \
    (board[2] == icon and board[4] == icon and board[6] == icon):
        return True
    else:
        return False


def draw():
    '''checks to see if a draw has occurred'''
    if ' ' not in board:
        return True
    else:
        return False


while True:
    '''runs steps of the program'''
    displayboard()
    playermove('O')
    displayboard()
    if victory('O'):
        print("'O' Wins!")
        break
    elif draw():
        print ('Its a Draw!')
        break
    playermove('X')
    if victory('X'):
        print("'X' Wins!")
        break
    elif draw():
        print ('Its a Draw!')
        break

input('Press any key to exit')
