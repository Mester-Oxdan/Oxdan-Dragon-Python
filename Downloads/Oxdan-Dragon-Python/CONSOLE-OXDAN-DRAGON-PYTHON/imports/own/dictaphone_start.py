import sounddevice
from scipy.io.wavfile import write
import colorama
import imports.own.will_go_to_start
from colorama import Fore

def dictaphone_start():

    fs= 44100

    try:

        second =  int(input(Fore.YELLOW + "\nEnter time to finish recording (in seconds): " + Fore.WHITE))

    except:

        print(colorama.Fore.RED + "\n(!ERROR!) " + colorama.Fore.WHITE + "=" + colorama.Fore.GREEN + " (!Only integers!)\n" + colorama.Fore.WHITE)
        imports.own.will_go_to_start.main()

    print(Fore.GREEN + "\n[!] Recording!\n" + Fore.WHITE)
    record_voice = sounddevice.rec( int ( second * fs ) , samplerate = fs , channels = 2 )
    sounddevice.wait()
    write("Output_racorded_voice.wav",fs,record_voice)
    print(Fore.RED + "[!] Recording Finished!" + Fore.WHITE)
    imports.own.will_go_to_start.main()