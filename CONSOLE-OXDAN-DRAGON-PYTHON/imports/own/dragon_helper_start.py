import speech_recognition as sr
import pyttsx3
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
import imports.own.color_start
import imports.own.color_back_start
from ctypes import cast, POINTER
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from comtypes import CLSCTX_ALL
from colorama import Fore 
import string
import imports.own.will_go_to_start

# Initialize the recognizer
r = sr.Recognizer()
 
# Function to convert text to
# speech
def SpeakText(command):
     
        # Initialize the engine
        engine = pyttsx3.init()
        engine.say(command)
        engine.runAndWait()

def dragon_helper_start():
    
    print(" ")
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
                           IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
 
    # Control volume
    ##volume.SetMasterVolumeLevel(-0.0, None) #max
    ##volume.SetMasterVolumeLevel(-5.0, None) #72%

    volume.SetMute(0, None)
    volume.SetMasterVolumeLevel(-15.0, None) #36%

    SpeakText("Hello I am Oxdan Dragon helper, Say exit for exit, How can I help you?")

    def go_to_dragon_helper():   
     
        # Exception handling to handle
        # exceptions at the runtime

        try:

                # use the microphone as source for input.
                with sr.Microphone() as source2:
             
                    # wait for a second to let the recognizer
                    # adjust the energy threshold based on
                    # the surrounding noise level
                    r.adjust_for_ambient_noise(source2, duration=0.2)
             
                    #listens for the user's input
                    audio2 = r.listen(source2)
             
                    #global MyText
                    # Using google to recognize audio
                    MyText = r.recognize_google(audio2)
                    MyText = MyText.lower()

                    devices = AudioUtilities.GetSpeakers()
                    interface = devices.Activate(
                           IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
                    volume = cast(interface, POINTER(IAudioEndpointVolume))
 
                    # Control volume
                    ##volume.SetMasterVolumeLevel(-0.0, None) #max
                    ##volume.SetMasterVolumeLevel(-5.0, None) #72%

                    volume.SetMute(0, None)
                    volume.SetMasterVolumeLevel(-15.0, None) #36%

                    list_MyText = MyText.split()

                    #for found_line in list_MyText:

                        #else:

                            #continue

                    # systems:
                    for found_line in list_MyText:

                        if found_line == "dot":

                            list_MyText.replace("dot", ".")
                            #list_MyText += "."
                            #MyText.strip()
                            #go_to_dragon_helper()
                            continue

                        #if found_line == "space":

                            #list_MyText.replace("space", " ")
                            #MyText.strip()
                            #go_to_dragon_helper()
                            #continue

                        if found_line == "dot." or found_line == "doug.":

                            try:
                                list_MyText.replace("dot.", "..")
                            except:
                                list_MyText.replace("doug.", "..")
                            #list_MyText += ".."
                            #MyText.strip()
                            #go_to_dragon_helper()
                            continue

                        else:

                            continue

                    # speaking:
                    if list_MyText[0].lower() == "hello":

                        SpeakText("Hello")
                        go_to_dragon_helper()

                    if list_MyText[0].lower() == "how are you":

                        SpeakText("I am good, What about you?")
                        go_to_dragon_helper()

                    if list_MyText[0].lower() == "about dragon helper":

                        SpeakText("I am same with dragon console but I can listen what did you say, I can understand just english, I can understand not for first time, you can dictate or spelling or say full words for me without normal commands i also have secret commands like this, Say exit for exit")
                        go_to_dragon_helper()

                    # Mains:
                    if list_MyText[0].lower() == "--help" or list_MyText[0].lower() == "-help" or list_MyText[0].lower() == "help" or list_MyText[0].lower() == "-h":

                        global x
                        imports.own.will_go_to_start.x = "-h"
                        imports.own.Commands.Commands()

                    if list_MyText[0].lower() == "--version" or list_MyText[0].lower() == "-version" or list_MyText[0].lower() == "version" or list_MyText[0].lower() == "-v":

                        global x
                        imports.own.will_go_to_start.x = "-v"
                        imports.own.Main_Commands.Main_Commands()

                    if list_MyText[0].lower() == "pip":

                        global x
                        imports.own.will_go_to_start.writex = "pip"
                        imports.own.Main_Commands.Main_Commands()

                    if list_MyText[0].lower() == "git":

                        global x
                        imports.own.will_go_to_start.writex = "git"
                        imports.own.Main_Commands.Main_Commands()

                    if list_MyText[0].lower() == "npm":

                        global x
                        imports.own.will_go_to_start.writex = "npm"
                        imports.own.Main_Commands.Main_Commands()

                    if list_MyText[0].lower() == "conda":

                        global x
                        imports.own.will_go_to_start.writex = "conda"
                        imports.own.Main_Commands.Main_Commands()

                    if list_MyText[0].lower() == "update":

                        global x
                        imports.own.will_go_to_start.writex = "update"
                        imports.own.Main_Commands.Main_Commands()

                    if list_MyText[0].lower() == "cls" or list_MyText[0].lower() == "clear":

                        global x
                        imports.own.will_go_to_start.x = "cls"
                        imports.own.Main_Commands.Main_Commands()

                    if list_MyText[0].lower() == "dir" or list_MyText[0].lower() == "ls":

                        global x
                        imports.own.will_go_to_start.x = "dir"
                        imports.own.Main_Commands.Main_Commands()

                    if list_MyText[0].lower() == "mkdir":

                            global x
                            imports.own.will_go_to_start.x = "mkdir"
                            list_MyText.remove("mkdir")
                            zxd = (''.join(list_MyText))
                            imports.own.Main_Commands.test = zxd
                            imports.own.Main_Commands.Main_Commands()

                    if list_MyText[0].lower() == "go" and list_MyText[1].lower() == "to":

                            global x
                            imports.own.will_go_to_start.x = "go_to"
                            list_MyText.remove("go")
                            list_MyText.remove("to")
                            zxd = (''.join(list_MyText))
                            imports.own.Main_Commands.cd = zxd
                            imports.own.Main_Commands.Main_Commands()

                    if list_MyText[0].lower() == "create":

                        global x
                        imports.own.will_go_to_start.x = "create" # test.txt
                        list_MyText.remove("create")
                        zxd_2 = (''.join(list_MyText))
                        imports.own.Main_Commands.name_56 = zxd_2
                        imports.own.Main_Commands.Main_Commands()

                    if list_MyText[0].lower() == "del" or list_MyText[0].lower() == "delete":

                        global x
                        imports.own.will_go_to_start.x = "del"
                        try:
                            list_MyText.remove("del")
                        except:
                            list_MyText.remove("delete")
                        zxd_3 = (''.join(list_MyText))
                        imports.own.Main_Commands.name_98 = zxd_3
                        imports.own.Main_Commands.Main_Commands()

                    if list_MyText[0].lower() == "install":

                        global x
                        imports.own.will_go_to_start.x = "install"
                        list_MyText.remove("install")
                        zxd_4 = (''.join(list_MyText))
                        imports.own.Main_Commands.name_578 = zxd_4
                        imports.own.Main_Commands.Main_Commands()

                    # Hackers Stuffs:
                    if list_MyText[0].lower() == "inject" and list_MyText[1].lower() == "prog" or list_MyText[0].lower() == "injector" and list_MyText[1].lower() == "program":

                        global x
                        imports.own.will_go_to_start.x = "inject_prog"
                        imports.own.Hacker_Stuffs.Hacker_Stuffs()

                    if list_MyText[0].lower() == "pas" and list_MyText[1].lower() == "gen" or list_MyText[0].lower() == "password" and list_MyText[1].lower() == "generator":

                        global x
                        imports.own.will_go_to_start.x = "pas_gen"
                        try:
                            list_MyText.remove("pas")
                            list_MyText.remove("gen")
                        except:
                            list_MyText.remove("password")
                            list_MyText.remove("generator")
                        zxd_5 = (''.join(list_MyText))
                        imports.own.Hacker_Stuffs.name_uy = zxd_5
                        imports.own.Hacker_Stuffs.Hacker_Stuffs()

                    if list_MyText[0].lower() == "my" and list_MyText[1].lower() == "wifi" and list_MyText[2].lower() == "pas" or list_MyText[0].lower() == "my" and list_MyText[1].lower() == "wifi" and list_MyText[2].lower() == "passwords":

                        global x
                        imports.own.will_go_to_start.x = "my_wifi_pas"
                        imports.own.Hacker_Stuffs.Hacker_Stuffs()

                    if list_MyText[0].lower() == "cor" and list_MyText[1].lower() == "desk" or list_MyText[0].lower() == "coordinates" and list_MyText[1].lower() == "desktop":

                        global x
                        imports.own.will_go_to_start.x = "cor_desk"
                        imports.own.Hacker_Stuffs.Hacker_Stuffs()

                    if list_MyText[0].lower() == "ascii" and list_MyText[1].lower() == "code":

                        global x
                        imports.own.will_go_to_start.x = "ascii_code"
                        imports.own.Hacker_Stuffs.Hacker_Stuffs()

                    if list_MyText[0].lower() == "ip" and list_MyText[1].lower() == "search":

                        global x
                        imports.own.will_go_to_start.x = "ip_search"
                        imports.own.Hacker_Stuffs.Hacker_Stuffs()

                    if list_MyText[0].lower() == "wifi" and list_MyText[1].lower() == "hack":

                        global x
                        imports.own.will_go_to_start.x = "wifi_hack"
                        imports.own.Hacker_Stuffs.Hacker_Stuffs()

                    if list_MyText[0].lower() == "con" and list_MyText[1].lower() == "wifi":

                        global x
                        imports.own.will_go_to_start.x = "con_wifi"
                        imports.own.Hacker_Stuffs.Hacker_Stuffs()

                    if list_MyText[0].lower() == "get" and list_MyText[1].lower() == "ip" and list_MyText[1].lower() == "website":

                        global x
                        imports.own.will_go_to_start.x = "get_ip_website"
                        list_MyText.remove("get")
                        list_MyText.remove("ip")
                        list_MyText.remove("website")
                        zxd_5 = (''.join(list_MyText))
                        imports.own.Hacker_Stuffs.zxd_5 = zxd_5
                        imports.own.Hacker_Stuffs.Hacker_Stuffs()

                    if list_MyText[0].lower() == "auto" and list_MyText[1].lower() == "clicker":

                        global x
                        imports.own.will_go_to_start.x = "auto_clicker"
                        imports.own.Hacker_Stuffs.Hacker_Stuffs()

                    if list_MyText[0].lower() == "morse" and list_MyText[1].lower() == "code":

                        global x
                        imports.own.will_go_to_start.x = "morse_code"
                        imports.own.Hacker_Stuffs.Hacker_Stuffs()

                    if list_MyText[0].lower() == "caesar" and list_MyText[1].lower() == "cipher":

                        global x
                        imports.own.will_go_to_start.x = "caesar_cipher"
                        imports.own.Hacker_Stuffs.Hacker_Stuffs()

                    # Pictures:
                    if list_MyText[0].lower() == "ukraine":

                        global x
                        imports.own.will_go_to_start.x = "ukraine"
                        imports.own.Pictures.Pictures()

                    if list_MyText[0].lower() == "author":

                        global x
                        imports.own.will_go_to_start.x = "author"
                        imports.own.Pictures.Pictures()

                    if list_MyText[0].lower() == "matrix":

                        global x
                        imports.own.will_go_to_start.x = "matrix"
                        imports.own.Pictures.Pictures()

                    # Accounts:
                    if list_MyText[0].lower() == "login":

                        global x
                        imports.own.will_go_to_start.x = "login"
                        imports.own.Accounts.Accounts()

                    if list_MyText[0].lower() == "registration":

                        global x
                        imports.own.will_go_to_start.x = "registration"
                        imports.own.Accounts.Accounts()

                    if list_MyText[0].lower() == "instructions":

                        global x
                        imports.own.will_go_to_start.x = "instructions"
                        imports.own.Accounts.Accounts()

                    if list_MyText[0].lower() == "del" and list_MyText[1].lower() == "account":

                        global x
                        imports.own.will_go_to_start.x = "del_account"
                        imports.own.Accounts.Accounts()

                    if list_MyText[0].lower() == "logout":

                        global x
                        imports.own.will_go_to_start.x = "logout"
                        imports.own.Accounts.Accounts()

                    # Serious:
                    if list_MyText[0].lower() == "tim" or list_MyText[0].lower() == "time":

                        global x
                        imports.own.will_go_to_start.x = "tim"
                        imports.own.Serious.Serious()

                    if list_MyText[0].lower() == "stopwatch":

                        global x
                        imports.own.will_go_to_start.x = "stopwatch"
                        imports.own.Serious.Serious()

                    if list_MyText[0].lower() == "timer":

                        global x
                        imports.own.will_go_to_start.x = "timer"
                        imports.own.Serious.Serious()

                    if list_MyText[0].lower() == "calculator":

                        global x
                        imports.own.will_go_to_start.x = "calculator"
                        imports.own.Serious.Serious()

                    if list_MyText[0].lower() == "calendar":

                        global x
                        imports.own.will_go_to_start.x = "calendar"
                        imports.own.Serious.Serious()

                    if list_MyText[0].lower() == "webcam" and list_MyText[1].lower() == "recorder":

                        global x
                        imports.own.will_go_to_start.x = "webcam_recorder"
                        imports.own.Serious.Serious()

                    if list_MyText[0].lower() == "screen" and list_MyText[1].lower() == "recorder":

                        global x
                        imports.own.will_go_to_start.x = "screen_recorder"
                        imports.own.Serious.Serious()

                    if list_MyText[0].lower() == "cur" and list_MyText[1].lower() == "conv" or list_MyText[0].lower() == "currency" and list_MyText[1].lower() == "converter":

                        global x
                        imports.own.will_go_to_start.x = "cur_conv"
                        imports.own.Serious.Serious()

                    if list_MyText[0].lower() == "notepad":

                        global x
                        imports.own.will_go_to_start.x = "notepad"
                        imports.own.Serious.Serious()

                    if list_MyText[0].lower() == "translator":

                        global x
                        imports.own.will_go_to_start.x = "translator"
                        imports.own.Serious.Serious()

                    if list_MyText[0].lower() == "dictaphone":

                        global x
                        imports.own.will_go_to_start.x = "dictaphone"
                        imports.own.Serious.Serious()

                    # Games:
                    if list_MyText[0].lower() == "pacman":

                        global x
                        imports.own.will_go_to_start.x = "pacman"
                        imports.own.Games.Games()

                    if list_MyText[0].lower() == "2048":

                        global x
                        imports.own.will_go_to_start.x = "2048"
                        imports.own.Games.Games()

                    if list_MyText[0].lower() == "arkanoid":

                        global x
                        imports.own.will_go_to_start.x = "arkanoid"
                        imports.own.Games.Games()

                    if list_MyText[0].lower() == "flappy" and list_MyText[1].lower() == "bird":

                        global x
                        imports.own.will_go_to_start.x = "flappy_bird"
                        imports.own.Games.Games()

                    if list_MyText[0].lower() == "tetris":

                        global x
                        imports.own.will_go_to_start.x = "tetris"
                        imports.own.Games.Games()

                    if list_MyText[0].lower() == "hangman":

                        global x
                        imports.own.will_go_to_start.x = "hangman"
                        imports.own.Games.Games()

                    if list_MyText[0].lower() == "car" and list_MyText[1].lower() == "racing":

                        global x
                        imports.own.will_go_to_start.x = "car_racing"
                        imports.own.Games.Games()

                    if list_MyText[0].lower() == "guess_number":

                        global x
                        imports.own.will_go_to_start.x = "guess_number"
                        imports.own.Games.Games()

                    if list_MyText[0].lower() == "math" and list_MyText[1].lower() == "game":

                        global x
                        imports.own.will_go_to_start.x = "math_game"
                        imports.own.Games.Games()

                    if list_MyText[0].lower() == "typing" and list_MyText[1].lower() == "tutor":

                        global x
                        imports.own.will_go_to_start.x = "typing_tutor"
                        imports.own.Games.Games()

                    if list_MyText[0].lower() == "battle" and list_MyText[1].lower() == "city":

                        global x
                        imports.own.will_go_to_start.x = "battle_city"
                        imports.own.Games.Games()

                    if list_MyText[0].lower() == "doom":

                        global x
                        imports.own.will_go_to_start.x = "doom"
                        imports.own.Games.Games()

                    if list_MyText[0].lower() == "mario":

                        global x
                        imports.own.will_go_to_start.x = "mario"
                        imports.own.Games.Games()

                    if list_MyText[0].lower() == "snake":

                        global x
                        imports.own.will_go_to_start.x = "snake"
                        list_MyText.remove("snake")
                        zxd_78 = (''.join(list_MyText))
                        imports.own.Games.zxd_6 = zxd_78
                        imports.own.Games.Games()

                    if list_MyText[0].lower() == "ping" and list_MyText[1].lower() == "pong":

                        global x
                        imports.own.will_go_to_start.x = "ping_pong"
                        list_MyText.remove("ping")
                        list_MyText.remove("pong")
                        zxd_7 = (''.join(list_MyText))
                        imports.own.Games.zxd_7 = zxd_7
                        imports.own.Games.Games()

                    if list_MyText[0].lower() == "tic" and list_MyText[1].lower() == "tac" and list_MyText[2].lower() == "toe":

                        global x
                        imports.own.will_go_to_start.x = "tic_tac_toe"
                        list_MyText.remove("tic")
                        list_MyText.remove("tac")
                        list_MyText.remove("toe")
                        zxd_8 = (''.join(list_MyText))
                        imports.own.Games.zxd_8 = zxd_8
                        imports.own.Games.Games()

                    if list_MyText[0].lower() == "checkers":

                        global x
                        imports.own.will_go_to_start.x = "checkers"
                        list_MyText.remove("checkers")
                        zxd_9 = (''.join(list_MyText))
                        imports.own.Games.zxd_9 = zxd_9
                        imports.own.Games.Games()

                    if list_MyText[0].lower() == "chess":

                        global x
                        imports.own.will_go_to_start.x = "chess"
                        list_MyText.remove("chess")
                        zxd_10 = (''.join(list_MyText))
                        imports.own.Games.zxd_10 = zxd_10
                        imports.own.Games.Games()
                        
                    if list_MyText[0].lower() == "space" and list_MyText[1].lower() == "shooter":

                        global x
                        imports.own.will_go_to_start.x = "space_shooter"
                        imports.own.Games.Games()

                    # Owns:
                    if list_MyText[0].lower() == "title":

                        global x
                        imports.own.will_go_to_start.x = "title"
                        list_MyText.remove("title")
                        a_tit = (''.join(list_MyText))
                        imports.own.Own.a_tit = a_tit
                        imports.own.Own.Own()

                    if list_MyText[0].lower() == "new" or list_MyText[0].lower() == "start":

                        global x
                        imports.own.will_go_to_start.x = "start"
                        imports.own.Own.Own()

                    if list_MyText[0].lower() == "open":

                        global x
                        imports.own.will_go_to_start.x = "open"
                        list_MyText.remove("open")
                        a_tit_1 = (''.join(list_MyText))
                        imports.own.Own.a_tit_1 = a_tit_1
                        imports.own.Own.Own()

                    if list_MyText[0].lower() == "shutdown":

                        global x
                        imports.own.will_go_to_start.x = "shutdown"
                        imports.own.Own.Own()

                    if list_MyText[0].lower() == "restart":

                        global x
                        imports.own.will_go_to_start.x = "restart"
                        imports.own.Own.Own()

                    if list_MyText[0].lower() == "data":

                        global x
                        imports.own.will_go_to_start.x = "data"
                        imports.own.Own.Own()

                    if list_MyText[0].lower() == "i" and list_MyText[1].lower() == "am" and list_MyText[2].lower() == "here":

                        global x
                        imports.own.will_go_to_start.x = "i_am_here"
                        imports.own.Own.Own()

                    if list_MyText[0].lower() == "&main" or list_MyText[0].lower() == "main":

                        global x
                        imports.own.will_go_to_start.x = "&main"
                        try:
                            list_MyText.remove("&main")
                        except:
                            list_MyText.remove("main")
                        a_tit_23 = (''.join(list_MyText))
                        imports.own.Own.a_tit_23 = a_tit_23
                        imports.own.Own.Own()

                    if list_MyText[0].lower() == "donators":

                        global x
                        imports.own.will_go_to_start.x = "donators"
                        imports.own.Own.Own()

                    if list_MyText[0].lower() == "helpers":

                        global x
                        imports.own.will_go_to_start.x = "helpers"
                        imports.own.Own.Own()

                    if list_MyText[0].lower() == "color":

                        global x
                        imports.own.will_go_to_start.x = "color"
                        list_MyText.remove("color")
                        a_tit_25 = (''.join(list_MyText))
                        imports.own.color_start.a_tit_25 = a_tit_25
                        imports.own.Own.Own()

                    if list_MyText[0].lower() == "color" and list_MyText[1].lower() == "back":

                        global x
                        imports.own.will_go_to_start.x = "color_back"
                        list_MyText.remove("color")
                        list_MyText.remove("back")
                        a_tit_278 = (''.join(list_MyText))
                        imports.own.color_back_start.a_tit_278 = a_tit_278
                        imports.own.Own.Own()

                    if list_MyText[0].lower() == "joke":

                        global x
                        imports.own.will_go_to_start.x = "joke"
                        list_MyText.remove("joke")
                        a_tit_2789 = (''.join(list_MyText))
                        imports.own.joke_start.a_tit_2789 = a_tit_2789
                        imports.own.Own.Own()

                    if list_MyText[0].lower() == "i?" or list_MyText[0].lower() == "i":

                        global x
                        imports.own.will_go_to_start.x = "i?"
                        imports.own.Own.Own()

                    if list_MyText[0].lower() == "administrator" or list_MyText[0].lower() == "admin" or list_MyText[0].lower() == "superuser":

                        global x
                        imports.own.will_go_to_start.x = "admin"
                        imports.own.Own.Own()

                    if list_MyText[0].lower() == "chan" and list_MyText[1].lower() == "backg":

                        global x
                        imports.own.will_go_to_start.x = "chan_backg"
                        imports.own.Own.Own()

                    if list_MyText[0].lower() == "send" and list_MyText[1].lower() == "ph" and list_MyText[2].lower() == "message":

                        global x
                        imports.own.will_go_to_start.x = "send_ph_message"
                        imports.own.Own.Own()

                    if list_MyText[0].lower() == "history":

                        global x
                        imports.own.will_go_to_start.x = "history"
                        imports.own.Own.Own()

                    if list_MyText[0].lower() == "cls" and list_MyText[1].lower() == "history":

                        global x
                        imports.own.will_go_to_start.x = "cls_history"
                        imports.own.Own.Own()

                    if list_MyText[0].lower() == "memory":

                        global x
                        imports.own.will_go_to_start.x = "memory"
                        imports.own.Own.Own()

                    if list_MyText[0].lower() == "rules":

                        global x
                        imports.own.will_go_to_start.x = "rules"
                        imports.own.Own.Own()

                    if list_MyText[0].lower() == "commands":

                        global x
                        imports.own.will_go_to_start.x = "commands"
                        imports.own.Own.Own()

                    if list_MyText[0].lower() == "tips":

                        global x
                        imports.own.will_go_to_start.x = "tips"
                        imports.own.Own.Own()

                    if list_MyText[0].lower() == "links":

                        global x
                        imports.own.will_go_to_start.x = "links"
                        imports.own.Own.Own()

                    if list_MyText[0].lower() == "my" and list_MyText[1].lower() == "volume" and list_MyText[2].lower() == "level":

                        global x
                        imports.own.will_go_to_start.x = "my_volume_level"
                        imports.own.Own.Own()

                    if list_MyText[0].lower() == "set" and list_MyText[1].lower() == "volume" and list_MyText[2].lower() == "level":

                        global x
                        imports.own.will_go_to_start.x = "set_volume_level"
                        list_MyText.remove("set")
                        list_MyText.remove("volume")
                        list_MyText.remove("level")
                        a_iuy = (''.join(list_MyText))
                        imports.own.Own.a_tit_2788 = a_iuy
                        imports.own.Own.Own()

                    if list_MyText[0].lower() == "set" and list_MyText[1].lower() == "mute":

                        global x
                        imports.own.imports.own.will_go_to_start.x = "set_mute"
                        list_MyText.remove("set")
                        list_MyText.remove("mute")
                        a_tit_2788 = (''.join(list_MyText))
                        imports.own.Own.a_tit_2788 = a_tit_2788
                        imports.own.Own.Own()

                    if list_MyText[0].lower() == "ip" or list_MyText[0].lower() == "ip" and list_MyText[1].lower() == "address":

                        global x
                        imports.own.will_go_to_start.x = "ip"
                        imports.own.Own.Own()

                    if list_MyText[0].lower() == "size":

                        global x
                        imports.own.will_go_to_start.x = "size"
                        list_MyText.remove("size")
                        a_tit_bg = list_MyText[1]
                        a_tit_bg_2 = list_MyText[2]
                        imports.own.Own.a_tit_bg = a_tit_bg
                        imports.own.Own.a_tit_bg_2 = a_tit_bg_2
                        imports.own.Own.Own()

                    if list_MyText[0].lower() == "my" and list_MyText[1].lower() == "location":

                        global x
                        imports.own.will_go_to_start.x = "my_location"
                        imports.own.Own.Own()

                    if list_MyText[0].lower() == "system" and list_MyText[1].lower() == "info":

                        global x
                        imports.own.will_go_to_start.x = "system_info"
                        imports.own.Own.Own()

                    if list_MyText[0].lower() == "energy" or list_MyText[0].lower() == "power":

                        global x
                        imports.own.will_go_to_start.x = "energy"
                        imports.own.Own.Own()

                    # Pranks:
                    if list_MyText[0].lower() == "prank" and list_MyText[1].lower() == "button":

                        global x
                        imports.own.will_go_to_start.x = "prank_button"
                        list_MyText.remove("prank")
                        list_MyText.remove("button")
                        zxd_5 = (''.join(list_MyText))
                        imports.own.Own.zxd_5 = zxd_5
                        imports.own.Pranks.Pranks()

                    if list_MyText[0].lower() == "melt" and list_MyText[1].lower() == "screen":

                        global x
                        imports.own.will_go_to_start.x = "melt_screen"
                        imports.own.Pranks.Pranks()

                    if list_MyText[0].lower() == "gdi" and list_MyText[1].lower() == "virus":

                        global x
                        imports.own.will_go_to_start.x = "gdi_virus"
                        imports.own.Pranks.Pranks()

                    # Elses:

                    # exit:
                    if list_MyText[0].lower() == "escape" or list_MyText[0].lower() == "exit" or list_MyText[0].lower() == "quit" or list_MyText[0].lower() == "stop" or list_MyText[0].lower() == "stop it" or list_MyText[0].lower() == "nothing":

                        imports.own.will_go_to_start.main()

                    print(Fore.YELLOW + "You say: " + Fore.WHITE + MyText)
                    SpeakText(MyText)
                    go_to_dragon_helper()

        except:

            if imports.own.will_go_to_start.x == "prank_button" or imports.own.will_go_to_start.x == "exit" or imports.own.will_go_to_start.x == "esc" or imports.own.will_go_to_start.x == "quit" or imports.own.will_go_to_start.x == "admin" or imports.own.will_go_to_start.x == "administrator" or imports.own.will_go_to_start.x == "superuser":

                quit(0)

            print("You say nothing")
            go_to_dragon_helper()

    go_to_dragon_helper()
