import msvcrt
import imports.own.will_go_to_start
import builtins
import time
from colorama import Fore
import os
from sys import platform
from imports.own.installs_start import installs_start
import subprocess
import colorama
import requests
import git
import shutil
import imports.own.start_start
import ctypes
import asyncio
import aiohttp

def handle_directory_or_file(path):
    # Check if the path is a directory
    if os.path.isdir(path):
        # List files in the directory
        files = os.listdir(path)
        
        if files:
            # There are files in the directory, ask user for confirmation
            #print(f"The directory '{path}' contains files: {files}")
            print(Fore.RED + "\nEnter 'esc' (for exit)" + Fore.WHITE)
            confirmation = input(Fore.YELLOW + f"Path '{path}' is a Directory. Are you sure you want to delete this directory and its contents? (yes/no): " + Fore.WHITE).strip().lower()
            
            if confirmation.lower() == 'yes' or confirmation.lower() == 'y':
                # Delete the directory and its contents
                shutil.rmtree(path)
                #print(f"The .")
                print(Fore.GREEN + "\n(!SUCCESS!) " + Fore.WHITE + "=" + Fore.YELLOW + f" (!Directory '{path}' has been deleted successfully!)\n" + Fore.WHITE)
            
            elif confirmation.lower() == 'esc':
                
                imports.own.will_go_to_start.main()
                
            else:
                #print("The .")
                print(Fore.RED + "\n(!ERROR!) " + Fore.WHITE + "=" + Fore.GREEN + " (!Directory has not been deleted!)\n" + Fore.WHITE)
        else:
            # Directory is empty
            #print(f"The directory '{path}' is empty.")
            print(Fore.RED + "\nEnter 'esc' (for exit)" + Fore.WHITE)
            confirmation = input(Fore.YELLOW + f"Path '{path}' is a Empty Directory. Do you want to delete this empty directory? (yes/no): " + Fore.WHITE).strip().lower()
            
            if confirmation.lower() == 'yes' or confirmation.lower() == 'y':
                # Delete the empty directory
                os.rmdir(path)
                #print(f"The .")
                print(Fore.GREEN + "\n(!SUCCESS!) " + Fore.WHITE + "=" + Fore.YELLOW + f" (!Empty directory '{path}' has been deleted successfully!)\n" + Fore.WHITE)
            
            elif confirmation.lower() == 'esc':
                
                imports.own.will_go_to_start.main()

            else:
                print("The .")
                print(Fore.RED + "\n(!ERROR!) " + Fore.WHITE + "=" + Fore.GREEN + " (!Empty directory has not been deleted!)\n" + Fore.WHITE)
    
    # If the path is not a directory, check if it's a file
    elif os.path.isfile(path):
        print(Fore.RED + "\nEnter 'esc' (for exit)" + Fore.WHITE)
        confirmation = input(Fore.YELLOW + f"Path '{path}' is a file. Are you sure you want to delete this file? (yes/no): " + Fore.WHITE).strip().lower()
        
        if confirmation == 'yes' or confirmation.lower() == 'y':
            # Delete the file
            os.remove(path)
            #print(f"The .")
            print(Fore.GREEN + "\n(!SUCCESS!) " + Fore.WHITE + "=" + Fore.YELLOW + f" (!File '{path}' has been deleted successfully!)\n" + Fore.WHITE)
        
        elif confirmation.lower() == 'esc':
                
                imports.own.will_go_to_start.main()

        else:
            #print("The ")
            print(Fore.RED + "\n(!ERROR!) " + Fore.WHITE + "=" + Fore.GREEN + " (!File has not been deleted!)\n" + Fore.WHITE)
    
    else:
        # Path does not exist
        #print(f"")
        print(Fore.RED + "\n(!ERROR!) " + Fore.WHITE + "=" + Fore.GREEN + f" (!Path '{path}' does not exist!)\n" + Fore.WHITE)

def get_current_commit_hash(repo_path):
                    repo = git.Repo(repo_path)
                    return repo.head.commit.hexsha

