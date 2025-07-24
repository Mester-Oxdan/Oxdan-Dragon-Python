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
import asyncio
import aiohttp

command_queue = []  # Global queue for pre-fed commands

global which1
which1 = True

global yes_or_no
yes_or_no = True

input_list = []

#print(os.path.join(os.environ["OXDAN-DRAGON-PYTHON"],r"my_dragon_ico_transformed.png"))
#msvcrt.getch()

def remove_098(string):
    return string.replace(" ", "")

def update_program():
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
                    message = Notification(app_id="OXDAN-DRAGON-PYTHON",
                                   title="New Update!",
                                   msg="New update available. After login use 'update' command.",
                                   duration="short",
                                   icon=os.path.join(os.environ["OXDAN-DRAGON-PYTHON"],r"my_dragon_ico_transformed.png"))
                                   #icon=r"C:\Users\bogda\Downloads\Oxdan-Dragon-Python\CONSOLE-OXDAN-DRAGON-PYTHON\imports\own\my_dragon_ico_transformed.png")
                                   
            
                    message.set_audio(audio.Default, loop=False)
                    message.add_actions(label="Go to Website.", launch="https://github.com/Mester-Oxdan/Oxdan-Dragon-Python")

                    message.show()
                    #imports.own.will_go_to_start.main()

            asyncio.run(main())

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
            #writex = input("\n" + current_dir + ">> ") # get path (+)
            if command_queue:
                writex = command_queue.pop(0)
                print(f"\n{current_dir}>> {writex}")  # Simulate echoing command
            else:
                writex = input("\n" + current_dir + ">> ")

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