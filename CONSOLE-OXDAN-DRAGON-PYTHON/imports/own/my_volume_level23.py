from ctypes import cast, POINTER
from msvcrt import getch
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import imports.own.will_go_to_start
from colorama import Fore

def my_volume_level():

    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
        IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))

    if (volume.GetMasterVolumeLevelScalar() * 100) == 0:

        print(Fore.YELLOW + "\nWindows volume muted: " + Fore.GREEN + "yes" + Fore.WHITE)

    elif (volume.GetMasterVolumeLevelScalar() * 100) > 0:

        print(Fore.YELLOW + "\nWindows volume muted: " + Fore.RED + "no" + Fore.WHITE)

    print(Fore.YELLOW + "Current windows volume: " + Fore.WHITE + str(round(volume.GetMasterVolumeLevelScalar() * 100)))
    #getch()
    imports.own.will_go_to_start.main()