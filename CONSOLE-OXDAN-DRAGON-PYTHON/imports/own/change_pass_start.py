import msvcrt
import os
from colorama import Fore
import builtins
import hashlib
import imports.own.start_start
import imports.own.will_go_to_start

def change_pass_start():
    os.system("cls")
    print("                                                              ")
    print("                                                              ")
    print("                                                              ")
    print("                                                              ")
    print("                                                              ")
    print("                                                              ")
    print("                                                              ")
    print("                                                              ")
    print("                                                              ")
    print("                                                              ")
    print("                                                              ")
    print(Fore.RED + "                                                          Enter 'esc' (for exit)")
    print(Fore.RED + "                                                           CHANGE PASSWORD:" + Fore.WHITE)

    email = input(Fore.YELLOW + "\n                                                              USERNAME: " + Fore.RED)
    if imports.own.will_go_to_start.remove_098(email.lower()) == "esc":
        imports.own.start_start.start_start()

    pwd = input(Fore.YELLOW + "                                                       CURRENT PASSWORD: " + Fore.RED)
    if imports.own.will_go_to_start.remove_098(pwd.lower()) == "esc":
        imports.own.start_start.start_start()

    enc = pwd.encode()
    current_hash = hashlib.md5(enc).hexdigest()

    file_path = os.path.join(os.environ["OXDAN-DRAGON-PYTHON"], "imports/own/login_data_base.txt")
    lines = []
    user_found = False
    password_correct = False

    try:
        with builtins.open(file_path, "r") as f:
            lines = f.readlines()

        for i, line in enumerate(lines):
            tokens = line.strip().split(" ")
            if len(tokens) < 2:
                continue

            stored_email = tokens[0].strip()
            stored_pwd = tokens[1].strip()

            if email == stored_email:
                user_found = True
                if current_hash == stored_pwd:
                    password_correct = True
                    break
                else:
                    break

        if not user_found:
            print(Fore.RED + "\n                                                      (!ERROR!) " + Fore.WHITE + "= " + Fore.GREEN + "(!Username not found!)\n" + Fore.WHITE)
            msvcrt.getch()
            imports.own.start_start.start_start()

        if not password_correct:
            print(Fore.RED + "\n                                                      (!ERROR!) " + Fore.WHITE + "= " + Fore.GREEN + "(!Incorrect password!)\n" + Fore.WHITE)
            msvcrt.getch()
            imports.own.start_start.start_start()

        new_pwd = input(Fore.YELLOW + "                                                         NEW PASSWORD: " + Fore.RED)
        if imports.own.will_go_to_start.remove_098(new_pwd.lower()) == "esc":
            imports.own.start_start.start_start()

        repeat_pwd = input(Fore.YELLOW + "                                                   REPEAT NEW PASSWORD: " + Fore.RED)
        if imports.own.will_go_to_start.remove_098(repeat_pwd.lower()) == "esc":
            imports.own.start_start.start_start()

        if new_pwd != repeat_pwd:
            print(Fore.RED + "\n                                                      (!ERROR!) " + Fore.WHITE + "= " + Fore.GREEN + "(!Passwords do not match!)\n" + Fore.WHITE)
            msvcrt.getch()
            imports.own.start_start.start_start()

        new_hash = hashlib.md5(new_pwd.encode()).hexdigest()

        # Update password in file
        for i, line in enumerate(lines):
            tokens = line.strip().split(" ")
            if len(tokens) >= 2 and tokens[0].strip() == email:
                lines[i] = email + " " + new_hash + "\n"
                break

        with builtins.open(file_path, "w") as f:
            f.writelines(lines)

        print(Fore.GREEN + "\n                                                    !PASSWORD CHANGED SUCCESSFULLY!")
        print(Fore.YELLOW)
        msvcrt.getch()
        imports.own.start_start.start_start()

    except Exception as e:
        print(Fore.RED + "\n                                                      (!ERROR!) " + Fore.WHITE + "= " + Fore.GREEN + f"(!Unexpected Error: {e}!)\n" + Fore.WHITE)
        msvcrt.getch()
        imports.own.start_start.start_start()
