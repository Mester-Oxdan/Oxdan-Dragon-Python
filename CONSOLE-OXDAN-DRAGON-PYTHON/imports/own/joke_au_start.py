import os
import random
from colorama import Fore
from ctypes import cast, POINTER
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from comtypes import CLSCTX_ALL
import imports.own.will_go_to_start

def joke_au_start(name):

    try:

        if name == "au" or name == "AU" or name == "Au":

                devices = AudioUtilities.GetSpeakers()
                interface = devices.Activate(
                       IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
                volume = cast(interface, POINTER(IAudioEndpointVolume))
 
                # Control volume
                ##volume.SetMasterVolumeLevel(-0.0, None) #max
                ##volume.SetMasterVolumeLevel(-5.0, None) #72%

                volume.SetMute(0, None)
                volume.SetMasterVolumeLevel(-16.0, None) #51%

                random_file_au = random.choice(os.listdir("memes\\(+)Audio"))
                os.system("start memes\\(+)Audio\\" + random_file_au)
                imports.own.will_go_to_start.main()

    except:

        print(Fore.RED + "\n(!ERROR!) " + Fore.WHITE + "=" + Fore.GREEN + " (!Enter joke option!)\n" + Fore.WHITE)
        imports.own.will_go_to_start.main()