def get_latest_commit_hash(username, repo, branch):
                url = f"https://api.github.com/repos/{username}/{repo}/branches/{branch}"
                response = requests.get(url)
                if response.status_code == 200:
                    return response.json()["commit"]["sha"]
                return None

def update_program(username, repo, branch, local_dir):
                    try:
                        remote_commit_hash = get_latest_commit_hash(username, repo, branch)
                        local_commit_hash = get_current_commit_hash(local_dir)

                        if remote_commit_hash and local_commit_hash and remote_commit_hash != local_commit_hash:
                            #print("A new version is available.")
                        
                            #shutil.rmtree(local_dir)  # Remove the existing directory
                            #git.Repo.clone_from(f"https://github.com/{username}/{repo}.git", local_dir)
                            #print()

                            os.system("git pull")
                            #os.system("start " + os.path.join(os.environ["OXDAN-DRAGON-PYTHON"], "update_python.py"))
                            print(" ")
                            print("Program updated " + Fore.GREEN + "successfully." + Fore.WHITE + " Please restart program.")
                            print("We try to update all files, but if you still have notification about update,")
                            print("Please go on my github, delete your old console, and download new one.")
                            print(" ")
                            #time.sleep(5)
                            #quit(0)
                            #os.system("start " + os.path.join(os.environ["OXDAN-DRAGON-PYTHON"], "../", "../","CONSOLE_OXDAN_DRAGON_PYTHON.py"))
                            
                            imports.own.will_go_to_start.main()

                            #os.system("git pull")
                            #print(" ")
                            #print("Program updated " + Fore.GREEN + "successfully." + Fore.WHITE + " Please restart the program.")
                            #imports.own.will_go_to_start.main()
                            

                            #print("Program updated successfully.")
                        else:
                            #print("You have the latest version.")
                            print(Fore.RED + "\n(!ERROR!) " + Fore.WHITE + "=" + Fore.GREEN + " (!Program already updated to last version!)" + Fore.WHITE)
                            imports.own.will_go_to_start.main()

                    except Exception as e:
                        print("Error:", e)
                        msvcrt.getch()
