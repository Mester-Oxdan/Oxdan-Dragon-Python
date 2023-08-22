from msvcrt import getch
import random
import os
import imports.own.will_go_to_start
from colorama import Fore

def guess_number_start():

            os.system("cls")
            number=random.randrange(0,100)
            guessCheck="wrong"

            global left, right
            left = 1
            right = 100

            attempts = 0

            print(" ")
            print(Fore.RED + "Write 'esc' (for exit)" + Fore.WHITE)

            while guessCheck=="wrong":

                
                        response = input(Fore.YELLOW + "Enter number (" + Fore.RED + str(left) + Fore.WHITE + " - " + Fore.GREEN + str(right) + Fore.YELLOW + "): " + Fore.WHITE)

                        

                        try:
                            val=int(response)

                        except ValueError:

                            if response.lower() == "esc":
                                imports.own.will_go_to_start.main()

                            else:
                                print(Fore.RED + "\n(!ERROR!) " + Fore.WHITE + "=" + Fore.GREEN + " (!Only integers!)\n" + Fore.WHITE)
                                
                                attempts -= 1

                                continue

                        #val=int (response)
                        
                        attempts += 1

                        if val<number:

                            #global left
                            left = int (response) + 1

                            print("\nMy number: (" + Fore.GREEN + "!Bigger!" + Fore.WHITE + ") \n")

                        elif val>number:

                            #global right
                            right = int (response) - 1

                            print("\nMy number: (" + Fore.RED + "!Lower!" + Fore.WHITE +") \n")

                        else:
                            guessCheck="correct"

            print(" ")
            print("Well you guess my number! (it is " + Fore.YELLOW + repr(number) + Fore.WHITE + ")")
            print("You neded " + Fore.YELLOW + repr(attempts) + Fore.WHITE + " attempts for this \n")

            imports.own.will_go_to_start.main()
