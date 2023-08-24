import msvcrt
import os
import colorama
import keyboard
import imports.own.login
import imports.own.signup
import imports.own.instructions
import ctypes
import time
import git
import requests
import shutil
import time
from winotify import Notification, audio

start_time = time.time()

files_dir = os.path.dirname(__file__)
os.environ["OXDAN-DRAGON-PYTHON"] = files_dir 

#path_to_png = os.path.join(os.environ["OXDAN-DRAGON-PYTHON"],"..","IMAGES","ALL","icon.png")

def get_latest_commit_hash(username, repo, branch):
    url = f"https://api.github.com/repos/{username}/{repo}/branches/{branch}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()["commit"]["sha"]
    return None

def get_current_commit_hash(repo_path):
    repo = git.Repo(repo_path)
    return repo.head.commit.hexsha

def update_program(username, repo, branch, local_dir):
    try:
        remote_commit_hash = get_latest_commit_hash(username, repo, branch)
        local_commit_hash = get_current_commit_hash(local_dir)

        if remote_commit_hash and local_commit_hash and remote_commit_hash != local_commit_hash:
            #print("A new version is available.")
            message = Notification(app_id="OXDAN-DRAGON-PYTHON",
                                   title="New Update!",
                                   msg="New update available. After login use 'update' command.",
                                   duration="short",
                                   icon=os.path.join(os.environ["OXDAN-DRAGON-PYTHON"],"my_dragon_ico.jpg"))
            
            message.set_audio(audio.Default, loop=False)

            message.show()
            #shutil.rmtree(local_dir)  # Remove the existing directory
            #git.Repo.clone_from(f"https://github.com/{username}/{repo}.git", local_dir)
            
            #print("Program updated successfully.")
        #else:
            #print("You have the latest version.")

    except Exception as e:
        print("Error:", e)
        msvcrt.getch()
        
github_username = "Mester-Oxdan"
repository_name = "Oxdan-Dragon-Python"
target_branch = "main"  # Update this with the branch you want to update from
local_directory = "../"  # Update this with your local program directory
    
update_program(github_username, repository_name, target_branch, local_directory)

def printMenu(items, active_index):

    print(" ")
    print("                                                              ")
    print("                                                              ")
    print("                                                              ")
    print("                                                              ")
    print("                                                              ")
    print("                                                              ")
    print("                                                              ")
    print("                                                              ")
    print("                                                              ")
    #print("                                                              ")
    for index, item in enumerate(items):
        if index == active_index:
            #print(f'\033[31;47m{item}\033[0m')

            print(colorama.Fore.RED + f'{item}' + colorama.Fore.YELLOW)
        else:
            print(item)

def start_start():

    print(colorama.Fore.YELLOW)
    os.system("cls")

    Menu = ["                                                              REGISTRATION", "                                                              LOGIN", "                                                              INSTRUCTIONS", "                                                              EXIT"]
    active_menu = 0
    keyboard.press(72)

    while True:

        key = ord(msvcrt.getch())

        if key == 27:
            
            exit(0)

        elif key == 72:

            if active_menu > 0:
                active_menu -= 1
            os.system("cls")
            
                
            #break

        elif key == 80:

            if active_menu < 3:
                active_menu += 1
            os.system("cls")

            #break

        elif key == 13:

            if active_menu == 0:

                os.system("cls")
                imports.own.signup.signup()

            if active_menu == 1:

                os.system("cls")
                imports.own.login.login()

            if active_menu == 2: ############

                os.system("cls")
                imports.own.instructions.instructions()

            if active_menu == 3:

                #os.system("cls")
                exit(0)

        elif key == 49: # 1

                os.system("cls")
                imports.own.signup.signup()

        elif key == 50:

                os.system("cls")
                imports.own.login.login()

        elif key == 51:

                os.system("cls")
                imports.own.instructions.instructions()

        elif key == 52:

                os.system("cls")
                exit(0)
            
        else:

            continue

        printMenu(Menu, active_menu)
