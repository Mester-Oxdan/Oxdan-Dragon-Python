from msvcrt import getch
import imports.own.will_go_to_start
import os
import random
from colorama import Fore

def hangman_start():

        os.system("cls")
        # constants
        HANGMAN = (
            """
         ------
         |    |
         |
         |
         |
         |
         |
         |
         |
        ----------
        """,
        """
         ------
         |    |
         |    \033[0;33mO\033[0m
         |
         |
         |
         |
         |
         |
        ----------
        """,
        """
         ------
         |    |
         |    \033[0;33mO\033[0;37m
         |   \033[0;33m-+-\033[0;37m
         | 
         |   
         |   
         |   
         |   
        ----------
        """,
        """
         ------
         |    |
         |    \033[0;33mO\033[0;37m
         |  \033[0;33m/-+-\033[0;37m
         |   
         |   
         |   
         |   
         |   
        ----------
        """,
        """
         ------
         |    |
         |    \033[0;33mO\033[0;37m
         |  \033[0;33m/-+-/\033[0;37m
         |   
         |   
         |   
         |   
         |   
        ----------
        """,
        """
         ------
         |    |
         |    \033[0;33mO\033[0;37m
         |  \033[0;33m/-+-/\033[0;37m
         |    \033[0;33m|\033[0;37m
         |   
         |   
         |   
         |   
        ----------
        """,
        """
         ------
         |    |
         |    \033[0;33mO\033[0;37m
         |  \033[0;33m/-+-/\033[0;37m
         |    \033[0;33m|\033[0;37m
         |    \033[0;33m|\033[0;37m
         |   \033[0;33m|\033[0;37m 
         |   \033[0;33m|\033[0;37m 
         |   
        ----------
        """,
        """
         ------
         |    |
         |    \033[0;33mO\033[0;37m
         |  \033[0;33m/-+-/\033[0;37m
         |    \033[0;33m|\033[0;37m
         |    \033[0;33m|\033[0;37m
         |   \033[0;33m| |\033[0;37m
         |   \033[0;33m| |\033[0;37m
         |  
        ----------
        """)

        # constant no. 2

        MAX_WRONG = len(HANGMAN) - 1

        # constant no. 3

        WORDS = ("THE GRIND", "HANGMAN", "WHEEL OF FORTUNE",
                 "AEROPOSTALE", "PYTHON", "CASABLANCA",
                 "ALASKA", "SILLY GOOSE", "OVERUSED", "OXDAN", 
                 "PRADUCTION")

        # initialise variables

        word = random.choice(WORDS) # the word to be guessed

        so_far = "-" * len(word) # one dash for each letter in word to be guessed

        wrong = 0 # counter to keep track of number of wrong guesses

        used = [] # list to keep track of letters already guessed

        os.system('cls')

        while wrong < MAX_WRONG and so_far != word:
            print (HANGMAN[wrong])
            print ("\nYou used following letters:\n", used)
            print(Fore.RED + "\nWrite 'esc' (for exit)")
            print ("\033[0;33mYou have guessed:\033[0;37m\t", so_far)

            guess = input()
            if guess == "esc":

                imports.own.will_go_to_start.main()

            if guess.isalpha():
                guess = guess.upper()
                #used.remove(guess)
                if guess in used:

                    #os.system('cls')
                    print ("\nYou already guessed this letter:\t", guess)
  
                    used.remove(str(guess))
                    #wrong -= 1
                    getch()

                used.append(guess)

                if guess in word:
                    os.system('cls')
                    print (Fore.GREEN + "!Letter " + "[" + guess + "]" + " was in word!" + Fore.WHITE)

                    # create a new so_far to include guess
                    new = ""


                    for i in range(len(word)):
                        if guess == word [i]:
                            new += guess
                        else:
                            new += so_far [i]
                    so_far = new

                else:
                    os.system('cls')
                    print (Fore.RED + "!Letter " + "[" + guess + "]" + " was not in word!" + Fore.WHITE)
                    used.remove(str(guess))
                    if guess not in used:
                        wrong += 1
                    else:
                        continue

            else:

                print("\nEnter only letters")
                getch()

            #used.append(guess)

        if wrong == MAX_WRONG:
            os.system('cls')

        else:
            os.system('cls')
            print(Fore.YELLOW + "Word is: " + Fore.WHITE + word )
            print(Fore.GREEN + "\n!You guessed it!" + Fore.WHITE)
            getch()
            imports.own.will_go_to_start.main()
        print(Fore.YELLOW + "\nWord was: " + Fore.WHITE + word )
        print(Fore.RED + "\n!You did not guessed it!" + Fore.WHITE)
        getch()
        imports.own.will_go_to_start.main()
