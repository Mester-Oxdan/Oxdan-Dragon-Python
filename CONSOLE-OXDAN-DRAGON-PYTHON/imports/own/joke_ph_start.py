import os
import random
from colorama import Fore
import imports.own.will_go_to_start

def joke_ph_start(name):

    try:
        if name == "ph" or name == "PH" or name == "Ph":

            random_file_ph = random.choice(os.listdir("memes\\(+)Photo"))
            os.system("start memes\\(+)Photo\\" + random_file_ph)
            imports.own.will_go_to_start.main()

    except:

        print(Fore.RED + "\n(!ERROR!) " + Fore.WHITE + "=" + Fore.GREEN + " (!Enter joke option!)\n" + Fore.WHITE)
        imports.own.will_go_to_start.main()
