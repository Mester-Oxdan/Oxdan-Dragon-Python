from time import sleep
from colorama import Fore
import imports.own.will_go_to_start

def Commands():
    
    if imports.own.will_go_to_start.x.lower() == "--help" or imports.own.will_go_to_start.x.lower() == "-help" or imports.own.will_go_to_start.x.lower() == "help" or imports.own.will_go_to_start.x.lower() == "-h": # --help (+)

            print(Fore.RED + "\n" + "COMMANDS:") # !MAIN COMMANDS!
            sleep(0.01)
            print(" ")
            sleep(0.01)
            print(Fore.YELLOW + "MAINS:") # class MAINS: (+)
            sleep(0.01)
            print(" ")
            sleep(0.01)
            print(Fore.WHITE + "search - check if entered command exists " + Fore.YELLOW + "( " + Fore.WHITE + "command" + Fore.YELLOW + " )" + Fore.WHITE) # search (+)
            sleep(0.01)
            print("--help " + Fore.CYAN + "or " + Fore.WHITE + "-help " + Fore.CYAN + "or " + Fore.WHITE + "help " + Fore.CYAN + "or " + Fore.WHITE + "-h " + " - shows all commands ") # --help (+)
            sleep(0.01)
            print("--version " + Fore.CYAN + "or " + Fore.WHITE + "-version " + Fore.CYAN + "or " + Fore.WHITE + "version " + Fore.CYAN + "or " + Fore.WHITE + "-v" + " - shows version ") # --version (+)
            sleep(0.01)
            print("pip - using entered pip commands " + Fore.YELLOW + "(" + Fore.WHITE + " command " + Fore.YELLOW + ")" + Fore.WHITE) # pip (+)
            sleep(0.01)
            print("git - using entered git commands " + Fore.YELLOW + "(" + Fore.WHITE + " command " + Fore.YELLOW + ")" + Fore.WHITE) # git (+)
            sleep(0.01)
            print("conda - using entered conda commands " + Fore.YELLOW + "(" + Fore.WHITE + " command " + Fore.YELLOW + ")" + Fore.WHITE) # conda (+)
            sleep(0.01)
            print("cmd - using entered cmd commands " + Fore.YELLOW + "(" + Fore.WHITE + " command " + Fore.YELLOW + ")" + Fore.WHITE) # cmd (+)
            sleep(0.01)
            print("cls " + Fore.CYAN + "or " + Fore.WHITE + "clear" + " - clear your screen ") # cls (+)
            sleep(0.01)
            print("go_to - go to entered directory " + Fore.YELLOW + "( " + Fore.WHITE + "path" + Fore.YELLOW + " )" + Fore.WHITE) # go_to (+)
            sleep(0.01)
            print("dir " + Fore.CYAN + "or " + Fore.WHITE + "ls" + " - shows all files of current directory ") # dir (+)
            sleep(0.01)
            print("mkdir - create new folder with entered name " + Fore.YELLOW + "( " + Fore.WHITE + "folder name" + Fore.YELLOW + " )" + Fore.WHITE) # mkdir (+)
            sleep(0.01)
            print("create - create new file with entered name.type " + Fore.YELLOW + "( " + Fore.WHITE + "name.type" + Fore.YELLOW + " )" + Fore.WHITE) # create (+)
            sleep(0.01)
            print("del " + Fore.CYAN + "or " + Fore.WHITE + "delete" + " - delete entered file " + Fore.YELLOW + "( " + Fore.WHITE + "file name" + Fore.YELLOW + " )" + Fore.WHITE) # del (+)
            sleep(0.01)
            print("install - install entered option " + Fore.YELLOW + "(" + Fore.WHITE + " python-3.10.6, nmap-7.94-setup, git, miniconda3 " + Fore.YELLOW + ")" + Fore.WHITE) # install (+)
            sleep(0.01)
            print("update - update Dragon console to last version") # update (+)
            sleep(0.01)
            print(" ")
            sleep(0.01)
            print(Fore.YELLOW + "HACKER STUFFS:") # class HACKER STUFFS: (+)
            sleep(0.01)
            print(" ")
            print(Fore.WHITE + "injector_dll - shows dll injector") # inject_dll (+)
            sleep(0.01)
            print("pas_gen - shows password generator " + Fore.YELLOW + "(" + Fore.WHITE + " w, u, n, nw " + Fore.YELLOW + ")" + Fore.WHITE) # pas_gen (+)
            sleep(0.01)
            print("my_wifi_pas - shows list passwords of yours wifi") # my_wifi_pas (+)
            sleep(0.01)
            print("cor_desk - shows Desktop coordinates") # cor_desk (+)
            sleep(0.01)
            print("ascii_code - shows ascii code of each pressed key") # ascii_code (+)
            sleep(0.01)
            print("ip_search - searching location by entered network ip address " + Fore.YELLOW + "(" + Fore.WHITE + " ip addreess " + Fore.YELLOW + ")" + Fore.WHITE + " (for location on google maps use (https://www.maps.ie/coordinates.html))") # ip_search (+)
            sleep(0.01)
            print("phone_search - searching location by entered phone number " + Fore.YELLOW + "(" + Fore.WHITE + " phone number " + Fore.YELLOW + ")" + Fore.WHITE + " (for location on google maps use (https://www.maps.ie/coordinates.html))") # phone_search (+)
            sleep(0.01)
            print("mimikatz - using entered mimikatz commands " + Fore.YELLOW + "(" + Fore.WHITE + " command " + Fore.YELLOW + ")" + Fore.WHITE) # mimikatz (+)
            sleep(0.01)
            print("john - using entered john the ripper commands " + Fore.YELLOW + "(" + Fore.WHITE + " command " + Fore.YELLOW + ")" + Fore.WHITE) # john (+)
            sleep(0.01)
            print("nmap - using entered nmap commands " + Fore.YELLOW + "(" + Fore.WHITE + " command " + Fore.YELLOW + ")" + Fore.WHITE) # nmap (+)
            sleep(0.01)
            print("con_wifi - doing connection to entered wifi network " + Fore.YELLOW + "(" + Fore.WHITE + " wifi network name " + Fore.YELLOW + ")" + Fore.WHITE) # con_wifi (+)
            sleep(0.01)
            print("wifi_hack - shows tool for brute force wifi network") # wifi_hack (+)
            sleep(0.01)
            print("stealer - coping importent files windows in target_files_dis folder") # stealer (+)
            sleep(0.01)
            print("get_ip_website - shows ip address entered site " + Fore.YELLOW + "( " + Fore.WHITE + "website name" + Fore.YELLOW + " )" + Fore.WHITE) # get_ip_website (+)
            sleep(0.01)
            print("auto_clicker - auto clicking, for exit press 'Esc'") # auto_clicker (+)
            sleep(0.01)
            print("morse_code_cipher - shows morse code cipher") # morse_code (+)
            sleep(0.01)
            print("caesar_cipher - shows caesar cipher") # caesar_cipher (+)
            sleep(0.01)
            print("ai_chat - shows ai chat") # ai_chat (+)
            sleep(0.01)
            print(" ")
            sleep(0.01)
            print(Fore.YELLOW + "PICTURES:") # class PICTURES: (+)
            sleep(0.01)
            print(" ")
            sleep(0.01)
            print(Fore.WHITE + "ukraine - shows Ukraine flag") # ukraine (+)
            sleep(0.01)
            print("author - shows author of this console") # author (+)
            sleep(0.01)
            print("matrix - shows hacker matrix") # matrix (+)
            sleep(0.01)
            print(" ")
            sleep(0.01)
            print(Fore.YELLOW + "ACCOUNTS:") # class ACCOUNTS: (+)
            sleep(0.01)
            print(" ")
            sleep(0.01)
            print(Fore.WHITE + "login - go to login page") # login (+)
            sleep(0.01)
            print("registration - go to registration page") # registration (+)
            sleep(0.01)
            print("instructions - go to instructions page") # instructions (+)
            sleep(0.01)
            print("del_account - delete entered account " + Fore.YELLOW + "( " + Fore.WHITE + "account name" + Fore.YELLOW + " )" + Fore.WHITE) # del_account (+)
            sleep(0.01)
            print("logout - go to main menu") # logout (+)
            sleep(0.01)
            print(" ")
            sleep(0.01)
            print(Fore.YELLOW + "SERIOUS:") # class SERIOUS: (+)
            sleep(0.01)
            print(" ")
            sleep(0.01)
            print(Fore.WHITE + "tim " + Fore.CYAN + "or " + Fore.WHITE + "time" + " - shows ryal time ") # tim (+)
            sleep(0.01)
            print("stopwatch - shows stopwatch") # stopwatch (+)
            sleep(0.01)
            print("timer - shows timer") # timer (+)
            sleep(0.01)
            print("calculator - shows calculator") # calculator (+)
            sleep(0.01)
            print("calendar - shows calendar") # calendar (+)
            sleep(0.01)
            print("webcam_recorder - shows webcam video recorder (without recording voice (you can use dictaphone for recording voice))") # webcam_recorder (+)
            sleep(0.01)
            print("screen_recorder - shows screen video recorder (without recording voice (you can use dictaphone for recording voice))") # screen_recorder (+) need add to c/c++
            sleep(0.01)
            print("cur_conv - shows currency converter") # cur_conv (+)
            sleep(0.01)
            print("notepad - shows notepad") # notepad (+)
            sleep(0.01)
            print("translator - shows languages translator") # translator (+)
            sleep(0.01)
            print("dictaphone - shows dictaphone") # dictaphone (+)
            sleep(0.01)
            print("chat_client - host to the chat server") # chat_client (+)
            sleep(0.01)
            print("chat_server - creates chat server") # chat_server (+)
            sleep(0.01)
            print(" ")
            sleep(0.01)
            print(Fore.YELLOW + "GAMES:") # class GAMES: (+)
            sleep(0.01)
            print(" ")
            sleep(0.01)
            print(Fore.WHITE + "pacman - shows pacman") # pacman (+)
            sleep(0.01)
            print("2048 - shows 2048") # 2048 (+)
            sleep(0.01)
            print("arkanoid - shows arkanoid") # arkanoid (+)
            sleep(0.01)
            print("flappy_bird - shows flappy bird") # flappy_bird (+)
            sleep(0.01)
            print("tetris - shows tetris") # tetris (+)
            sleep(0.01)
            print("hangman - shows hangman") # hangman (+)
            sleep(0.01)
            print("car_racing - shows car racing game") # car_racing (+)
            sleep(0.01)
            print("guess_number - shows game guess my number") # guess_number (+)
            sleep(0.01)
            print("math_game - shows math game") # math_game (+)
            sleep(0.01)
            print("typing_tutor - shows typing tutor") # typing_tutor (+)
            sleep(0.01)
            print("battle_city - shows battle city") # battle_city (+)
            sleep(0.01)
            print("doom - shows doom") # doom (+)
            sleep(0.01)
            print("mario - shows mario") # mario (+)
            sleep(0.01)
            print("snake - shows snake game " + Fore.YELLOW + "(" + Fore.WHITE + " 1, 2, ai " + Fore.YELLOW + ")" + Fore.WHITE) # snake (+)
            sleep(0.01)
            print("ping_pong - shows ping pong " + Fore.YELLOW + "(" + Fore.WHITE + " 1, 2, ai " + Fore.YELLOW + ")" + Fore.WHITE) # ping_pong (+)
            sleep(0.01)
            print("tic_tac_toe - shows tic-tac-toe " + Fore.YELLOW + "(" + Fore.WHITE + " 2, ai " + Fore.YELLOW + ")" + Fore.WHITE) # tic_tac_toe (+)
            sleep(0.01)
            print("checkers - shows checkers " + Fore.YELLOW + "(" + Fore.WHITE + " 2, ai " + Fore.YELLOW + ")" + Fore.WHITE) # checkers (+)
            sleep(0.01)
            print("chess - shows chess " + Fore.YELLOW + "(" + Fore.WHITE + " 2, ai " + Fore.YELLOW + ")" + Fore.WHITE) # chess (+)
            sleep(0.01)
            print("space_shooter - shows space shooter ") # space shooter (+)
            sleep(0.01)
            print(" ")
            sleep(0.01)
            print(Fore.YELLOW + "OWNS:") # class OWNS: (+)
            sleep(0.01)
            print(" ")
            sleep(0.01)
            print(Fore.WHITE + "title - set input title " + Fore.YELLOW + "( " + Fore.WHITE + "title name" + Fore.YELLOW + " )" + Fore.WHITE) # title (+)
            sleep(0.01)
            print("new " + Fore.CYAN + "or " + Fore.WHITE + "start" + " - opens one more Dragon console ") # new (+)
            sleep(0.01)
            print("open - open entered file " + Fore.YELLOW + "( " + Fore.WHITE + "path" + Fore.YELLOW + " )" + Fore.WHITE) # open (+)
            sleep(0.01)
            print("shutdown - shutdown your laptop") # shutdown (+) 
            sleep(0.01)
            print("restart - restart your laptop") # restart (+)
            sleep(0.01)
            print("data - shows real time data") # data (+)
            sleep(0.01)
            print("promo_code - using input promo code " + Fore.YELLOW + "( " + Fore.WHITE + "promo code name" + Fore.YELLOW + " )" + Fore.WHITE) # title (+)
            sleep(0.01)
            print("i_am_here - shows how much time did you spent here") # i_am_here (+)
            sleep(0.01)
            print("&main - turn main " + Fore.YELLOW + "(" + Fore.WHITE + " on, off " + Fore.YELLOW + ")" + Fore.WHITE) # &main (+)
            sleep(0.01)
            print("donate - donate specified amount of money for author") # donate (+)
            sleep(0.01)
            print("donators - shows list of top 15 donators for author (updating with new version)") # donators (+)
            sleep(0.01)
            print("helpers - shows list of top 15 helpers for author (updating with new version)") # helpers (+)
            sleep(0.01)

            color = Fore.WHITE + " color"
            koma = Fore.WHITE + ","
            g = Fore.GREEN + " g"
            b = Fore.BLUE + " b"
            r = Fore.RED + " r"
            y = Fore.YELLOW + " y"
            bl = Fore.WHITE + " bl"
            w = Fore.WHITE + " w"
            p = Fore.MAGENTA + " p"
            wb = Fore.CYAN + " wb "

            print("color - set color text " + Fore.YELLOW + "(" + Fore.WHITE + color + koma + g + koma + b + koma + r + koma + y + koma + bl + koma + w + koma + p + koma + wb + Fore.YELLOW + ")" + Fore.WHITE) # color (+)
            sleep(0.01)
            print("color_back - set background color for console " + Fore.YELLOW + "(" + Fore.WHITE + color + koma + g + koma + b + koma + r + koma + y + koma + bl + koma + w + koma + p + koma + wb + Fore.YELLOW + ")" + Fore.WHITE) # color_back (+)
            sleep(0.01)
            print("i? - shows you are admin or user") # i? (+)
            sleep(0.01)
            print("administrator " + Fore.CYAN + "or " + Fore.WHITE + "admin " + Fore.CYAN + "or " + Fore.WHITE + "superuser" + " - open Dragon console as administrator") # administrator (+)
            sleep(0.01)
            print("chan_backg - set desktop background with entered path to photo " + Fore.YELLOW + "( " + Fore.WHITE + "path" + Fore.YELLOW + " )" + Fore.WHITE) # chan_backg (+)
            sleep(0.01)
            print("send_ph_message - send message on entered phone number") # send_ph_message (+)
            sleep(0.01)
            print("history - shows all entered commands") # history (+)
            sleep(0.01)
            print("cls_history - clear all entered commands") # cls_history (+)
            sleep(0.01)
            print("memory - shows memory of your disk") # memory (+)
            sleep(0.01)
            print("rules - shows rules of this console") # rules (+)
            sleep(0.01)
            print("commands - shows commands only") # commands (+)
            sleep(0.01)
            print("tips - shows tips only") # tips (+)
            sleep(0.01)
            print("links - shows links only") # links (+)
            sleep(0.01)
            print("dragon_helper - will enter commands that you said, while you did't say 'exit'") # dargon_helper (+) need add to c/c++
            sleep(0.01)
            print("my_volume_level - shows windows volume level") # my_volume_level (+)
            sleep(0.01)
            print("set_volume_level - set windows volume level " + Fore.YELLOW + "( " + Fore.WHITE + "number" + Fore.YELLOW + " )" + Fore.WHITE) # set_volume_level (+)
            sleep(0.01)
            print("set_mute - set windows mute " + Fore.YELLOW + "(" + Fore.WHITE + " on, off " + Fore.YELLOW + ")" + Fore.WHITE) # set_mute (+)
            sleep(0.01)
            print("ip - shows your ip address") # ip (+)
            sleep(0.01)
            print("size - set console size with entered parameters " + Fore.YELLOW + "( " + Fore.WHITE + "x, y" + Fore.YELLOW + " )" + Fore.WHITE) # size (+)
            sleep(0.01)
            print("my_location - shows your location") # my_location (+)
            sleep(0.01)
            print("system_info - shows info about computer") # system_info (+)
            sleep(0.01)
            print("energy " + Fore.CYAN + "or " + Fore.WHITE + "power" + " - shows energy of computer " ) # energy (+)
            sleep(0.01)
            print(" ")
            sleep(0.01)
            print(Fore.YELLOW + "PRANKS:") # class PRANKS: (+)
            sleep(0.01)
            print(" ")
            sleep(0.01)
            print(Fore.WHITE + "prank_button - shows prank with run away button " + Fore.YELLOW + "(" + Fore.WHITE + " yes, no " + Fore.YELLOW + ")" + Fore.WHITE) # prank_button (+)
            sleep(0.01)
            print("melt_screen - shows melting screen, for exit from process click on console, press 'Esc'") # melt_screen (+)
            sleep(0.01)
            print("gdi_virus - shows gdi virus, for exit press 'Esc'") # gdi_virus (+)
            sleep(0.01)
            print(" ")
            sleep(0.01)
            print(Fore.YELLOW + "ELSES:") # class ELSES: (+)
            sleep(0.01)
            print(" ")
            sleep(0.01)
            print(Fore.WHITE + "exit " + Fore.CYAN + "or " + Fore.WHITE + "esc " + Fore.CYAN + "or " + Fore.WHITE + "quit" + " - exit from here ") # exit (+)
            sleep(0.01)
            print(" ")
            sleep(0.01)
            print(Fore.RED + "TIPS:") # class !MAIN TIPS! (+)
            sleep(0.01)
            print(" ")
            sleep(0.01)
            print(Fore.WHITE + "1) in " + Fore.YELLOW + "(" + Fore.WHITE + " " + Fore.YELLOW + ")" + Fore.WHITE + " shows options") # 1) tip (+)
            sleep(0.01)
            print("2) best size for console is " + Fore.YELLOW + "141" + Fore.WHITE + ", " + Fore.YELLOW + "29" + Fore.WHITE) # 2) tip (+)
            sleep(0.01)
            print("3) ") # 3) tip (+)
            sleep(0.01)
            print(" ")
            print(Fore.RED + "LINKS:") # class !MAIN LINKS! (+)
            sleep(0.01)
            print(" ")
            sleep(0.01)
            print(Fore.WHITE + "1) OXDAN Website (https://oxdan.com)") # 1) link DRAGON (+)
            sleep(0.01)
            print("2) Chess.com (https://www.chess.com/home)") # 2) link chess.com (+)
            sleep(0.01)
            print("3) Google Maps Locator (https://www.maps.ie/coordinates.html)") # 3) google maps locator (+)
            sleep(0.01)
            print("4) Github (https://github.com/Mester-Oxdan)") # 4) Github (+)
            sleep(0.01)
            print("5) Youtube (https://www.youtube.com/@Oxdan_Praduction)") # 5) Youtube (+)
            sleep(0.01)
            print("6) TikTok (https://www.tiktok.com/@oxdan_praduction)") # 6) TikTok (+)
            sleep(0.01)
            print("7) Instagram (https://instagram.com/oxdanpraduction)") # 7) Instagram (+)
            sleep(0.01)
            print("8) Kwork (https://kwork.com/user/jecob)") # 8) Kwork (+)
            sleep(0.01)
            print("9) Fiverr (https://www.fiverr.com/jecob_567)") # 9) Fiverr (+)
            sleep(0.01)
            print("10) Upwork (https://www.upwork.com/freelancers/~01e296384cd379e73e?viewMode=1&mp_source=share)") # 10) Upwork (+)
            sleep(0.01)
            print("11) Reddit (https://www.reddit.com/u/detektive-void/s/JyYykvbe9o)") # 11) Reddit (+)
            sleep(0.01)
            print("12) For Sponsoring/Donations: Cash App ($BoHladii /OR/ 4403 9352 3234 1307)") # 12) Sponsoring/Donations Cash App (+)
            sleep(0.01)
            print("13) Buy Me A Coffee (https://www.buymeacoffee.com/oxdan)") # 13) Buy Me A Coffee (+)
            sleep(0.01)
            print("14) For Shops: Etsy (https://oxdanpraduction3dart.etsy.com)") # 14) Etsy (+)
            sleep(0.01)
            print("15) ") # 15)  (+)
            sleep(0.01)
            imports.own.will_go_to_start.main()
