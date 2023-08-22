import pyautogui
from time import sleep
from pynput.keyboard import Key, Listener
from threading import Thread
import os
from time import sleep
from colorama import *
import imports.own.will_go_to_start
import pyautogui
import keyboard
from colorama import Fore

def auto_clicker_start():

        auto_clicker_bool = True
        print(Fore.RED + "\nPress 'Esc' for exit" + Fore.WHITE)

        while auto_clicker_bool:

            pyautogui.leftClick()

            if keyboard.is_pressed("esc"):
                
                auto_clicker_bool = False
                imports.own.will_go_to_start.main()
