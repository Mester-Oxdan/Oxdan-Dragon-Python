from msvcrt import getch
import will_go_to_start
import builtins
import random
import time
from colorama import Fore

def askPas()->int:

    while True:

        input_str = input(Fore.YELLOW + "Number of passwords: " + Fore.WHITE)

        if input_str.isdigit():

            Pas = int(input_str)

        else:

            print(Fore.RED + "\n(!ERROR!) " + Fore.WHITE + "=" + Fore.GREEN + " (!Only integers!)\n" + Fore.WHITE)
            getch()
            continue

        return Pas

def askChar()->int:

    while True:

        input_str45 = input(Fore.YELLOW + "Number of chars in passwords: " + Fore.WHITE)

        if input_str45.isdigit():

            Char = int(input_str45)

        else:

            print(Fore.RED + "\n(!ERROR!) " + Fore.WHITE + "=" + Fore.GREEN + " (!Only integers!)\n" + Fore.WHITE)
            getch()
            continue

        return Char

def pas_gen_nw_start():
                            print(" ")

                            Pas = askPas()

                            print(" ")

                            Char = askChar()

                            saveChar = Char
    
                            words = ['Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M','q','w','e',
                             'r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m','1','2','3','4','5','6',
                             '7','8','9','0',' ']
                            size = len(words)
                            random.seed(time.time())

                            with builtins.open("Pass_Gen_U.txt", "w") as outFile:
                                    for _ in range(Pas):
                                        print("\n")
                                        for _ in range(Char):
                                            outFile.write(words[random.randint(0, size - 1)])
                                            print(words[random.randint(0, size - 1)], end="")
                                        print("\n")
                                        outFile.write("\n")
                                        if Char == 0:
                                            Char = saveChar
                                            outFile.write("\n")
                                            print("\n")
                            will_go_to_start.main()