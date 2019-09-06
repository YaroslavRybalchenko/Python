import random
#GLOBAL CONSTANTS
k=0
X='X'
O='O'
EMPTY=' '
LENGTH=9
TIE='Ничья'
#FUNCTIONS
def display_instruction():
    print('Ячейки поля пронумерованы следующим образом: ')
    print('''
\t 0 | 1 | 2
\t ---------
\t 3 | 4 | 5
\t ---------
\t 6 | 7 | 8
''')

def yes_no_question(question):
    answer=None
    while answer not in ('Y','N','y','n'):
        answer=input(question)
        if answer not in ('Y','N','y','n'):
            print('Введен недопустимый символ!')
    return answer

def get_number(question,low,high):
    number=None
    while not number in range(int(low),int(high)):
        number=int(input(question))
    return number

def game_order():
    answer=yes_no_question('Будете ходить первым?(y/n): ')
    if answer.lower()=='y':
        player=X
        computer=O
    elif answer.lower()=='n':
        player=O
        computer=X
    return computer,player

def clear_board():
    board=[]
    for i in range(LENGTH):
        board.append(EMPTY)
    return board

def display_board(board):
    print('\t',board[0],' | ',board[1],' | ',board[2])
    print('\t -------------')
    print('\t',board[3],' | ',board[4],' | ',board[5])
    print('\t -------------')
    print('\t',board[6],' | ',board[7],' | ',board[8])
        
def allowed_cells(board):
    allowed=[]
    for i in range(LENGTH):
        if board[i]==EMPTY:
            allowed.append(i)
    return allowed

def winner(board):
    WAYS_ТО_WIN=((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    for i in WAYS_ТО_WIN:
        if board[i[0]]==board[i[1]]==board[i[2]] and board[i[0]]!=EMPTY:
            winner=board[i[0]]
            return winner
        if EMPTY not in board:
            return TIE
    return None

def player_move(board,human):
    move=None
    while move not in allowed_cells(board):
        move=get_number('Выберите ячейку для хода: ',0,LENGTH)
        if move not in allowed_cells(board):
            print('Данная ячейка уже занята.')
    return move

def computer_move(board,computer,player,strategy):
    global k
    board=board[:]
    MOVESET_1=(4,2,8,6,0,1,3,5,7)
    MOVESET_2=(0,4,3,1,2,5,8,7,6)
    print("Я выберу поле номер", end=" ")
    for move in allowed_cells(board):
        board[move]=computer
        if winner(board)==computer:
            print(move)
            return move
        board[move]=EMPTY
    for move in allowed_cells(board):
        board[move]=player
        if winner(board)==player:
            print(move)
            return move
        board[move]=EMPTY
    if (board[0]!=player and board[2]!=player and board[6]!=player and board[8]!=player):
        k=1
    if k==1 and strategy==0:
        for move in MOVESET_2:
            if move in allowed_cells(board):
                 print(move)
                 return move
    else:
        for move in MOVESET_1:
            if move in allowed_cells(board):
                print(move)
                return move

def next_turn(turn):
    if turn==X:
        return O
    else:
        return X

def congratulations(the_winner,computer,player):
    if the_winner!=TIE:
        print("Tpи", the_winner, "в ряд!\n")
    else:
        print("Hичья!\n")
    if the_winner==computer:
        print('Победил компьютер.')
    elif the_winner==player:
        print("Вы победили")
    elif the_winner==TIE:
        print("Hичья!\n")

def main():
    display_instruction()
    strategy=random.randint(0,1)
    computer,player = game_order()
    turn=X
    board=clear_board()
    display_board(board)
    while not winner(board):
        if turn==player:
            move=player_move(board,player)
            board[move]=player
        else:
            move=computer_move(board,computer,player,strategy)
            board[move]=computer
        display_board(board)
        turn=next_turn(turn)
    the_winner=winner(board)
    congratulations(the_winner,computer,player)

main()
input()
