import imports.own.will_go_to_start
import os
from colorama import Fore

def color_back_start():

            try:

                    tokens = imports.own.will_go_to_start.writex.split(" ")
                    name = tokens[1]

                    if name == "g" or name == "G": # Green (+)
                        os.system("color 27")
                        #print("\x1b[32m")

                        imports.own.will_go_to_start.main()

                    elif name == "b" or name == "B": # Blue (+)
                        os.system("color 17")
                        imports.own.will_go_to_start.main()

                    elif name == "r" or name == "R": # Red (+)
                        os.system("color 47")
                        imports.own.will_go_to_start.main()

                    elif name == "y" or name == "Y": # Yellow (+)
                        os.system("color 67")
                        imports.own.will_go_to_start.main()

                    elif name == "bl" or name == "BL": # Black (+)
                        os.system("color 07")
                        imports.own.will_go_to_start.main()

                    elif name == "w" or name == "W": # White (+)
                        os.system("color f7")
                        imports.own.will_go_to_start.main()

                    elif name == "p" or name == "P": # Purple (+)
                        os.system("color 57")
                        imports.own.will_go_to_start.main()

                    elif name == "wb" or name == "WB": # White/Blue (+)
                        os.system("color 37")
                        imports.own.will_go_to_start.main()

                    else:
                        print(Fore.RED + "\n(!ERROR!) " + Fore.WHITE + "=" + Fore.GREEN + " (!Enter color_back option!)" + Fore.WHITE)
                        imports.own.will_go_to_start.main()

            except:
                print(Fore.RED + "\n(!ERROR!) " + Fore.WHITE + "=" + Fore.GREEN + " (!Enter color_back option!)" + Fore.WHITE)
                imports.own.will_go_to_start.main()