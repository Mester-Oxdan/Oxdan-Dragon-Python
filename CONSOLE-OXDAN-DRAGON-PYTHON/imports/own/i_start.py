import os
import ctypes
import imports.own.will_go_to_start

def i_start():

            try:
                is_admin = os.getuid() == 0
            except AttributeError:
                is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0

            if is_admin == False:
                print(" ")
                print("You are: 'User'")

            elif is_admin == True:
                print(" ")
                print("You are: 'Super User/Admin'")

            imports.own.will_go_to_start.main()