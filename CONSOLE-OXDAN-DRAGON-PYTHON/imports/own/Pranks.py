import imports.own.will_go_to_start
from colorama import Fore
from imports.own.prank_button import prank_button_yes
from imports.own.prank_button import prank_button_no
from imports.own.prank_melt_screen_start import prank_melt_screen_start
from imports.own.gdi_virus_start import gdi_virus_start

def Pranks():

    if imports.own.will_go_to_start.x.lower() == "prank_button": # prank_button (+)

                try:

                    try:

                        if zxd_5 == "no":

                            prank_button_no()

                        if zxd_5 == "yes":

                            prank_button_yes()

                        imports.own.will_go_to_start.main()

                    except:

                        tokens_prank_button = imports.own.will_go_to_start.writex.split(" ")
                        global a_prank_button
                        a_prank_button = tokens_prank_button[1]

                        if a_prank_button == "no":

                            prank_button_no()

                        if a_prank_button == "yes":

                            prank_button_yes()

                        imports.own.will_go_to_start.main()

                except:

                    print(Fore.RED + "\n(!ERROR!) " + Fore.WHITE + "=" + Fore.GREEN + " (!Enter prank_button option!)" + Fore.WHITE + "\n")
                    imports.own.will_go_to_start.main()

    elif imports.own.will_go_to_start.x.lower() == "melt_screen": # melt_screen (+)

        try:

            prank_melt_screen_start()

        except:

            imports.own.will_go_to_start.main()

    elif imports.own.will_go_to_start.x.lower() == "gdi_virus": # gdi_virus (+)

        try:

            gdi_virus_start()

        except:

            imports.own.will_go_to_start.main()
