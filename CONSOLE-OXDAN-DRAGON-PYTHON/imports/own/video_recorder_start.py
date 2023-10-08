import cv2
import imports.own.will_go_to_start
from colorama import *
import colorama

def webcam_recorder_start():

            print(Fore.RED + "\nPress 'Esc' for exit" + Fore.WHITE)

            # Create an object to read camera video 
            cap = cv2.VideoCapture(0)

            # Check if camera opened successfully
            if (cap.isOpened() == False): 

                print(colorama.Fore.RED + "\n(!ERROR!) " + colorama.Fore.WHITE + "=" + colorama.Fore.GREEN + " (!Camera unable to open!)\n" + colorama.Fore.WHITE)

            # Set resolutions of frame.
            # convert from float to integer.
            frame_width = int(cap.get(3))
            frame_height = int(cap.get(4))

            # Create VideoWriter object.
            # and store the output in 'captured_video.avi' file.

            video_cod = cv2.VideoWriter_fourcc(*'XVID')
            video_output= cv2.VideoWriter('output_recorded_video.avi',
                      video_cod,
                      10,
                      (frame_width,frame_height))

            while True:

                    ret, frame = cap.read()

                    if ret == True: 
                       
                          # Write the frame into the file 'captured_video.avi'
                          video_output.write(frame)

                          # Display the frame, saved in the file   
                          cv2.imshow('Video: ',frame)

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
