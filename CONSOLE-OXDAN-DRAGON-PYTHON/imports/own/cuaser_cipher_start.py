from msvcrt import getch
import os
from colorama import *
import imports.own.will_go_to_start

def Encryption(plaintext, key_val):

            ciphertext = ''
            for i in range(len(plaintext)):
                special = plaintext[i]
                new_special = special.lower()
                if new_special == " ":
                    ciphertext += ' '
                elif special.isalpha():
                    ciphertext += chr((ord(new_special) + key_val - 97) % 26 + 97)

            return ciphertext

def Decryption(ciphertext, key_val):

            plaintext = ''
            for i in range(len(ciphertext)):
                special = ciphertext[i]
                new_special = special.lower()
                if new_special == " ":
                    plaintext += ' '
                elif special.isalpha():
                    plaintext += chr((ord(new_special) - key_val - 97) % 26 + 97)
            return plaintext

def cuaser_cipher_start():

        while True:

            os.system('cls')
            print(Fore.RED + "\nPress Esc (for exit)")
            print(Fore.YELLOW + '(1) Encryption (2) Decryption: ' + Fore.WHITE)

            choice = ord(getch())

            if choice == 27:

                imports.own.will_go_to_start.main()

            elif choice == 49:

                    os.system('cls')
                    sen = input(Fore.YELLOW + 'Enter text: ' + Fore.WHITE)
                    key = int(input(Fore.YELLOW + 'Enter key: ' + Fore.WHITE))
                    print(" ")
                    print(24 * '*')
                    print(f'* Encrypt text --> {Encryption(sen, key)} *')
                    print(24 * '*')
                    print('\nSpecial symbols (!,# etc and numbers) are deleted...')
                    print(Fore.YELLOW + "\nContinue?" + Fore.WHITE + " [" + Fore.GREEN + "yes" + Fore.WHITE + "/" + Fore.RED + "no" + Fore.WHITE + "]")

                    con = ord(getch())

                    if con == 110:

                        os.system('cls')
                        print(" ")
                        imports.own.will_go_to_start.main()

                    elif choice == 27:

                        imports.own.will_go_to_start.main()

                    else:
                        
                        cuaser_cipher_start()

            elif choice == 50:

                    os.system('cls')
                    csen = input(Fore.YELLOW + 'Enter text: ' + Fore.WHITE)
                    key = int(input(Fore.YELLOW + 'Enter key: ' + Fore.WHITE))
                    print(" ")
                    print(24 * '*')
                    print(f'* Decipher text --> {Decryption(csen, key)} *')
                    print(24 * '*')
                    print('\nSpecial symbols (!,# etc and numbers) are deleted..')
                    print(Fore.YELLOW + "\nContinue?" + Fore.WHITE + " [" + Fore.GREEN + "yes" + Fore.WHITE + "/" + Fore.RED + "no" + Fore.WHITE + "]")

                    con = ord(getch())

                    if con == 110:

                        os.system('cls')
                        print(" ")
                        imports.own.will_go_to_start.main()

                    elif con == 27:

                        imports.own.will_go_to_start.main()

                    else:
                        
                        if con == 27:

                            imports.own.will_go_to_start.main()

                        cuaser_cipher_start()
            else:
                    
                    cuaser_cipher_start()