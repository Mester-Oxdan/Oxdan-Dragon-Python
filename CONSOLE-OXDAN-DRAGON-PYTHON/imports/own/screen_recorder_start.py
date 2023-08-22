# importing the required packages
import pyautogui
import cv2
import numpy as np
from colorama import *
import imports.own.will_go_to_start

def screen_recorder_start():

        print(Fore.RED + "\nPress 'Esc' for exit" + Fore.WHITE)

        # Specify resolution
        resolution = (1920, 1080) # 1920, 1080
  
        # Specify video codec
        codec = cv2.VideoWriter_fourcc(*"XVID")
  
        # Specify name of Output file
        filename = "output_recorded_screen.avi"
  
        # Specify frames rate. We can choose any 
        # value and experiment with it
        fps = 60.0
  
        # Creating a VideoWriter object
        out = cv2.VideoWriter(filename, codec, fps, resolution)
  
        # Create an Empty window
        cv2.namedWindow("Video: ", cv2.WINDOW_NORMAL)
  
        # Resize this window
        cv2.resizeWindow("Video: ", 480, 270)
  
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
                    cv2.imshow('Video: ', frame)
      
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