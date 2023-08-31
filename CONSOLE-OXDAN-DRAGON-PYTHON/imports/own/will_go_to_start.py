import sys
import os
import imports.own.Commands
import imports.own.Main_Commands
import imports.own.Pictures
import imports.own.Accounts
import imports.own.Hacker_Stuffs
import imports.own.Serious
import imports.own.Games
import imports.own.Own
import imports.own.Pranks
import imports.own.Elses
from colorama import Fore
from winotify import Notification, audio
import requests, git, msvcrt

global which1
which1 = True

global yes_or_no
yes_or_no = True

input_list = []

def get_latest_commit_hash(username, repo, branch):
    url = f"https://api.github.com/repos/{username}/{repo}/branches/{branch}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()["commit"]["sha"]
    return None

def get_current_commit_hash(repo_path):
    repo = git.Repo(repo_path)
    return repo.head.commit.hexsha

#print(os.path.join(os.environ["OXDAN-DRAGON-PYTHON"],r"my_dragon_ico_transformed.png"))
#msvcrt.getch()

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
                                   icon=os.path.join(os.environ["OXDAN-DRAGON-PYTHON"],r"my_dragon_ico_transformed.png"))
                                   #icon=r"C:\Users\bogda\Downloads\Oxdan-Dragon-Python\CONSOLE-OXDAN-DRAGON-PYTHON\imports\own\my_dragon_ico_transformed.png")
                                   
            
            message.set_audio(audio.Default, loop=False)
            message.add_actions(label="Go to Website.", launch="https://github.com/Mester-Oxdan/Oxdan-Dragon-Python")

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

def main():

    will_start = which1
    
    while True:

        if will_start == True:

            current_dir = os.getcwd()
            global writex
            writex = input("\n" + current_dir + ">> ") # get path (+)
            writex.strip() # remove !spaces!
            tokens = writex.split(" ")
            global x
            x = tokens[0]

            input_list.append(x)

            # big -> class
            # midle -> class
            # small -> class

            imports.own.Serious.Serious() # (+) big
            imports.own.Hacker_Stuffs.Hacker_Stuffs() # (+) big
            imports.own.Games.Games() # (+) big
            imports.own.Elses.Elses() # (+) big
            imports.own.Main_Commands.Main_Commands() # (+) big
            imports.own.Own.Own() # (+) big
            imports.own.Pictures.Pictures() # (+) middle
            imports.own.Accounts.Accounts() # (+) middle
            imports.own.Pranks.Pranks() # (+) middle
            imports.own.Commands.Commands() # (+) small
            
            if x.lower() == "": # nothing (+)

                main()

            else:

                if x.lower() == "stopwatch":

                    break

                print(" ");
                print("'" + x + "'" + " Is " + Fore.RED + "bad" + Fore.WHITE + " command ") # else (+)
                #print(" ")
                main()

        if will_start == False:

            writex = input()
            writex.strip() # remove !spaces!
            tokens = writex.split(" ")
            #global x
            x = tokens[0]

            # big -> class
            # midle -> class
            # small -> class

            imports.own.Serious.Serious() # (+) big
            imports.own.Hacker_Stuffs.Hacker_Stuffs() # (+) big
            imports.own.Games.Games() # (+) big
            imports.own.Elses.Elses() # (+) big
            imports.own.Main_Commands.Main_Commands() # (+) big
            imports.own.Own.Own() # (+) big
            imports.own.Pictures.Pictures() # (+) middle
            imports.own.Accounts.Accounts() # (+) middle
            imports.own.Pranks.Pranks() # (+) middle
            imports.own.Commands.Commands() # (+) small

            if x.lower() == "": # nothing (+)

                main()

            else:

                if x.lower() == "stopwatch":

                    break

                print(" ");
                print("'" + x + "'" + " Is " + Fore.RED + "bad" + Fore.WHITE + " command ") # else (+)
                #print(" ")
                main()

def willgotostart():

    if sys.platform == "linux" or sys.platform == "linux2":
                                        
                                        main()

    elif sys.platform == "win32":
                                                    
                                        main()