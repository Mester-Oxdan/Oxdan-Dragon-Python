from msvcrt import getch
import random
import builtins
import time
import imports.own.will_go_to_start
from colorama import Fore

def askPas()->int:

    print(Fore.RED + "Write 'esc' (for exit)" + Fore.WHITE)

    while(True):
        input_str = input(Fore.YELLOW + "Enter number of passwords: " + Fore.WHITE)

        if input_str.lower() == "esc":
            print(" ")
            imports.own.will_go_to_start.main()

        if( input_str.isdigit() ):

            Pas = int(input_str)

        else:

            print(Fore.RED + "\n(!ERROR!) " + Fore.WHITE + "=" + Fore.GREEN + " (!Only integers!)\n" + Fore.WHITE)
            getch()
            continue

        return Pas

def askChar()->int:

   while True:

        input_str45 = input(Fore.YELLOW + "Enter number of chars in passwords: " + Fore.WHITE)

        if input_str45.lower() == "esc":
            print(" ")
            imports.own.will_go_to_start.main()

        if( input_str45.isdigit() ):

            Char = int(input_str45)

        else:

            print(Fore.RED + "\n(!ERROR!) " + Fore.WHITE + "=" + Fore.GREEN + " (!Only integers!)\n" + Fore.WHITE)
            getch()
            continue

        return Char

def pas_gen_n_start():

    while True:

                                    print(" ")

                                    Pas = askPas()

                                    print(" ")

                                    Char = askChar()

                                    saveChar = Char
    
                                    words = ['1','2','3','4','5','6','7','8','9','0']
                                    size = len(words)
                                    random.seed(time.time())

                                    with builtins.open("Pass_Gen_N.txt", "w") as outFile:

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
