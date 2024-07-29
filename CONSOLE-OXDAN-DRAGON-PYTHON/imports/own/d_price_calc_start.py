import os
import imports.own.will_go_to_start
from colorama import Fore

def d_price_calc_start():
    start_the_calc = True

    while start_the_calc:
        print(" ")
        print(Fore.RED + "Enter 'esc' (for exit)" + Fore.WHITE)
        time = input(Fore.YELLOW + "Enter time emount (minutes): " + Fore.WHITE)
        try:
            time_2 = int(time)

        except ValueError:

                            if imports.own.will_go_to_start.remove_098(time.lower()) == "esc":
                                imports.own.will_go_to_start.main()

                            else:
                                print(Fore.RED + "\n(!ERROR!) " + Fore.WHITE + "=" + Fore.GREEN + " (!Only integers!)\n" + Fore.WHITE)

                                continue
        print(" ")
        print(Fore.RED + "Enter 'esc' (for exit)" + Fore.WHITE)
        plastic = input(Fore.YELLOW + "Enter plastic amout (grams): " +Fore.WHITE)
        try:
            plastic_2 = int(plastic)

        except ValueError:

                            if imports.own.will_go_to_start.remove_098(plastic.lower()) == "esc":
                                imports.own.will_go_to_start.main()

                            else:
                                print(Fore.RED + "\n(!ERROR!) " + Fore.WHITE + "=" + Fore.GREEN + " (!Only integers!)\n" + Fore.WHITE)

                                continue
        pla_result = ((time_2 * 0.0007) + (plastic_2 * 0.018)) * 2.5 + 0.5
        petg_result = ((time_2 * 0.0007) + (plastic_2 * 0.015)) * 2.5 + 0.5

        pla_result_rounded = round(pla_result, 3)
        petg_result_rounded = round(petg_result, 3)
        print(" ")
        print(Fore.YELLOW + "PLA: " + Fore.GREEN + "$" + Fore.WHITE + str(pla_result_rounded))
        print(Fore.YELLOW + "PETG: " + Fore.GREEN + "$" + Fore.WHITE + str(petg_result_rounded))
        
        print(" ")
        print(Fore.YELLOW + "Do you want to calculate again? (" + Fore.GREEN + "y" + Fore.WHITE + "/" + Fore.RED + "n" + Fore.YELLOW + ")" + Fore.WHITE)
        choice = input()
        if choice != 'y' or choice != 'yes':
               imports.own.will_go_to_start.main()
               