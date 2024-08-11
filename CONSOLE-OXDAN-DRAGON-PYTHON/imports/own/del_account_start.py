import re
import imports.own.will_go_to_start
import colorama
import hashlib
import builtins
from colorama import Fore
import os

def del_account_start():

                print(Fore.RED + "\nEnter 'esc' (for exit)" + Fore.WHITE)

                wrote_stored_email = input(Fore.YELLOW + "Enter account name: " + Fore.WHITE)

                if imports.own.will_go_to_start.remove_098(wrote_stored_email.lower()) == "esc":

                    imports.own.will_go_to_start.main()

                wrote_stored_pwd = input(Fore.YELLOW + "\nEnter account password: " + Fore.WHITE)

                if imports.own.will_go_to_start.remove_098(wrote_stored_pwd.lower()) == "esc":

                    imports.own.will_go_to_start.main()

                del_account_bool = False

                auth = wrote_stored_pwd.encode()
                wrote_stored_pwd_tran = hashlib.md5(auth).hexdigest()

                with builtins.open(os.environ["OXDAN-DRAGON-PYTHON"] + "/imports/own/login_data_base.txt", "r") as f:

                    for line in f:

                          tokens = line.split(" ")

                          if (len(tokens) < 2 ):

                              continue

                          stored_email = tokens[0].strip()
                          stored_pwd = tokens[1].strip()

                          if wrote_stored_pwd_tran == stored_pwd and wrote_stored_email != stored_email:

                             del_account_bool = True
                             print(colorama.Fore.RED + "(!ERROR!) " + colorama.Fore.WHITE + "=" + colorama.Fore.GREEN + " (!Wrong username!)\n" + colorama.Fore.WHITE)
                             imports.own.will_go_to_start.main()

                          elif wrote_stored_email == stored_email and wrote_stored_pwd_tran != stored_pwd:

                             del_account_bool = True
                             print(colorama.Fore.RED + "(!ERROR!) " + colorama.Fore.WHITE + "=" + colorama.Fore.GREEN + " (!Wrong password!)\n" + colorama.Fore.WHITE)
                             imports.own.will_go_to_start.main()

                          elif wrote_stored_email == stored_email and wrote_stored_pwd_tran == stored_pwd:

                              del_account_bool = True

                              with open(os.environ["OXDAN-DRAGON-PYTHON"] + "/imports/own/login_data_base.txt", 'r') as f:

                                    text = f.read()
                                    text_without_special_email = re.sub(wrote_stored_email + " " + wrote_stored_pwd_tran, '', text)

                              with open(os.environ["OXDAN-DRAGON-PYTHON"] + "/imports/own/login_data_base.txt", 'w') as f:

                                    f.write(text_without_special_email)

                          else:

                              continue

                if del_account_bool == False:

                    print(colorama.Fore.RED + "\n(!ERROR!) " + colorama.Fore.WHITE + "=" + colorama.Fore.GREEN + " (!Account did not found!)\n" + colorama.Fore.WHITE)
                    imports.own.will_go_to_start.main()

                else:
                    print(colorama.Fore.GREEN + "\n(!SUCCESS!) " + colorama.Fore.WHITE + "=" + colorama.Fore.YELLOW + " (!Account deleted successfully!)\n" + colorama.Fore.WHITE)
                    imports.own.will_go_to_start.main()