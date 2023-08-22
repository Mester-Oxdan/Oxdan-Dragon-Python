import imports.own.will_go_to_start
from tkinter import ttk, NSEW, NS
import tkinter as tk
import time
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import winsound
import os

class Clock():
            def __init__(self):
                
                self.root = tk.Tk()
                self.root.title("Timer!")
                self.style = ttk.Style()
                self.style.configure("BW.TLabel", font=(
                    'Helvetica', 25),  foreground="black")
                self.label = ttk.Label(text="--:--", style='BW.TLabel')
                self.label.grid(row=0, column=0, columnspan=3, sticky=NS)

                self._pomodoro_time_limit = 20 * 60
                self._pomodoro_starttime = time.time()
                self.start_button = ttk.Button(text='Start', command=self.start_timer)
                self.start_button.grid(row=2, column=2)
                self.progressbar = ttk.Progressbar()
                self.progressbar.grid(row=1, column=0, columnspan=3)

                self.time_input_label = ttk.Label(text="session length")
                self.time_input_label.grid(row=2, column=0)
                self.time_input_entry = ttk.Entry()
                self.time_input_entry.grid(row=2, column=1)

                self.time_input_entry.insert(
                    0, str(self.get_formatted_time(self._pomodoro_time_limit)))

            def update_clock(self):

                now = int(time.time() - self._pomodoro_starttime)
                # Остановка таймера при достижении лимита времени
                if now > self._pomodoro_time_limit:

                    self.root.after_cancel(self._timer_job)
                    devices = AudioUtilities.GetSpeakers()
                    interface = devices.Activate(
                       IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
                    volume = cast(interface, POINTER(IAudioEndpointVolume))
 
                    # Control volume
                    ##volume.SetMasterVolumeLevel(-0.0, None) #max
                    ##volume.SetMasterVolumeLevel(-5.0, None) #72%

                    volume.SetMute(0, None)
                    volume.SetMasterVolumeLevel(-10.0, None) #51%
                    frequency = 2500  # Set Frequency To 2500 Hertz
                    duration = 1000  # Set Duration To 1000 ms == 1 second
                    winsound.Beep(frequency, duration)

                    return

                self.label.configure(text=self.get_formatted_time(now),)
                # Запуск таймера
                self._timer_job = self.root.after(1000, self.update_clock)
                self.progressbar.step(self._progressbar_increment)

            def start_timer(self):
                import time
                try:
                    self._pomodoro_time_limit = self.parse_time_limit()
                except:
                    self.label.configure(
                        text='!Only integers!')
                    return
                self._pomodoro_starttime = time.time()
                self._progressbar_increment = 100 / self._pomodoro_time_limit
                self.progressbar['value'] = -self._progressbar_increment
                self.update_clock()

            def get_formatted_time(self, time_to_format: int):
                return f'{time_to_format // 60}:{time_to_format % 60}'

            def parse_time_limit(self):
                val = self.time_input_entry.get().strip()
                if ':' in val:
                    minuts, seconds = val.split(':')
                    return int(minuts) * 60 + int(seconds)
                else:
                    return int(val) * 60

def timer_start():

        app = Clock()
        app.root.iconbitmap(os.path.join(os.environ["OXDAN-DRAGON-PYTHON"],'my_dragon_ico.ico'))
        app.root.mainloop()
        imports.own.will_go_to_start.main()