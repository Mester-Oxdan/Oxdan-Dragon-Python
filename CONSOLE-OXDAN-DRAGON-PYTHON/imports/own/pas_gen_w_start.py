from msvcrt import getch
import random
import builtins
import time
import imports.own.will_go_to_start
from colorama import Fore

def askPas()->int:

    print(Fore.RED + "Enter 'esc' (for exit)" + Fore.WHITE)

    while True:

        input_str = input(Fore.YELLOW + "Enter number of passwords: " + Fore.WHITE)

        if imports.own.will_go_to_start.remove_098(input_str.lower()) == "esc":

            imports.own.will_go_to_start.main()

        if input_str.isdigit():

            Pas = int(input_str)

        else:

            print(Fore.RED + "\n(!ERROR!) " + Fore.WHITE + "=" + Fore.GREEN + " (!Only integers!)\n" + Fore.WHITE)
            getch()
            continue

        return Pas

def askChar()->int:

    print(Fore.RED + "Enter 'esc' (for exit)" + Fore.WHITE)

    while True:

        input_str45 = input(Fore.YELLOW + "Enter number of chars in passwords: " + Fore.WHITE)

        if imports.own.will_go_to_start.remove_098(input_str45.lower()) == "esc":

            imports.own.will_go_to_start.main()

        if input_str45.isdigit():

            Char = int(input_str45)

        else:

            print(Fore.RED + "\n(!ERROR!) " + Fore.WHITE + "=" + Fore.GREEN + " (!Only integers!)\n" + Fore.WHITE)
            getch()
            continue

        return Char

def pas_gen_w_start():
            
                        print(" ")

                        Char = askChar()

                        saveChar = Char
                        
                        
                        words = ["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "A", "S", "D", "F", "G", "H", "J", "K", "L", "Z", "X", "C", "V", "B", "N", "M", "q", "w", "e", 
                         "r", "t", "y", "u", "i", "o", "p", "a", "s", "d", "f", "g", "h", "j", "k", "l", "z", "x", "c", "v", "b", "n", "m", " "]
                        size = len(words)
                        random.seed(time.time())
                        Pas = size ** Char
                        with builtins.open("Pass_Gen_W.txt", "w") as outFile:
                                for _ in range(Pas):
                                    print(" ")
                                    for _ in range(Char):
                                        outFile.write(words[random.randint(0, size - 1)])
                                        print(words[random.randint(0, size - 1)], end="")
                                    #print(" ")
                                    outFile.write("\n")
                                    if Char == 0:
                                        Char = saveChar
                                        outFile.write("\n")
                        print(" ")
                        imports.own.will_go_to_start.main()