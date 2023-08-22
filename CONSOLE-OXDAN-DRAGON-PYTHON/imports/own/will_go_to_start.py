import sys
import os
import imports.own.Commands
import imports.own.Main_Commands
import imports.own.Pictures
import imports.own.Accounts
import imports.own.Hacker_Stuffs
import imports.own.Serious
import imports.own.Games
import imports.own.Own
import imports.own.Pranks
import imports.own.Elses
from colorama import Fore

global which1
which1 = True

global yes_or_no
yes_or_no = True

input_list = []

def main():

    will_start = which1
    
    while True:

        if will_start == True:

            current_dir = os.getcwd()
            global writex
            writex = input("\n" + current_dir + ">> ") # get path (+)
            writex.strip() # remove !spaces!
            tokens = writex.split(" ")
            global x
            x = tokens[0]

            input_list.append(x)

            # big -> class
            # midle -> class
            # small -> class

            imports.own.Serious.Serious() # (+) big
            imports.own.Hacker_Stuffs.Hacker_Stuffs() # (+) big
            imports.own.Games.Games() # (+) big
            imports.own.Elses.Elses() # (+) big
            imports.own.Main_Commands.Main_Commands() # (+) big
            imports.own.Own.Own() # (+) big
            imports.own.Pictures.Pictures() # (+) middle
            imports.own.Accounts.Accounts() # (+) middle
            imports.own.Pranks.Pranks() # (+) middle
            imports.own.Commands.Commands() # (+) small
            
            if x.lower() == "": # nothing (+)

                main()

            else:

                if x.lower() == "stopwatch":

                    break

                print(" ");
                print("'" + x + "'" + " Is " + Fore.RED + "bad" + Fore.WHITE + " command ") # else (+)
                #print(" ")
                main()

        if will_start == False:

            writex = input()
            writex.strip() # remove !spaces!
            tokens = writex.split(" ")
            #global x
            x = tokens[0]

            # big -> class
            # midle -> class
            # small -> class

            imports.own.Serious.Serious() # (+) big
            imports.own.Hacker_Stuffs.Hacker_Stuffs() # (+) big
            imports.own.Games.Games() # (+) big
            imports.own.Elses.Elses() # (+) big
            imports.own.Main_Commands.Main_Commands() # (+) big
            imports.own.Own.Own() # (+) big
            imports.own.Pictures.Pictures() # (+) middle
            imports.own.Accounts.Accounts() # (+) middle
            imports.own.Pranks.Pranks() # (+) middle
            imports.own.Commands.Commands() # (+) small

            if x.lower() == "": # nothing (+)

                main()

            else:

                if x.lower() == "stopwatch":

                    break

                print(" ");
                print("'" + x + "'" + " Is " + Fore.RED + "bad" + Fore.WHITE + " command ") # else (+)
                #print(" ")
                main()

def willgotostart():

    if sys.platform == "linux" or sys.platform == "linux2":
                                        
                                        main()

    elif sys.platform == "win32":
                                                    
                                        main()