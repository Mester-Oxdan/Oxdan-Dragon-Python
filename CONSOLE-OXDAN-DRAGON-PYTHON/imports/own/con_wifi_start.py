import pywifi #import
from pywifi import const # const - это некоторые константы, установленные wifi, например, код состояния соответствует 4, сбой равен 0 и т. д.
import time
from colorama import Fore
import os
import imports.own.will_go_to_start

profile = pywifi.Profile()

def crack_4(password):

    while True:
            "" "Взломать Wi-Fi" ""
            wifi = pywifi.PyWiFi () # Реализуем объект
            # Получите первую сетевую карту
            iface= wifi.interfaces()[0]
                 # Отключить подключение сетевой карты
            iface.disconnect()
            time.sleep(2)
    
                 # Удалить все файлы конфигурации Wi-Fi (что-то вроде запрета точкам доступа Wi-Fi запоминать нашу информацию об инициализации Lei Shiyu)
            iface.remove_all_network_profiles()
    
                 # Создайте новый файл конфигурации Wi-Fi, укажите файл, имя Wi-Fi, пароль, метод кодирования и другие параметры конфигурации
                 # const.IFACE_DISCONNECTED фактически равно 4, 4 означает, что соединение успешно
            if iface.status() == const.IFACE_DISCONNECTED: 

                profile.auth = const.AUTH_ALG_OPEN
                         # алгоритм шифрования Wi-Fi
                profile.akm.append(const.AKM_TYPE_WPA2PSK)
                profile.cipher = const.CIPHER_TYPE_CCMP
                         # пароль Wi-Fi
                profile.key = password #password здесь пароль, переданный read_password ()

                         # Добавить новый файл конфигурации Wi-Fi
                new_profile = iface.add_network_profile(profile)

                         # Подключить Wi-Fi

                try:
        
                    iface.connect(new_profile)

                except:

                    print(Fore.RED + "\n(!ERROR!) " + Fore.WHITE + "=" + Fore.GREEN + " (!Wifi name was not found!)\n" + Fore.WHITE)
                    imports.own.will_go_to_start.main()

                time.sleep(4)
                if iface.status() == const.IFACE_CONNECTED:
                    print("\nConnection was " + Fore.GREEN + "successful!" + Fore.WHITE)
                    imports.own.will_go_to_start.main()
                else:
                    print(Fore.RED + "\n(!ERROR!) " + Fore.WHITE + "=" + Fore.GREEN + " (!Wifi password or ssid was wrong!)\n" + Fore.WHITE)
                    imports.own.will_go_to_start.main()

def con_wifi_start():

    print(Fore.RED + "Write 'esc' (for exit)")
    ferd = input(Fore.YELLOW + "Enter wifi name: " + Fore.WHITE)
    if ferd.lower() == "esc":
        imports.own.will_go_to_start.main()
    ferd_2 = input(Fore.YELLOW + "Enter wifi password: " + Fore.WHITE)
    if ferd_2.lower() == "esc":
        imports.own.will_go_to_start.main()
    try:
        
        profile.ssid = str(ferd)
        crack_4(ferd_2)

    except:

        print(Fore.RED + "\n(!ERROR!) " + Fore.WHITE + "=" + Fore.GREEN + " (!Wifi name was not found!)\n" + Fore.WHITE)
        imports.own.will_go_to_start.main()