def Main_Commands():
    
    if imports.own.will_go_to_start.x.lower() == "--version" or imports.own.will_go_to_start.x.lower() == "-version" or imports.own.will_go_to_start.x.lower() == "version" or imports.own.will_go_to_start.x.lower() == "-v": # --version (+)

        try:

            print("\n" + Fore.YELLOW + " Oxdan" + Fore.RED + " Dragon" + Fore.WHITE + " [ Version: 2.2024 [ENGLISH] (PYTHON) [WINDOWS] ] ")
            time.sleep(0.01)
            print("(c) Oxdan Praduction. ")
            time.sleep(0.01)
            imports.own.will_go_to_start.main()

        except:

            imports.own.will_go_to_start.main()
            
    if imports.own.will_go_to_start.writex.lower().startswith("cmd"): # cmd (+)

        try:

                print(" ")
                # Split the input into a list of command-line arguments
                command = imports.own.will_go_to_start.writex.lower().split()
                command.remove("cmd")
                separetor = " "
                right_command = separetor.join(command)
                if right_command == "cmd":
                   
                    print(colorama.Fore.RED + "(!ERROR!) " + colorama.Fore.WHITE + "=" + colorama.Fore.GREEN + " (!We're so sorry about that, only cmd --> cmd command can't be run!)" + colorama.Fore.WHITE)
                    imports.own.will_go_to_start.main()

                else:
                     
                    os.system(right_command)
                    #print(command)
                    # Execute the pip command
                    #result = subprocess.run(right_command, capture_output=True, text=True)

                    # Print the output of the command
                    #print(result.stdout)
                    print(" ")
                    imports.own.will_go_to_start.main()
                    #command.clear()

        except:

           print(colorama.Fore.RED + "(!ERROR!) " + colorama.Fore.WHITE + "=" + colorama.Fore.GREEN + " (!Check your system. (should be windows)!)" + colorama.Fore.WHITE)
           imports.own.will_go_to_start.main()

    if imports.own.will_go_to_start.writex.lower().startswith("pip"): # pip (+)

        try:

                print(" ")
                # Split the input into a list of command-line arguments
                command = imports.own.will_go_to_start.writex.lower().split()

                # Execute the pip command
                result = subprocess.run(command, capture_output=True, text=True)

                # Print the output of the command
                print(result.stdout)
                imports.own.will_go_to_start.main()

        except:

           print(colorama.Fore.RED + "(!ERROR!) " + colorama.Fore.WHITE + "=" + colorama.Fore.GREEN + " (!Install python-3.10.6!)" + colorama.Fore.WHITE)
           imports.own.will_go_to_start.main()

    if imports.own.will_go_to_start.writex.lower().startswith("git"): # git (+)

        try:

                print(" ")
                # Split the input into a list of command-line arguments
                command = imports.own.will_go_to_start.writex.lower().split()

                # Execute the pip command
                result = subprocess.run(command, capture_output=True, text=True)

                # Print the output of the command
                print(result.stdout)
                imports.own.will_go_to_start.main()

        except:

           print(colorama.Fore.RED + "(!ERROR!) " + colorama.Fore.WHITE + "=" + colorama.Fore.GREEN + " (!Install git!)" + colorama.Fore.WHITE)
           imports.own.will_go_to_start.main()

    if imports.own.will_go_to_start.writex.lower().startswith("npm"): # npm (+)

        try:
                
                print(" ")

                command = imports.own.will_go_to_start.writex.lower()

                # Execute the command using os.system() and capture the output
                result = os.system(command + " 2>&1")

                # Print the output of the command
                print(result)
                imports.own.will_go_to_start.main()

        except:

           print(colorama.Fore.RED + "(!ERROR!) " + colorama.Fore.WHITE + "=" + colorama.Fore.GREEN + " (!Install npm!)" + colorama.Fore.WHITE)
           imports.own.will_go_to_start.main()

    if imports.own.will_go_to_start.writex.lower().startswith("conda"): # conda (+)

        try:

                print(" ")

                try:
                    output = subprocess.check_output(["conda", "run", "-n", "base", "-c", "conda-forge", imports.own.will_go_to_start.writex.lower()], stderr=subprocess.STDOUT, shell=True)
                    print(output.decode())
                except subprocess.CalledProcessError as e:
                    print(e.output.decode())

                imports.own.will_go_to_start.main()

        except:

           print(colorama.Fore.RED + "(!ERROR!) " + colorama.Fore.WHITE + "=" + colorama.Fore.GREEN + " (!Install miniconda!)" + colorama.Fore.WHITE)
           imports.own.will_go_to_start.main()

    elif imports.own.will_go_to_start.x.lower() == "cls" or imports.own.will_go_to_start.x.lower() == "clear": # cls (+)
        
        try:

            if platform == "linux" or platform == "linux2":

                # linux
                os.system("clear")

            elif platform == "win32":

                # Windows...
                os.system("cls")

            else:
                os.system("cls")

            imports.own.will_go_to_start.main()

        except:

            imports.own.will_go_to_start.main()

    elif imports.own.will_go_to_start.x.lower() == "go_to" or imports.own.will_go_to_start.x.lower() == "cd": # go_to (+)
        
        try:

            try:

                #tokens = will_go_to_start.writex.split(" ")
                #cd = tokens[1]

                os.chdir(cd)

                imports.own.will_go_to_start.main()

            except:

                tokens = imports.own.will_go_to_start.writex.split(" ")
                cd_45 = tokens[1]

                os.chdir(cd_45)

                imports.own.will_go_to_start.main()

        except:

            print(Fore.RED + "\n(!ERROR!) " + Fore.WHITE + "=" + Fore.GREEN + " (!Enter path to directory!)\n" + Fore.WHITE)
            imports.own.will_go_to_start.main()

    elif imports.own.will_go_to_start.x.lower() == "update": # update (+)
        
        try:

            async def fetch_data():
                async with aiohttp.ClientSession() as session:
                    url = "http://raw.githubusercontent.com/Mester-Oxdan/Oxdan-Dragon-Python/main/version"
                    async with session.get(url) as response:
                        return await response.text()

            async def main():
                response = await fetch_data()
                #print (response)
                if response != "2.2024\n":
                    print(" ")
                    print("\033[0;33mYou're right!\033[0;37m")
                    print("We have a new version for you: 3.2025")
                    print("If you want to \033[0;32mdownload\033[0;37m it, just go to our Website or GitHub.")
                    imports.own.will_go_to_start.main()
                else:
                    print(Fore.RED + "\n(!ERROR!) " + Fore.WHITE + "=" + Fore.GREEN + " (!Program already updated to last version!)" + Fore.WHITE)
                    imports.own.will_go_to_start.main()

            asyncio.run(main())

        except:

            print(Fore.RED + "\n(!ERROR!) " + Fore.WHITE + "=" + Fore.GREEN + " (!Program already updated to last version!)" + Fore.WHITE)
            imports.own.will_go_to_start.main()
            
    elif imports.own.will_go_to_start.x.lower() == "dir" or imports.own.will_go_to_start.x.lower() == "ls": # dir (+)
            
        print(" ")

        try:

            print(Fore.YELLOW + "FILES: \n")
            entries = os.listdir(str(os.getcwd()))

            for entry in entries:
                print(Fore.WHITE + entry)

            imports.own.will_go_to_start.main()

        except:

            imports.own.will_go_to_start.main()

    elif imports.own.will_go_to_start.x.lower() == "mkdir": # mkdir (+)
        
        try:

                tokens = imports.own.will_go_to_start.writex.split(" ")
                name = tokens[1]
                if not os.path.exists(name):
                    os.mkdir(name)
                    #print(f".")
                    print(Fore.GREEN + "\n(!SUCCESS!) " + Fore.WHITE + "=" + Fore.YELLOW + " (!Directory created successfully!)" + Fore.WHITE)
                else:
                    #print(f".")
                    print(Fore.RED + "\n(!ERROR!) " + Fore.WHITE + "=" + Fore.GREEN + " (!Directory with that name already exists!)" + Fore.WHITE)
                    
                imports.own.will_go_to_start.main()

        except:

            print(Fore.RED + "\n(!ERROR!) " + Fore.WHITE + "=" + Fore.GREEN + " (!Enter name for folder!)" + Fore.WHITE)
            imports.own.will_go_to_start.main()

    elif imports.own.will_go_to_start.x.lower() == "install": # install (+)

        try:

            try:
            
                installs_start(name_578)
                imports.own.will_go_to_start.main()

            except:

                tokens = imports.own.will_go_to_start.writex.split(" ")
                name = tokens[1]
            
                installs_start(name)
            
                imports.own.will_go_to_start.main()

        except:

            print(Fore.RED + "\n(!ERROR!) " + Fore.WHITE + "=" + Fore.GREEN + " (!Enter install option!)\n" + Fore.WHITE)
            imports.own.will_go_to_start.main()

    if imports.own.will_go_to_start.x.lower() == "del" or imports.own.will_go_to_start.x.lower == "delete": # del (+)
        
        try:


                tokens = imports.own.will_go_to_start.writex.split(" ")
                name = tokens[1]
             
                """try:

                    os.rmdir(os.getcwd() + "\\" + name)

                except:

                    os.unlink(os.getcwd() + "\\" + name)
                """
                path = os.getcwd() + "\\" + name
                handle_directory_or_file(path)

                imports.own.will_go_to_start.main()

        except:

            print(Fore.RED + "\n(!ERROR!) " + Fore.WHITE + "=" + Fore.GREEN + " (!Enter name for file or directory!)\n" + Fore.WHITE)
            imports.own.will_go_to_start.main()
            
    if imports.own.will_go_to_start.writex.lower().startswith("search"): # search (+)

        try:

                print(" ")
                # Split the input into a list of command-line arguments
                command_09 = imports.own.will_go_to_start.writex.lower().split()
                command_09.remove("search")
                separetor = " "
                right_command_09 = separetor.join(command_09)
                     
                #os.system(right_command)
                #print(command)
                # Execute the pip command
                #result = subprocess.run(right_command, capture_output=True, text=True)
                command_list = [
        "search", "--help", "-help", "help", "-h", "--version", "-version", "version", "-v", "pip", "git", "conda",
        "cmd", "cls", "clear", "go_to", "dir", "ls", "mkdir", "create", "del", "delete", "install", "update",
        "injector_dll", "pas_gen", "my_wifi_pas", "cor_desk", "ascii_code", "ip_search", "phone_search", "mimikatz",
        "john", "nmap", "con_wifi", "wifi_hack", "stealer", "get_ip_website", "auto_clicker", "morse_code_cipher",
        "caesar_cipher", "ai_chat", "ukraine", "author", "matrix", "login", "registration", "instructions",
        "del_account", "logout", "tim", "time", "stopwatch", "timer", "calculator", "calendar", "webcam_recorder",
        "screen_recorder", "cur_conv", "notepad", "translator", "dictaphone", "chat_client", "chat_server", "pacman",
        "2048", "arkanoid", "flappy_bird", "tetris", "hangman", "car_racing", "guess_number", "math_game",
        "typing_tutor", "battle_city", "doom", "mario", "snake", "ping_pong", "tic_tac_toe", "checkers", "chess",
        "space_shooter", "title", "new", "start", "open", "shutdown", "restart", "data", "promo_code", "i_am_here",
        "&main", "donate", "donators", "helpers", "color_back", "i?", "administrator", "admin", "superuser",
        "chan_backg", "send_ph_message", "history", "cls_history", "memory", "rules", "commands", "tips", "links",
        "my_volume_level", "set_volume_level", "set_mute", "ip", "size", "my_location", "system_info",
        "energy", "power", "prank_button", "melt_screen", "gdi_virus", "exit", "esc", "quit"
    ] #dragon_helper, color, 

                # Take user input
                #user_input = input("Enter a fruit name: ")

                # Check if the input exists in the list
                if right_command_09 in command_list:
                        print(colorama.Fore.GREEN + "(!SUCCESS!) " + colorama.Fore.WHITE + "=" + colorama.Fore.YELLOW + " (!This command exists!)" + colorama.Fore.WHITE)
                else:
                        print(colorama.Fore.RED + "(!ERROR!) " + colorama.Fore.WHITE + "=" + colorama.Fore.GREEN + " (!This command doesn't exists!)" + colorama.Fore.WHITE)
                # Print the output of the command
                #print(result.stdout)
                print(" ")
                imports.own.will_go_to_start.main()
                #command.clear()

        except:

           print(colorama.Fore.RED + "(!ERROR!) " + colorama.Fore.WHITE + "=" + colorama.Fore.GREEN + " (!This command doesn't exists!)" + colorama.Fore.WHITE)
           imports.own.will_go_to_start.main()

    elif imports.own.will_go_to_start.x.lower() == "create": # create (+)
        
        try:

            try:

                #tokens = will_go_to_start.writex.split(" ")
                #name = tokens[1]
             
                finp = builtins.open(name_56, 'w')
                finp.close()
                imports.own.will_go_to_start.main()

            except:

                tokens = imports.own.will_go_to_start.writex.split(" ")
                name = tokens[1]
             
                if not os.path.exists(name):
                    finp = builtins.open(name, 'w')
                    finp.close()
                    #print(f".")
                    print(Fore.GREEN + "\n(!SUCCESS!) " + Fore.WHITE + "=" + Fore.YELLOW + " (!File created successfully!)" + Fore.WHITE)
                else:
                    #print(f".")
                    print(Fore.RED + "\n(!ERROR!) " + Fore.WHITE + "=" + Fore.GREEN + " (!File with that name already exists!)" + Fore.WHITE)
                  

                imports.own.will_go_to_start.main()

        except:

            print(Fore.RED + "\n(!ERROR!) " + Fore.WHITE + "=" + Fore.GREEN + " (!Enter name for file!)" + Fore.WHITE)
            imports.own.will_go_to_start.main()
