import imports.own.start_start
import keyboard
import imports.own.will_go_to_start
import imports.own.login
import imports.own.signup
import imports.own.instructions
import colorama
from imports.own.del_account_start import del_account_start
from imports.own.my_accounts_start import my_accounts_start
from imports.own.change_pass_start import change_pass_start

def Accounts():

            if imports.own.will_go_to_start.x.lower() == "login" or imports.own.will_go_to_start.x.lower() == "signin": # login (+)

                 try:

                       imports.own.login.login()

                 except:

                        imports.own.will_go_to_start.main()

            if imports.own.will_go_to_start.x.lower() == "registration" or imports.own.will_go_to_start.x.lower() == "signup": # registration (+)

                    try:

                       imports.own.signup.signup()

                    except:

                        imports.own.will_go_to_start.main()

            if imports.own.will_go_to_start.x.lower() == "change_pass": # change_pass (+)

                    try:

                       change_pass_start()

                    except:

                        imports.own.will_go_to_start.main()


            if imports.own.will_go_to_start.x.lower() == "instructions": # instructions (+)

                    try:

                       imports.own.instructions.instructions()

                    except:

                        imports.own.will_go_to_start.main()

            elif imports.own.will_go_to_start.x.lower() == "del_account": # del_account (+)
            
                try:

                    del_account_start()
                
                except:

                    print(colorama.Fore.RED + "\n(!ERROR!) " + colorama.Fore.WHITE + "=" + colorama.Fore.GREEN + " (!Account did not found!)\n" + colorama.Fore.WHITE)
                    imports.own.will_go_to_start.main()
                    
            if imports.own.will_go_to_start.x.lower() == "my_accounts": # my_accounts (+)

                try:

                    #keyboard.press(72)
                    #imports.own.start_start.start_start()
                    my_accounts_start() 

                except:

                    imports.own.will_go_to_start.main()

            if imports.own.will_go_to_start.x.lower() == "logout": # logout (+)

                try:

                    keyboard.press(72)
                    imports.own.start_start.start_start()

                except:

                    imports.own.will_go_to_start.main()
