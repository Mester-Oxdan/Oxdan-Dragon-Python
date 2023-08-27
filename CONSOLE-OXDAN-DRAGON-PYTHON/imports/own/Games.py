import imports.own.will_go_to_start
from colorama import Fore
from imports.own.space_shooter_start import space_shooter_start
from imports.own.tetris_start import tetris_start
from imports.own.checkers_2_start import checkers_2_start
from imports.own.checkers_ai_start import checkers_ai_start
from imports.own.chess_2_start import chess_2_start
from imports.own.chess_ai_start import chess_ai_start
from imports.own.pacman_start import pacman_start
from imports.own.tic_tac_toe_2_start import tic_tac_toe_2_start
from imports.own.tic_tac_toe_ai_start import tic_tac_toe_ai_start
from imports.own.ping_pong_1_start import ping_pong_1_start
from imports.own.snake_ai_start import snake_ai_start
from imports.own.t2048_start import start_2048
from imports.own.hangman_start import hangman_start
from imports.own.arkanoid_start import arkanoid_start
from imports.own.snake_1_start import snake_1_start
from imports.own.snake_2_start import snake_2_start
from imports.own.flappybird_start import flappybird_start
from imports.own.ping_pong_2_start import ping_pong_2_start
from imports.own.guess_number_start import guess_number_start
from imports.own.ping_pong_ai_start import ping_pong_ai_start
from imports.own.car_racing_start import car_racing_start
from imports.own.battle_city import battle_city
from imports.own.typing_tutor_start import typing_tutor_start
from imports.own.doom_start import doom_start
from imports.own.math_game_start import math_game_start
import pygame

