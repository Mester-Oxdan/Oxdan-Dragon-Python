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

def update_program():
    try:

        # Replace with the URL of the raw file on GitHub
        raw_file_url = "https://raw.githubusercontent.com/Mester-Oxdan/Oxdan-Dragon-Python/main/version"

        # Make the GET request to fetch the file content
        response = requests.get(raw_file_url)

        if response.status_code == 200:
            version_content = response.text.strip()  # The file content as a string, with leading/trailing whitespace removed
            if (version_content == '1.2023'):  # Use '==' for comparison, and '2.2024' instead of '1.2023'
                #print(Fore.RED + "You're not using the latest version." + Fore.WHITE)
                #print(Fore.RED + "\n(!ERROR!) " + Fore.WHITE + "=" + Fore.GREEN + " (!Program already updated to last version!)" + Fore.WHITE)
                print("")
            else:
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
        else:
            print(f"Failed to fetch file content. Status code: {response.status_code}")
            msvcrt.getch()
            
    except Exception as e:
        print("Error:", e)
        msvcrt.getch()
        
update_program()

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