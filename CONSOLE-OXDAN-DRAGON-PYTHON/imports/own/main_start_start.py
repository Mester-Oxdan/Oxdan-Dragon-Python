import imports.own.will_go_to_start
from colorama import Fore

def main_start_start():

        try:

                tokens = imports.own.will_go_to_start.writex.split(" ")
                man = tokens[1]
            
                if man == "off":

                    global which1
                    imports.own.will_go_to_start.which1 = False

                elif man == "on":

                    global which1
                    imports.own.will_go_to_start.which1 = True

                else:
                    print(Fore.RED + "\n(!ERROR!) " + Fore.WHITE + "=" + Fore.GREEN + " (!Enter &main option)\n" + Fore.WHITE)
                    imports.own.will_go_to_start.main()

                imports.own.will_go_to_start.main()

        except:

            print(Fore.RED + "\n(!ERROR!) " + Fore.WHITE + "=" + Fore.GREEN + " (!Enter &main option)\n" + Fore.WHITE)
            imports.own.will_go_to_start.main()