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
                            print("Program updated " + Fore.GREEN + "successfully." + Fore.WHITE + " Please restart program.")
                            #time.sleep(5)
                            #quit(0)
                            #os.system("start " + os.path.join(os.environ["OXDAN-DRAGON-PYTHON"], "../", "../","CONSOLE_OXDAN_DRAGON_PYTHON.py"))
                            
                            imports.own.will_go_to_start.main()

                            os.system("git pull")
                            print(" ")
                            print("Program updated " + Fore.GREEN + "successfully." + Fore.WHITE + " Please restart the program.")
                            imports.own.will_go_to_start.main()
                            

                            #print("Program updated successfully.")
                        else:
                            #print("You have the latest version.")
                            print(Fore.RED + "\n(!ERROR!) " + Fore.WHITE + "=" + Fore.GREEN + " (!Program already updated to last version!)" + Fore.WHITE)
                            imports.own.will_go_to_start.main()

                    except Exception as e:
                        print("Error:", e)
                        msvcrt.getch()
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
            try:
                is_admin = os.getuid() == 0
            except AttributeError:
                is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0

            if is_admin == True:
                
                
        
                github_username = "Mester-Oxdan"
                repository_name = "Oxdan-Dragon-Python"
                target_branch = "main"  # Update this with the branch you want to update from
                local_directory = "../"  # Update this with your local program directory
    
                update_program(github_username, repository_name, target_branch, local_directory)
            
            elif is_admin == False:
                print(" ")
                print("To update program you should be " + Fore.RED + "admin.")
                time.sleep(0.01)
                print(Fore.YELLOW + "Hint:" + Fore.WHITE + " to run console as admin you can use 'admin' command")
                time.sleep(0.01)
                print("then you can check your self who you are by 'i?' command.")
                imports.own.will_go_to_start.main()
            
            

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
