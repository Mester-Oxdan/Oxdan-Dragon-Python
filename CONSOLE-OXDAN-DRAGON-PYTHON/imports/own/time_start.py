import tkinter as tk
import imports.own.will_go_to_start
import os
import keyboard
import imports.own.start_start
from time import strftime

def time_start():

    while True:

                

                my_w = tk.Tk()
                my_w.geometry("518x335")
                my_w.title("Time")

                

                def my_time():
                    time_string = strftime('%H:%M:%S %p \n %A \n %x')
                    l1.config(text=time_string)
                    l1.after(1000,my_time) # time delay of 1000 milliseconds 

                my_font=('times',52,'bold') # display size and style
                my_w.iconbitmap(os.path.join(os.environ["OXDAN-DRAGON-PYTHON"] + "\imports\own","my_dragon_ico.ico"))
                

                l1=tk.Label(my_w,font=my_font,bg='yellow')
                l1.grid(row=1,column=1,padx=5,pady=25)
                my_time()
                my_w.mainloop()
                imports.own.will_go_to_start.main()
 