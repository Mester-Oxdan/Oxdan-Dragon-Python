import os
import tkinter
import imports.own.will_go_to_start
from tkcalendar import Calendar

def calendar_start():

        # Create Object
        root = tkinter.Tk()
        root.title("Calendar")
        root.iconbitmap(os.path.join(os.environ["OXDAN-DRAGON-PYTHON"],'imports/own/my_dragon_ico.ico'))
        # Set geometry
        root.geometry("400x400")
 
        # Add Calendar
        
        cal = Calendar(root, selectmode = 'day',
               year = 2025, month = 1,
               day = 7)
 
        cal.pack(pady = 20)
 
        def grad_date():
            date.config(text = "Selected Date is: " + cal.get_date())
 
        # Add tkinter.Button\ and Label
        tkinter.Button(root, text = "Get Date",
            command = grad_date).pack(pady = 20)
 
        date = tkinter.Label(root, text = "")
        date.pack(pady = 20)
 
        #root.iconbitmap(os.path.join(os.environ["OXDAN-DRAGON-PYTHON"],'imports/own/dragon.ico'))
        # Execute Tkinter
        def on_escape(event):
                root.destroy()
                imports.own.will_go_to_start.main()
                
        root.bind('<Escape>', on_escape)
        root.mainloop()

        imports.own.will_go_to_start.main()