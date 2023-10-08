import imports.own.will_go_to_start
import pymem
from colorama import Fore
from concurrent.futures import process

def inject_prog_start():

            print(Fore.RED + "\nWrite 'esc' (for exit)" + Fore.WHITE)
            dll_path = input(Fore.YELLOW + "Enter DLL PATH: " + Fore.WHITE)
            dll_path_bytes = bytes(dll_path, "UTF-8")

            if dll_path == "esc":

                imports.own.will_go_to_start.main()

            print(" ")
            process_name = input(Fore.YELLOW + "Enter Process Name: " + Fore.WHITE)

            if process_name == "esc":

                imports.own.will_go_to_start.main()

            open_process = pymem.Pymem(process_name)
            process.inject_dll(open_process.process_hendle, dll_path_bytes)

            print(" ")
            print(Fore.GREEN + "!DLL INJECT SUCCESSFUL!" + Fore.WHITE)

            imports.own.will_go_to_start.main()