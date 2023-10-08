import os
from colorama import Fore
from win32gui import *
from win32api import *
from win32ui import *
from win32con import *
from random import *
import keyboard
import cv2
import imports.own.will_go_to_start

def gdi_virus_start():

    print(Fore.RED + "\nPress 'Esc' for exit" + Fore.WHITE)

    while True:

        desk = GetDC(0)
        x = GetSystemMetrics(0)
        y = GetSystemMetrics(1)

        for i in range(0, 100):
            brush = CreateSolidBrush(RGB(
                randrange(255),
                randrange(255),
                randrange(255),
                ))
            SelectObject(desk, brush)
            PatBlt(desk, randrange(x), randrange(y), randrange(x), randrange(y),  PATINVERT)
            DeleteObject(brush)
            Sleep(100)

            if keyboard.is_pressed('Esc'):

                        print(" ")
                        imports.own.will_go_to_start.main()

        ReleaseDC(desk, GetDesktopWindow())
        DeleteDC(desk)

        if keyboard.is_pressed('Esc'):

                        print(" ")
                        imports.own.will_go_to_start.main()