def Games():

    if imports.own.will_go_to_start.x.lower() == "pacman": # pacman (+)

        try:

            pacman_start()

        except:

            imports.own.will_go_to_start.main()

    elif imports.own.will_go_to_start.x.lower() == "car_racing": # car_racing (+)

        try:

            car_racing_start()

        except:

            imports.own.will_go_to_start.main()

    elif imports.own.will_go_to_start.x.lower() == "tic_tac_toe": # tic_tac_toe (+)

        try:

            if zxd_8 == "2" or zxd_8 == "two":

                try:

                    tic_tac_toe_2_start()
                    imports.own.will_go_to_start.main()
                except:

                    imports.own.will_go_to_start.main()

            elif zxd_8 == "ai":

                try:
                    tic_tac_toe_ai_start()
                    imports.own.will_go_to_start.main()
                except:

                    imports.own.will_go_to_start.main()

            else:

                print(Fore.RED + "\n(!ERROR!) " + Fore.WHITE + "=" + Fore.GREEN + " (!Enter tic_tac_toe option!)" + Fore.WHITE)
                imports.own.will_go_to_start.main()

        except:

            tokens = imports.own.will_go_to_start.writex.split(" ")
            take654 = tokens[1]

            if take654 == "2" or take654 == "two":

                try:

                    tic_tac_toe_2_start()

                except:

                    imports.own.will_go_to_start.main()

            elif take654 == "ai":

                try:
                    tic_tac_toe_ai_start()

                except:

                    imports.own.will_go_to_start.main()

            else:

                print(Fore.RED + "\n(!ERROR!) " + Fore.WHITE + "=" + Fore.GREEN + " (!Enter tic_tac_toe option!)\n" + Fore.WHITE)
                imports.own.will_go_to_start.main()

    elif imports.own.will_go_to_start.x.lower() == "checkers": # checkers (+)

        try:

            if zxd_9 == "2" or zxd_9 == "two": # (+)

                try:
              
                    checkers_2_start()

                except:

                    imports.own.will_go_to_start.main()

            if zxd_9 == "ai": # (+)
                

                try:
              
                    checkers_ai_start()

                except:

                    imports.own.will_go_to_start.main()

            else:

                print(Fore.RED + "\n(!ERROR!) " + Fore.WHITE + "=" + Fore.GREEN + " (!Enter checkers option!)\n" + Fore.WHITE)
                imports.own.will_go_to_start.main()

        except:

            tokens = imports.own.will_go_to_start.writex.split(" ")
            take = tokens[1]

            if take == "2" or take == "two": # (+)

                try:
              
                    checkers_2_start()

                except:

                    imports.own.will_go_to_start.main()

            if take == "ai": # (+)
                

                try:
              
                    checkers_ai_start()

                except:

                    imports.own.will_go_to_start.main()

            else:

                print(Fore.RED + "\n(!ERROR!) " + Fore.WHITE + "=" + Fore.GREEN + " (!Enter checkers option!)\n" + Fore.WHITE)
                imports.own.will_go_to_start.main()

    elif imports.own.will_go_to_start.x.lower() == "chess": # chess (+)

        try:

            if zxd_10 == "2" or zxd_10 == "two": # (+)

                try:
              
                    chess_2_start()

                except:

                    pygame.quit()
                    imports.own.will_go_to_start.main()

            if zxd_10 == "ai": # (+)

                try:
              
                    chess_ai_start()

                except:

                    pygame.quit()
                    imports.own.will_go_to_start.main()

            else:

                print(Fore.RED + "\n(!ERROR!) " + Fore.WHITE + "=" + Fore.GREEN + " (!Enter chess option!)\n" + Fore.WHITE)
                imports.own.will_go_to_start.main()

        except:

            tokens = imports.own.will_go_to_start.writex.split(" ")
            take = tokens[1]

            if take == "2" or take == "two": # (+)

                try:
              
                    chess_2_start()

                except:

                    pygame.quit()
                    imports.own.will_go_to_start.main()

            if take == "ai": # (+)

                try:
              
                    chess_ai_start()

                except:

                    pygame.quit()
                    imports.own.will_go_to_start.main()

            else:

                print(Fore.RED + "\n(!ERROR!) " + Fore.WHITE + "=" + Fore.GREEN + " (!Enter chess option!)\n" + Fore.WHITE)
                imports.own.will_go_to_start.main()

    elif imports.own.will_go_to_start.x.lower() == "mario":

        try:

            import pygame as pg
            from imports.mario.source.main import main
            #from source.main import main

            main()
            pg.quit()
            imports.own.will_go_to_start.main()

        except:

            pg.quit()
            imports.own.will_go_to_start.main()

    elif imports.own.will_go_to_start.x.lower() == "battle_city": # battle_city (+)
                
            try:
                
                #print(Fore.RED + "\nPress Esc (for exit)" + Fore.WHITE)
                #print("\n")
                battle_city()

            except:

                imports.own.will_go_to_start.main()

    elif imports.own.will_go_to_start.x.lower() == "doom": # doom (+)
                
            #try:
                
                doom_start()

            #except:

                #pygame.quit()
                #imports.own.will_go_to_start.main()

    elif imports.own.will_go_to_start.x.lower() == "ping_pong": # ping_pong (+)

        try:

            if zxd_7 == "1" or zxd_7 == "one": # (-)

                try:
              
                    ping_pong_1_start()

                except:

                    imports.own.will_go_to_start.main()

            if zxd_7 == "2" or zxd_7 == "two": # (+)
                    
                try:
              
                    ping_pong_2_start()

                except:

                    imports.own.will_go_to_start.main()

            if zxd_7 == "ai": # (+)

                try:
              
                    ping_pong_ai_start()

                except:

                    imports.own.will_go_to_start.main()

            else:
            
                print(Fore.RED + "\n(!ERROR!) " + Fore.WHITE + "=" + Fore.GREEN + " (!Enter ping_pong option!)\n" + Fore.WHITE)
                imports.own.will_go_to_start.main()

        except:

            tokens = imports.own.will_go_to_start.writex.split(" ")
            take = tokens[1]

            if take == "1" or take == "one": # (-)

                try:
              
                    ping_pong_1_start()

                except:

                    imports.own.will_go_to_start.main()

            if take == "2" or take == "two": # (+)
                    
                try:
              
                    ping_pong_2_start()

                except:

                    imports.own.will_go_to_start.main()

            if take == "ai": # (+)

                try:
              
                    ping_pong_ai_start()

                except:

                    imports.own.will_go_to_start.main()

            else:
            
                print(Fore.RED + "\n(!ERROR!) " + Fore.WHITE + "=" + Fore.GREEN + " (!Enter ping_pong option!)\n" + Fore.WHITE)
                imports.own.will_go_to_start.main()

    elif imports.own.will_go_to_start.x.lower() == "flappy_bird": # flappy_bird (+)

        try:

            flappybird_start()

        except:

            imports.own.will_go_to_start.main()

    elif imports.own.will_go_to_start.x.lower() == "2048": # 2048 (+)

        try:

            start_2048()

        except:

            imports.own.will_go_to_start.main()

    elif imports.own.will_go_to_start.x.lower() == "tetris": # tetris (+)

        try:

            tetris_start()

        except:

            imports.own.will_go_to_start.main()

    elif imports.own.will_go_to_start.x.lower() == "space_shooter": # space_shooter (+)

        try:

            space_shooter_start()

        except:

            imports.own.will_go_to_start.main()

    elif imports.own.will_go_to_start.x.lower() == "snake": # snake (+)

        try:

            if zxd_6 == "ai":
            
                try:

                    snake_ai_start()

                except:

                    imports.own.will_go_to_start.main()

            if zxd_6 == "1" or zxd_6 == "one":

                try:

                    snake_1_start()

                except:

                    imports.own.will_go_to_start.main()

            if zxd_6 == "2" or zxd_6 == "two":
            
                try:

                    snake_2_start()

                except:

                    imports.own.will_go_to_start.main()

            else:
            
                print(Fore.RED + "\n(!ERROR!) " + Fore.WHITE + "=" + Fore.GREEN + " (!Enter snake option!)\n" + Fore.WHITE)
                imports.own.will_go_to_start.main()

        except:

            tokens = imports.own.will_go_to_start.writex.split(" ")
            take23 = tokens[1]

            if take23 == "ai":
            
                try:

                    snake_ai_start()

                except:

                    imports.own.will_go_to_start.main()

            if take23 == "1" or take23 == "one":

                try:

                    snake_1_start()

                except:

                    imports.own.will_go_to_start.main()

            if take23 == "2" or take23 == "two":
            
                try:

                    snake_2_start()

                except:

                    imports.own.will_go_to_start.main()

            else:
            
                print(Fore.RED + "\n(!ERROR!) " + Fore.WHITE + "=" + Fore.GREEN + " (!Enter snake option!)\n" + Fore.WHITE)
                imports.own.will_go_to_start.main()

    elif imports.own.will_go_to_start.x.lower() == "guess_number": # guess_number (+)
            
        try:

            guess_number_start()

        except:

            imports.own.will_go_to_start.main()

    elif imports.own.will_go_to_start.x.lower() == "math_game": # math_game (+)
            
        try:

            math_game_start()

        except:

            imports.own.will_go_to_start.main()

    elif imports.own.will_go_to_start.x.lower() == "typing_tutor": # typing_tutor (+)
            
        try:

            typing_tutor_start()

        except:

            imports.own.will_go_to_start.main()

    elif imports.own.will_go_to_start.x.lower() == "hangman": # hangman (+)

        try:

            hangman_start()

        except:

            imports.own.will_go_to_start.main()

    elif imports.own.will_go_to_start.x.lower() == "arkanoid": # arkanoid (+)
            
        try:

            arkanoid_start()

        except:

            imports.own.will_go_to_start.main()
            