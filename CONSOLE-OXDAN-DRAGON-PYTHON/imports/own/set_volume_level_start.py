import win32api
import win32con
import time
from ctypes import cast, POINTER
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from comtypes import CLSCTX_ALL
import imports.own.will_go_to_start

def setWindowsVolumeLevel(volumeLevel):
    # Set the volume level using the VK_VOLUME_UP and VK_VOLUME_DOWN virtual keys
        for i in range(volumeLevel):
            win32api.keybd_event(win32con.VK_VOLUME_UP, 0, 0, 0)
            win32api.keybd_event(win32con.VK_VOLUME_UP, 0, win32con.KEYEVENTF_KEYUP, 0)
            time.sleep(0.1) # Wait for the volume to adjust

def set_volume_level_start(a):

    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
                           IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
 
    # Control volume
    ##volume.SetMasterVolumeLevel(-0.0, None) #max
    ##volume.SetMasterVolumeLevel(-5.0, None) #72%

    volume.SetMute(0, None)
    volume.SetMasterVolumeLevel(-65.0, None) #0%

    volumeLevel = int(a) / 2 # Set the desired volume level here
    setWindowsVolumeLevel(int(volumeLevel))
    imports.own.will_go_to_start.main()
