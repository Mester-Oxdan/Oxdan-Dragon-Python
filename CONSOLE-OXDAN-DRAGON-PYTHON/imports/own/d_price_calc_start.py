import os
import imports.own.will_go_to_start
from colorama import Fore

def d_price_calc_start():
    start_the_calc = True

    while start_the_calc:
        print(" ")
        print(Fore.RED + "Enter 'esc' (for exit)" + Fore.WHITE)
        time = input(Fore.YELLOW + "Enter time amount ($0.0007/minute): " + Fore.WHITE)
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
        plastic = input(Fore.YELLOW + "Enter plastic amount (grams): " +Fore.WHITE)
        try:
            plastic_2 = int(plastic)

        except ValueError:

                            if imports.own.will_go_to_start.remove_098(plastic.lower()) == "esc":
                                imports.own.will_go_to_start.main()

                            else:
                                print(Fore.RED + "\n(!ERROR!) " + Fore.WHITE + "=" + Fore.GREEN + " (!Only integers!)\n" + Fore.WHITE)

                                continue
                         
        print(" ")
        print(Fore.RED + "Enter 'esc' (for exit)" + Fore.WHITE)
        magnits = input(Fore.YELLOW + "Enter magnits amount (pcs): " +Fore.WHITE)
        try:
            magnits_2 = int(magnits)

        except ValueError:

                            if imports.own.will_go_to_start.remove_098(magnits.lower()) == "esc":
                                imports.own.will_go_to_start.main()

                            else:
                                print(Fore.RED + "\n(!ERROR!) " + Fore.WHITE + "=" + Fore.GREEN + " (!Only integers!)\n" + Fore.WHITE)

                                continue

        if magnits_2 != 0:
            print(" ")
            print(Fore.RED + "Enter 'esc' (for exit)" + Fore.WHITE)
            magnits_size = input(Fore.YELLOW + "Enter magnits size 1, 2, 3, 4 (1 - 10x2mm, 2 - 8x2mm, 3 - 6x2mm, 4 - 5x2mm): " + Fore.WHITE)
            try:
                magnits_size_2 = int(magnits_size)
                if magnits_size_2 == 1:
                       magnits_coast = 0.13 * magnits_2
                if magnits_size_2 == 2:
                       magnits_coast = 0.08 * magnits_2
                if magnits_size_2 == 3:
                       magnits_coast = 0.06 * magnits_2
                if magnits_size_2 == 4:
                       magnits_coast = 0.07 * magnits_2
            except ValueError:

                                if imports.own.will_go_to_start.remove_098(magnits_size.lower()) == "esc":
                                    imports.own.will_go_to_start.main()

                                else:
                                    print(Fore.RED + "\n(!ERROR!) " + Fore.WHITE + "=" + Fore.GREEN + " (!Only integers!)\n" + Fore.WHITE)

                                    continue
        print(" ")
        print(Fore.RED + "Enter 'esc' (for exit)" + Fore.WHITE)
        ring = input(Fore.YELLOW + "Enter rings amount ($0.1/pcs): " + Fore.WHITE)
        try:
            ring_2 = int(ring)

        except ValueError:

                            if imports.own.will_go_to_start.remove_098(ring.lower()) == "esc":
                                imports.own.will_go_to_start.main()

                            else:
                                print(Fore.RED + "\n(!ERROR!) " + Fore.WHITE + "=" + Fore.GREEN + " (!Only integers!)\n" + Fore.WHITE)

                                continue
        if magnits_2 != 0:
            magnits_coast_2 = magnits_coast
        else:
            magnits_coast_2 = 0;   
        pla_result = ((time_2 * 0.0007) + (plastic_2 * 0.018) + magnits_coast_2 + (ring_2 * 0.1)) * 2.5 + 0.5
        petg_result = ((time_2 * 0.0007) + (plastic_2 * 0.015)+ magnits_coast_2 + (ring_2 * 0.1)) * 2.5 + 0.5

        pla_result_rounded = round(pla_result, 3)
        petg_result_rounded = round(petg_result, 3)
        print(" ")
        print(Fore.YELLOW + "PLA Model: " + Fore.GREEN + "$" + Fore.WHITE + str(pla_result_rounded))
        print(Fore.YELLOW + "PETG Model: " + Fore.GREEN + "$" + Fore.WHITE + str(petg_result_rounded))
        
        print(" ")
        print(Fore.YELLOW + "Do you want to calculate again? (" + Fore.GREEN + "y" + Fore.WHITE + "/" + Fore.RED + "n" + Fore.YELLOW + ")" + Fore.WHITE)
        choice = input()
        if choice != 'y' or choice != 'yes':
               imports.own.will_go_to_start.main()
        else:
               d_price_calc_start()