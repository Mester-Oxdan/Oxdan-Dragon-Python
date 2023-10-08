from msvcrt import getch
import os
import random
from colorama import Fore
import imports.own.will_go_to_start

def tic_tac_toe_ai_start():

            os.system('cls')
            board = [' ' for x in range(10)]

            def insertLetter(letter, pos):
                board[pos] = letter

            def spaceIsFree(pos):
                return board[pos] == ' '

            def printBoard(board):
                os.system('cls')
                print('Welcome to Tic-Tac-Toe ai!')
                print('-----------')
                print('   |   |')
                print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
                print('   |   |')
                print('-----------')
                print('   |   |')
                print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
                print('   |   |')
                print('-----------')
                print('   |   |')
                print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
                print('   |   |')
                print('-----------')
    
            def isWinner(bo, le):
                return (bo[7] == le and bo[8] == le and bo[9] == le) or (bo[4] == le and bo[5] == le and bo[6] == le) or(bo[1] == le and bo[2] == le and bo[3] == le) or(bo[1] == le and bo[4] == le and bo[7] == le) or(bo[2] == le and bo[5] == le and bo[8] == le) or(bo[3] == le and bo[6] == le and bo[9] == le) or(bo[1] == le and bo[5] == le and bo[9] == le) or(bo[3] == le and bo[5] == le and bo[7] == le)

            def playerMove():
                run = True
                while run:
                    move = input('\nPlease select a position to place for \033[0;33mX\033[0;37m (1-9): ')
                    try:
                        move = int(move)
                        if move > 0 and move < 10:
                            if spaceIsFree(move):
                                run = False
                                insertLetter('X', move)
                            else:
                                
                                print(Fore.RED + "\n(!ERROR!) " + Fore.WHITE + "=" + Fore.GREEN + " (!Already occupied!)" + Fore.WHITE)
                        else:
                            
                            print(Fore.RED + "\n(!ERROR!) " + Fore.WHITE + "=" + Fore.GREEN + " (!Out of range!)" + Fore.WHITE)

                    except:

                        print(Fore.RED + "\n(!ERROR!) " + Fore.WHITE + "=" + Fore.GREEN + " (!Only integers!)" + Fore.WHITE)

            def compMove():
                possibleMoves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
                move = 0

                for let in ['O', 'X']:
                    for i in possibleMoves:
                        boardCopy = board[:]
                        boardCopy[i] = let
                        if isWinner(boardCopy, let):
                            move = i
                            return move

                cornersOpen = []
                for i in possibleMoves:
                    if i in [1,3,7,9]:
                        cornersOpen.append(i)
            
                if len(cornersOpen) > 0:
                    move = selectRandom(cornersOpen)
                    return move

                if 5 in possibleMoves:
                    move = 5
                    return move

                edgesOpen = []
                for i in possibleMoves:
                    if i in [2,4,6,8]:
                        edgesOpen.append(i)
            
                if len(edgesOpen) > 0:
                    move = selectRandom(edgesOpen)
        
                return move

            def selectRandom(li):
                
                ln = len(li)
                r = random.randrange(0,ln)
                return li[r]
    

            def isBoardFull(board):
                if board.count(' ') > 1:
                    return False
                else:
                    return True

            def main():
                
                printBoard(board)

                while not(isBoardFull(board)):
                    if not(isWinner(board, 'O')):
                        playerMove()
                        printBoard(board)
                    else:
                        print(Fore.RED + '\n!You lose! \033[0;33mcomputer won\033[0;31m this time!' + Fore.WHITE)
                        getch()
                        imports.own.will_go_to_start.main()

                    if not(isWinner(board, 'X')):
                        move = compMove()
                        if move == 0:
                            print(Fore.YELLOW + '\nTie Game!' + Fore.WHITE)
                            getch()
                            imports.own.will_go_to_start.main()

                        else:
                            insertLetter('O', move)
                            os.system('cls')
                            print('Computer placed an \'\033[0;36mO\033[0;37m\' in position', move , ':')
                            printBoard(board)
                    else:
                        print(Fore.GREEN + '\n\033[0;33m!You win!\033[0;32m in this time! Good Job!' + Fore.WHITE)
                        getch()
                        imports.own.will_go_to_start.main()

                if isBoardFull(board):
                    print(Fore.YELLOW + '\nTie Game!' + Fore.WHITE)
                    getch()
                    imports.own.will_go_to_start.main()

            while True:

                os.system('cls')
                answer = input('Do you want to play Tic_Tac_Toe? (Y/N) ')
                if answer.lower() == 'y' or answer.lower() == 'yes':
                    board = [' ' for x in range(10)]
                    print('----------------------------------------')
                    main()
                else:
                    imports.own.will_go_to_start.main()
