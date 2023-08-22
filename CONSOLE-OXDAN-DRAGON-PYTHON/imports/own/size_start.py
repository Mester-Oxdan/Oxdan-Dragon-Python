import os
import imports.own.will_go_to_start
from colorama import Fore

def size_start():

        try:

            try:
            
                os.system("mode " + a_tit_bg + "," + a_tit_bg_2)

                imports.own.will_go_to_start.main()

            except:

                tokens = imports.own.will_go_to_start.writex.split(" ")
                a = tokens[1]
                b = tokens[2]
            
                os.system("mode " + a + "," + b)

                imports.own.will_go_to_start.main()

        except:
            print(Fore.RED + "\n(!ERROR!) " + Fore.WHITE + "=" + Fore.GREEN + " (!Enter 2 parameters! (without ','))\n" + Fore.WHITE)
            imports.own.will_go_to_start.main()