import cv2
import imports.own.will_go_to_start
from colorama import Fore
import colorama
import ctypes
import os

def set_window_icon_2(window_name, icon_path):
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

def webcam_recorder_start():

            print(Fore.RED + "\nPress 'Esc' for exit" + Fore.WHITE)

            # Create an object to read camera video 
            cap = cv2.VideoCapture(0)

            # Check if camera opened successfully
            if (cap.isOpened() == False): 

                print(colorama.Fore.RED + "\n(!ERROR!) " + colorama.Fore.WHITE + "=" + colorama.Fore.GREEN + " (!Unable to open camera!)\n" + colorama.Fore.WHITE)

            # Set resolutions of frame.
            # convert from float to integer.
            frame_width = int(cap.get(3))
            frame_height = int(cap.get(4))

            # Create VideoWriter object.
            # and store the output in 'captured_video.avi' file.

            video_cod = cv2.VideoWriter_fourcc(*'XVID')
            video_output= cv2.VideoWriter('webcam_recording.avi',
                      video_cod,
                      10,
                      (frame_width,frame_height))

            while True:

                    ret, frame = cap.read()

                    if ret == True: 
                       
                          # Write the frame into the file 'captured_video.avi'
                          video_output.write(frame)

                          # Display the frame, saved in the file   
                          cv2.imshow('Webcam Recorder: ',frame)
                          # Set custom icon for the window
                          icon_path_2 = os.environ["OXDAN-DRAGON-PYTHON"] + "\\imports\\own\\my_dragon_ico.ico"  # Replace with the correct path to your .ico file
                          set_window_icon_2("Webcam Recorder: ", icon_path_2)
                        # Press x on keyboard to stop recording
                    if cv2.waitKey(27) >= 0:
                        
                        cap.release()
                        video_output.release()

                        cv2.destroyAllWindows() 

                        #os.system('cls')
 
                        imports.own.will_go_to_start.main()

                    # Break the loop
                    #else:
                    #    break  
                    
            # release video capture
            # and video write objects
            cap.release()
            video_output.release()

            # Closes all the frames
            cv2.destroyAllWindows() 

            #os.system('cls')
 
            imports.own.will_go_to_start.main()
