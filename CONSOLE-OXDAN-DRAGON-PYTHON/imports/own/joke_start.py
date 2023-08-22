import imports.own.will_go_to_start
from colorama import Fore
from imports.own.joke_all_start import joke_all_start
from imports.own.joke_ph_start import joke_ph_start
from imports.own.joke_v_start import joke_v_start
from imports.own.joke_au_start import joke_au_start

def joke_start():

    try:

        try:

            joke_all_start(a_tit_2789)
            joke_ph_start(a_tit_2789)
            joke_v_start(a_tit_2789)
            joke_au_start(a_tit_2789)

        except:

            tokens = imports.own.will_go_to_start.writex.split(" ")
            name = tokens[1]

            joke_all_start(name)
            joke_ph_start(name)
            joke_v_start(name)
            joke_au_start(name)

    except:

        print(Fore.RED + "\n(!ERROR!) " + Fore.WHITE + "=" + Fore.GREEN + " (!Enter joke option!)\n" + Fore.WHITE)
        imports.own.will_go_to_start.main() 