#TicTocToe Program
import time 
start_time = time.time()

def show_game_board():
    for i in range(3):
        for j in range(3):
            print(game[i][j], end=' ')
        print()

def check():
     
    if game[0][0] == 'X' and game[0][1] == 'X' and game[0][2] == 'X' :
        print('Player 1 Wins and Time is=',(time.time() - start_time))
        exit()

    elif game[0][0] == 'O' and game[0][1] == 'O' and game[0][2] == 'O' :
        print('Player 2 Winsand Time is=',(time.time() - start_time))
        exit()

    elif game[1][0] == 'X' and game[1][1] == 'X' and game[1][2] == 'X' :
        print('Player 1 Wins and Time is=',(time.time() - start_time))
        exit()
    
    elif game[1][0] == 'O' and game[1][1] == 'O' and game[1][2] == 'O':
        print('Player 2 Wins and Time is=',(time.time() - start_time))
        exit()

    elif game[2][0] == 'X' and game[2][1] == 'X' and game[2][2] == 'X':
        print('Player 1 Wins and Time is=',(time.time() - start_time))
        exit()
    
    elif game[2][0] == 'O' and game[2][1] == 'O' and game[2][2] == 'O':
        print('Player 2 Wins and Time is=',(time.time() - start_time))
        exit()

    elif game[0][0] == 'X' and game[1][0] == 'X' and game[2][0] == 'X':
        print('Player 1 Wins and Time is=',(time.time() - start_time))
        exit()

    elif game[0][0] == 'O' and game[1][0] == 'O' and game[2][0] == 'O':
        print('Player 2 Wins and Time is=',(time.time() - start_time))
        exit()

    elif game[0][1] == 'X' and game[1][1] == 'X' and game[2][1] == 'X':
        print('Player 1 Wins and Time is=',(time.time() - start_time))
        exit()

    elif game[0][1] == 'O' and game[1][1] == 'O' and game[2][1] == 'O':
        print('Player 2 Wins and Time is=',(time.time() - start_time))
        exit()

    elif game[0][2] == 'X' and game[1][2] == 'X' and game[2][2] == 'X':
        print('Player 1 Wins and Time is=',(time.time() - start_time))
        exit()

    elif game[0][2] == 'O' and game[1][2] == 'O' and game[2][2] == 'O':
        print('Player 2 Wins and Time is=',(time.time() - start_time))
        exit()

    elif game[0][0] == 'X' and game[1][1] == 'X' and game[2][2] == 'X':
        print('Player 1 Wins and Time is=',(time.time() - start_time))
        exit()

    elif game[0][0] == 'O' and game[1][1] == 'O' and game[2][2] == 'O':
        print('Player 2 Wins and Time is=',(time.time() - start_time))
        exit()

    elif game[0][2] == 'X' and game[1][1] == 'X' and game[2][0] == 'X':
        print('Player 1 Wins and Time is=',(time.time() - start_time))
        exit()

    elif game[0][2] == 'O' and game[1][1] == 'O' and game[2][0] == 'O':
        print('Player 2 Wins and Time is=',(time.time() - start_time))
        exit()
 
game=[['_','_','_'],
      ['_','_','_'],
      ['_','_','_']]

show_game_board()
check()
while True:
#for i in range(3):
   # for j in range(3):
       # print(game[i][j], end=' ')
    #print()
    print('Player 1.')
    while True:
        row=int(input('satr ra vard kon='))
        col=int(input('soton ra vard kon='))
        if 0<= row <=2 and 0<=col <=2:
            if game[row][col]=='_':
                game[row][col]='X'
                break
            else:
                print('Cell is not empty!')
        else:
            print('out of Range try again')

    show_game_board()
    check()
    #for i in range(3):
    # for j in range(3):
        #  print(game[i][j], end=' ')
        #print()


    print('Player 2.')
    while True:
        row=int(input('satr ra vard kon='))
        col=int(input('soton ra vard kon='))
        if 0<= row <=2 and 0<=col <=2:
            if game[row][col]=='_':
                game[row][col]='O'
                break
            else:
                print('cell is not empty')
        else:
            print('out of Range try again')
    show_game_board()
    check()
    #for i in range(3):
    # for j in range(3):
        #  print(game[i][j], end=' ')
        #print()