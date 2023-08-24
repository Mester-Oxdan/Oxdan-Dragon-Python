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

def Main_Commands():
    
    if imports.own.will_go_to_start.x.lower() == "--version" or imports.own.will_go_to_start.x == "-version" or imports.own.will_go_to_start.x == "version" or imports.own.will_go_to_start.x == "-v": # --version (+)

        try:

            print("\n" + Fore.YELLOW + " Oxdan" + Fore.RED + " Dragon" + Fore.WHITE + " [ Version: 1.2023 [ENGLISH] (PYTHON) [WINDOWS] ] ")
            time.sleep(0.01)
            print("(c) Oxdan Praduction. ")
            time.sleep(0.01)
            imports.own.will_go_to_start.main()

        except:

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

    elif imports.own.will_go_to_start.x.lower() == "go_to": # go_to (+)
        
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
            
            def update_program_1(username, repo, branch, local_dir):
                try:
                    #remote_commit_hash = get_latest_commit_hash(username, repo, branch)
                    #local_commit_hash = get_current_commit_hash(local_dir)

                    if imports.own.start_start.remote_commit_hash and imports.own.start_start.local_commit_hash and imports.own.start_start.remote_commit_hash != imports.own.start_start.local_commit_hash:
                        #print("A new version is available.")
                        #message = Notification(app_id="OXDAN-DRAGON-PYTHON",
                                               #title="New Update!",
                                               #msg="New update available. After login use 'update' command.",
                                               #duration="short",
                                               #icon=os.path.join(os.environ["OXDAN-DRAGON-PYTHON"],"my_dragon_ico.jpg"))
            
                        #message.set_audio(audio.Default, loop=False)

                        #message.show()
                        shutil.rmtree(local_dir)  # Remove the existing directory
                        git.Repo.clone_from(f"https://github.com/{username}/{repo}.git", local_dir)
                        print("Program updated " + Fore.GREEN + "successfully." + Fore.WHITE + " Please restart the program.")
                        imports.own.will_go_to_start.main()
                        #print("Program updated successfully.")

                    else:
                        print("You have the latest version.")
                        imports.own.will_go_to_start.main()

                except Exception as e:
                    print("Error:", e)
                    msvcrt.getch()
        
            github_username_1 = "Mester-Oxdan"
            repository_name_1 = "Oxdan-Dragon-Python"
            target_branch_1 = "main"  # Update this with the branch you want to update from
            local_directory_1 = os.path.join(os.environ["OXDAN-DRAGON-PYTHON"], "..", "..", "..", "..")  # Update this with your local program directory
    
            update_program_1(github_username_1, repository_name_1, target_branch_1, local_directory_1)

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
            try:

                os.mkdir(test)
                imports.own.will_go_to_start.main()

            except:

                tokens = imports.own.will_go_to_start.writex.split(" ")
                name = tokens[1]
                os.mkdir(name)
                imports.own.will_go_to_start.main()

        except:

            print(Fore.RED + "\n(!ERROR!) " + Fore.WHITE + "=" + Fore.GREEN + " (!Enter name for folder!)" + Fore.WHITE)
            imports.own.will_go_to_start.main()

    elif imports.own.will_go_to_start.x.lower() == "install": # install (+) ?

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

    elif imports.own.will_go_to_start.x.lower() == "del" or imports.own.will_go_to_start.x.lower == "delete": # del (+)
        
        try:

            try:
             
                try:

                    os.rmdir(os.getcwd() + "\\" + name_98)

                except:

                    os.unlink(os.getcwd() + "\\" + name_98)

                imports.own.will_go_to_start.main()

            except:

                tokens = imports.own.will_go_to_start.writex.split(" ")
                name = tokens[1]
             
                try:

                    os.rmdir(os.getcwd() + "\\" + name)

                except:

                    os.unlink(os.getcwd() + "\\" + name)

                imports.own.will_go_to_start.main()

        except:

            print(Fore.RED + "\n(!ERROR!) " + Fore.WHITE + "=" + Fore.GREEN + " (!Enter name for file!)\n" + Fore.WHITE)
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
             
                finp = builtins.open(name, 'w')
                finp.close()
                imports.own.will_go_to_start.main()

        except:

            print(Fore.RED + "\n(!ERROR!) " + Fore.WHITE + "=" + Fore.GREEN + " (!Enter name for file!)" + Fore.WHITE)
            imports.own.will_go_to_start.main()
