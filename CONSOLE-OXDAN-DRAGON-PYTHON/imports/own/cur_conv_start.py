import tkinter
from tkinter import ttk
#from tkinter import tk
import tkinter
import imports.own.will_go_to_start
import requests
import datetime as dt
import os

def cur_conv_start():

          # Converting stuff
          
          class CurrencyConverter:

            def __init__(self,url):
                 #self.url = 'https://api.exchangerate.host/latest'
                 self.response = requests.get(url)
                 self.data = self.response.json()
                 self.rates = self.data.get('rates')

            def convert(self, amount, base_currency, des_currency):
               if base_currency != 'EUR':
                 amount = amount/self.rates[base_currency]

                 # Limiting the result to 2 decimal places
                 amount = round(amount*self.rates[des_currency], 2)
                 # Add comma every 3 numbers
                 amount = '{:,}'.format(amount)
                 return amount
        
          import tkinter as tk
          class Main(tk.Tk):

            def __init__(self, converter):
                
                tk.Tk.__init__(self)
                self.title('Currency Converter')
                self.geometry('400x400')
                self.iconbitmap(os.path.join(os.environ["OXDAN-DRAGON-PYTHON"], r'imports/own/my_dragon_ico.ico'))
                self.config(bg='#3A3B3C')
                self.CurrencyConverter = converter

                # Create title label
                self.title_label = tkinter.Label(self, text='Currency Converter', bg='#3A3B3C', fg='white', font=('franklin gothic medium', 20), relief='sunken')
                self.title_label.place(x=200, y=35, anchor='center')

                # Create date label
                self.date_label = tkinter.Label(self, text=f'{dt.datetime.now():%A, %B %d, %Y}', bg='#3A3B3C', fg='white', font=('calibri', 10))
                self.date_label.place(x=0, y=400, anchor='sw')

                # Create version label
                self.version_label = tkinter.Label(self, text='v1.0', bg='#3A3B3C', fg='white', font=('calibri', 10))
                self.version_label.place(x=400, y=400, anchor='se')

                # Create amount label
                self.amount_label = tkinter.Label(self, text='Input Amount: ', bg='#3A3B3C', fg='white', font=('franklin gothic book', 15))
                self.amount_label.place(x=200, y=80, anchor='center')

                # Create amount entry box
                self.amount_entry = tkinter.Entry(self)
                self.amount_entry.config(width=25)
                self.amount_entry.place(x=200, y=110, anchor='center')

                # Create 'from' label
                self.base_currency_label = tkinter.Label(self, text='From: ', bg='#3A3B3C', fg='white', font=('franklin gothic book', 15))
                self.base_currency_label.place(x=200, y=140, anchor='center')

                # Create 'to' label
                self.destination_currency_label = tkinter.Label(self, text='To: ', bg='#3A3B3C', fg='white', font=('franklin gothic book', 15))
                self.destination_currency_label.place(x=200, y=200, anchor='center')

                # Create dropdown menus
                self.currency_variable1 = tkinter.StringVar(self)
                self.currency_variable2 = tkinter.StringVar(self)
                self.currency_variable1.set('USD')
                self.currency_variable2.set('RUB')

                self.currency_combobox1 = ttk.Combobox(self, width=20, textvariable=self.currency_variable1, values=list(self.CurrencyConverter.rates.keys()), state='readonly')
                self.currency_combobox1.place(x=200, y=170, anchor='center')

                self.currency_combobox2 = ttk.Combobox(self, width=20, textvariable=self.currency_variable2, values=list(self.CurrencyConverter.rates.keys()), state='readonly')
                self.currency_combobox2.place(x=200, y=230, anchor='center')   

                self.conv_btn = ttk.Button( self, text="Convert", command=self.conv_val, width=20 )
                self.conv_btn.place(x=200, y=260, anchor='center')

                self.out_box = tkinter.Entry(self, width=20)
                self.out_box.place(x=200, y=300, anchor='center' )



            def conv_val(self):
                val1 = float(self.amount_entry.get())
                cur1 = self.currency_combobox1.get()
                cur2 = self.currency_combobox2.get()
                val2 = self.CurrencyConverter.convert(val1,cur1,cur2)
                self.out_box.insert(tkinter.END,str(val2))
                self.out_box.pack()
                self.out_box.place(x=200, y=300, anchor='center' )


          
          converter = CurrencyConverter('https://api.exchangerate.host/latest')
          Main(converter)
          tkinter.mainloop()

          imports.own.will_go_to_start.main()