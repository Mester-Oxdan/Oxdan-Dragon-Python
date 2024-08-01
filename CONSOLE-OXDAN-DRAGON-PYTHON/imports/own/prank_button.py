from tkinter import *
from tkinter import messagebox
import random
from colorama import Fore
import os
import imports.own.will_go_to_start

def prank_button_no():

    os.system("cls")

    enter_question = input(Fore.YELLOW + "Enter main question (space = '_'): " + Fore.WHITE)

    resp_no = input(Fore.YELLOW + "\nEnter response for button 'yes' (space = '_'): " + Fore.WHITE)

    root = Tk()

    root.iconbitmap(os.path.join(os.environ["OXDAN-DRAGON-PYTHON"],'imports/own/my_dragon_ico.ico'))

    def no(event):

        btnNo.place(x=random.randint(0, 500), y=random.randint(0, 500))

    def yes():

        messageboxid_no = messagebox.showinfo("Response: ", resp_no)
        
        if messageboxid_no == True:

            os.system(r"start " + os.path.join(os.environ["OXDAN-DRAGON-PYTHON"]) + "/CONSOLE_OXDAN_DRAGON_PYTHON.py")
            quit(0)

        else:
            
            os.system(r"start " + os.path.join(os.environ["OXDAN-DRAGON-PYTHON"]) + "/CONSOLE_OXDAN_DRAGON_PYTHON.py")
            quit(0)

    def disable_event():
       pass

    root.geometry('600x600')
    root.title(enter_question)
    root.resizable(width=False,height=False)
    root['bg'] = 'white'

    label = Label(root, text=enter_question, font='Arial 20 bold', bg='white').pack()
    btnYes = Button(root, text='Yes', font='Arial 20 bold', command=yes)
    btnYes.place(x=170, y=100)
    btnNo = Button(root, text='No', font='Arial 20 bold')
    btnNo.place(x=350, y=100)
    btnNo.bind('<Enter>', no)

    if imports.own.will_go_to_start.yes_or_no == True:

        root.protocol("WM_DELETE_WINDOW", disable_event)

    if imports.own.will_go_to_start.yes_or_no == False:

        os.system(r"start " + os.path.join(os.environ["OXDAN-DRAGON-PYTHON"]) + "/CONSOLE_OXDAN_DRAGON_PYTHON.py")
        quit(0)

    root.mainloop()

def prank_button_yes():

    os.system("cls")

    enter_question = input(Fore.YELLOW + "Enter main question (space = '_'): " + Fore.WHITE)

    resp_yes = input(Fore.YELLOW + "\nEnter response for button 'no' (space = '_'): " + Fore.WHITE)

    root = Tk()

    root.iconbitmap(os.path.join(os.environ["OXDAN-DRAGON-PYTHON"], 'imports/own/my_dragon_ico.ico'))

    def no(event):

        btnNo.place(x=random.randint(0, 500), y=random.randint(0, 500))

    def yes():

        messageboxid_yes = messagebox.showinfo("Response: ", resp_yes)

        if messageboxid_yes == True:

            os.system(r"start " + os.path.join(os.environ["OXDAN-DRAGON-PYTHON"]) + "/CONSOLE_OXDAN_DRAGON_PYTHON.py")
            quit(0)

        else:

            os.system(r"start " + os.path.join(os.environ["OXDAN-DRAGON-PYTHON"]) + "/CONSOLE_OXDAN_DRAGON_PYTHON.py")
            quit(0)

    def disable_event():
       pass

    root.geometry('600x600')
    root.title(enter_question)
    root.resizable(width=False,height=False)
    root['bg'] = 'white'

    label = Label(root, text=enter_question, font='Arial 20 bold', bg='white').pack()
    btnYes = Button(root, text='No', font='Arial 20 bold', command=yes)
    btnYes.place(x=170, y=100)
    btnNo = Button(root, text='Yes', font='Arial 20 bold')
    btnNo.place(x=350, y=100)
    btnNo.bind('<Enter>', no)
    
    if imports.own.will_go_to_start.yes_or_no == True:

        root.protocol("WM_DELETE_WINDOW", disable_event)

    if imports.own.will_go_to_start.yes_or_no == False:

        os.system(r"start " + os.path.join(os.environ["OXDAN-DRAGON-PYTHON"] + "/CONSOLE_OXDAN_DRAGON_PYTHON.py"))
        quit(0)

    root.mainloop()