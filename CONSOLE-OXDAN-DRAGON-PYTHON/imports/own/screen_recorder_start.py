# importing the required packages
import pyautogui
import cv2
import numpy as np
from colorama import Fore
import imports.own.will_go_to_start
import ctypes
import os 

def set_window_icon(window_name, icon_path):
    # Get the window handle (HWND) for the OpenCV window
    hwnd = ctypes.windll.user32.FindWindowW(None, window_name)
    
    if hwnd:
        # Load the icon from the specified path
        hIcon = ctypes.windll.user32.LoadImageW(None, icon_path, 1, 0, 0, 0x00000010 | 0x00000080)
        
        # Set the icon for the window
        ctypes.windll.user32.SendMessageW(hwnd, 0x0080, 1, hIcon)  # ICON_BIG
        ctypes.windll.user32.SendMessageW(hwnd, 0x0080, 0, hIcon)  # ICON_SMALL
    else:
        #print("Could not find OpenCV window!")
        print(Fore.RED + "\n(!ERROR!) " + Fore.WHITE + "=" + Fore.GREEN + " (!Could not find OpenCV window!)\n" + Fore.WHITE)
        imports.own.will_go_to_start.main()

def screen_recorder_start():

        print(Fore.RED + "\nPress 'Esc' for exit" + Fore.WHITE)

        # Specify resolution
        resolution = (1920, 1080) # 1920, 1080
  
        # Specify video codec
        codec = cv2.VideoWriter_fourcc(*"XVID")
  
        # Specify name of Output file
        filename = "screen_recoring.avi"
  
        # Specify frames rate. We can choose any 
        # value and experiment with it
        fps = 60.0
  
        # Creating a VideoWriter object
        out = cv2.VideoWriter(filename, codec, fps, resolution)
  
        # Create an Empty window
        cv2.namedWindow("Screen Recorder: ", cv2.WINDOW_NORMAL)
  
        # Resize this window
        cv2.resizeWindow("Screen Recorder: ", 480, 270)
        # Set custom icon for the window
        icon_path = os.environ["OXDAN-DRAGON-PYTHON"] + "\\imports\\own\\my_dragon_ico.ico"  # Replace with the correct path to your .ico file
        set_window_icon("Screen Recorder: ", icon_path)
        refed = True

        while refed == True:

                    # Take screenshot using PyAutoGUI
                    img = pyautogui.screenshot()
  
                    # Convert the screenshot to a numpy array
                    frame = np.array(img)
  
                    # Convert it from BGR(Blue, Green, Red) to
                    # RGB(Red, Green, Blue)
                    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
  
                    # Write it to the output file
                    out.write(frame)
      
                    # Optional: Display the recording screen
                    cv2.imshow('Screen Recorder: ', frame)
      
                    # Stop recording when we press 'q'
                    if cv2.waitKey(27) >= 0:

                                refed = False

                                # Release the Video writer
                                out.release()
  
                                # Destroy all windows
                                cv2.destroyAllWindows()

                                imports.own.will_go_to_start.main()
  
        # Release the Video writer
        out.release()
  
        # Destroy all windows
        cv2.destroyAllWindows()

        imports.own.will_go_to_start.main()