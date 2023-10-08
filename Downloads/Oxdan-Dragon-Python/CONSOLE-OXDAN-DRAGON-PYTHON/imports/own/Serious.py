import imports.own.will_go_to_start
from colorama import Fore
from translate import Translator
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

def Serious():

    if imports.own.will_go_to_start.x.lower() == "tim" or imports.own.will_go_to_start.x.lower() == "time": # tim (-)

        try:

            time_start()

        except:

            imports.own.will_go_to_start.main()

    elif imports.own.will_go_to_start.x.lower() == "translator":

        try:

            print(" ")
            print(Fore.RED + "Write 'esc' (for exit)")
            x = input(Fore.YELLOW + "\nEnter language from: " + Fore.WHITE)
            if x == "esc":

                imports.own.will_go_to_start.main()

            y = input(Fore.YELLOW + "Enter language to: " + Fore.WHITE)
            if y == "esc":

                imports.own.will_go_to_start.main()
            z = input(Fore.YELLOW + "Enter text to translate from " + x + " to " + y + ": " + Fore.WHITE)
            if z == "esc":

                imports.own.will_go_to_start.main()
            translator = Translator(from_lang = str(x), to_lang = str(y))

            result = translator.translate(str(z))

            print(Fore.YELLOW + "Translated text: " + Fore.WHITE + result)
            #print(" ")

            imports.own.will_go_to_start.main()

        except:

            print(Fore.RED + "\n(!ERROR!) " + Fore.WHITE + "=" + Fore.GREEN + " (!Enter valid languages!)\n" + Fore.WHITE)
            imports.own.will_go_to_start.main()

    if imports.own.will_go_to_start.x.lower() == "stopwatch": # stopwatch (+)

        try:

            stopwatch_start()

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