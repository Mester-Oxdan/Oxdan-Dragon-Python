import psutil
import imports.own.will_go_to_start
from colorama import Fore

def energy_start():
  
            # function returning time in hh:mm:ss
            def convertTime(seconds):
                minutes, seconds = divmod(seconds, 60)
                hours, minutes = divmod(minutes, 60)
                return "%d:%02d:%02d" % (hours, minutes, seconds)
  
            # returns a tuple
            battery = psutil.sensors_battery()

            if battery.percent < 50:

                print(Fore.WHITE + "\nBattery percentage:" + Fore.RED, battery.percent)

            if battery.percent > 50:

                print(Fore.WHITE + "\nBattery percentage:" + Fore.GREEN, battery.percent)

            if battery.power_plugged == True:

                print(Fore.WHITE + "Power plugged in: " + Fore.GREEN + "yes")

            if battery.power_plugged == False:

                print(Fore.WHITE + "Power plugged in: " + Fore.RED + "no")
  
            # converting seconds to hh:mm:ss
            print(Fore.WHITE + "Battery left:", convertTime(battery.secsleft))
            imports.own.will_go_to_start.main()