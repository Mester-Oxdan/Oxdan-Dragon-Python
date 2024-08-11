import imports.own.will_go_to_start
from colorama import Fore
from imports.own.timer_start import timer_start
from imports.own.time_start import time_start
from imports.own.stopwatch_start import stopwatch_start
from imports.own.calculator_start import calculator_start
from imports.own.calendar_start import calendar_start
from imports.own.cur_conv_start import cur_conv_start
from imports.own.dictaphone_start import dictaphone_start
from imports.own.video_recorder_start import webcam_recorder_start
from imports.own.screen_recorder_start import screen_recorder_start
from imports.own.notepad_start import notepad_start
from imports.own.d_price_calc_start import d_price_calc_start
from imports.own.chat_start import chat_start
import os
from googletrans import Translator
import colorama

def Serious():

    if imports.own.will_go_to_start.x.lower() == "tim" or imports.own.will_go_to_start.x.lower() == "time": # tim (-)

        try:
            #print(os.path.join(os.environ["OXDAN-DRAGON-PYTHON"] +"\imports\own" ,"\my_dragon_ico.ico"))
            time_start()

        except:

            imports.own.will_go_to_start.main()

    elif imports.own.will_go_to_start.x.lower() == "translator":

        try:

            print(" ")
            print(Fore.RED + "Enter 'esc' (for exit)" + Fore.WHITE)
            x = input(Fore.YELLOW + "Enter language from: " + Fore.WHITE)
            if imports.own.will_go_to_start.remove_098(x.lower()) == "esc":
                imports.own.will_go_to_start.main()

            print(Fore.RED + "\nEnter 'esc' (for exit)" + Fore.WHITE)
            y = input(Fore.YELLOW + "Enter language to: " + Fore.WHITE)
            if imports.own.will_go_to_start.remove_098(y.lower()) == "esc":
                imports.own.will_go_to_start.main()

            print(Fore.RED + "\nEnter 'esc' (for exit)" + Fore.WHITE)
            z = input(Fore.YELLOW + f"Enter text to translate from {x} to {y}: " + Fore.WHITE)
            if imports.own.will_go_to_start.remove_098(z.lower()) == "esc":
                imports.own.will_go_to_start.main()

            # Create translator object
            translator = Translator()

            # Translate the entire sentence
            result = translator.translate(z, src=x, dest=y).text

            print(Fore.YELLOW + "Translated text: " + Fore.WHITE + result)
            imports.own.will_go_to_start.main()
            
        except:

            print(Fore.RED + "\n(!ERROR!) " + Fore.WHITE + "=" + Fore.GREEN + " (!Enter valid languages!)\n" + Fore.WHITE)
            imports.own.will_go_to_start.main()

    if imports.own.will_go_to_start.x.lower() == "stopwatch": # stopwatch (+)

        try:

            stopwatch_start()

        except:

            imports.own.will_go_to_start.main()
            
    """if imports.own.will_go_to_start.x.lower() == "chat": # chat (+)

        try:

            chat_start()

        except:

            imports.own.will_go_to_start.main()"""
            
    if imports.own.will_go_to_start.x.lower() == "3d_price_calc": # 3d_price_calc (+)

        try:

            d_price_calc_start()

        except:

            imports.own.will_go_to_start.main()

    if imports.own.will_go_to_start.x.lower() == "webcam_recorder": # webcam_recorder (+)

        try:

            webcam_recorder_start()

        except:

            imports.own.will_go_to_start.main()

    if imports.own.will_go_to_start.x.lower() == "screen_recorder": # screen_recorder (+)

        try:

            screen_recorder_start()

        except:

            imports.own.will_go_to_start.main()

    if imports.own.will_go_to_start.x.lower() == "dictaphone": # dictaphone (+)

        try:

            dictaphone_start()

        except:

            imports.own.will_go_to_start.main()

    if imports.own.will_go_to_start.x.lower() == "timer": # timer (+)
        
        try:

            timer_start()

        except:

            imports.own.will_go_to_start.main()

    elif imports.own.will_go_to_start.x.lower() == "calculator": # calculator (+)
                
        try:

            calculator_start()

        except:

            imports.own.will_go_to_start.main()

    elif imports.own.will_go_to_start.x.lower() == "calendar": # calendar (+)
            
        try:

            calendar_start()

        except:

            imports.own.will_go_to_start.main()

    elif imports.own.will_go_to_start.x.lower() == "cur_conv": # cur_conv (+)
            
        try:

            cur_conv_start()

        except:

            imports.own.will_go_to_start.main()

    elif imports.own.will_go_to_start.x.lower() == "notepad": # notepad (+)
            
        try:

            notepad_start()
            imports.own.will_go_to_start.main()

        except:

            imports.own.will_go_to_start.main()