from msvcrt import getch
import os
from colorama import *
import imports.own.will_go_to_start

def Encryption(plaintext, key_val):
    ciphertext = ''
    for i in range(len(plaintext)):
        special = plaintext[i]
        # Handling special characters
        if special == " ":
            ciphertext += ' '
        elif special.isalpha():
            # Encryption logic for letters
            new_special = special.lower()
            ciphertext += chr((ord(new_special) - ord('a') + key_val) % 26 + ord('a'))
        else:
            # Handle special characters
            ciphertext += special
    return ciphertext

def Decryption(ciphertext, key_val):
    plaintext = ''
    for i in range(len(ciphertext)):
        special = ciphertext[i]
        # Handling special characters
        if special == " ":
            plaintext += ' '
        elif special.isalpha():
            # Decryption logic for letters
            new_special = special.lower()
            plaintext += chr((ord(new_special) - ord('a') - key_val) % 26 + ord('a'))
        else:
            # Handle special characters
            plaintext += special
    return plaintext

def cuaser_cipher_start():

        while True:

            os.system('cls')
            print(Fore.RED + "\nEnter 'esc' (for exit)" + Fore.WHITE)
            choice = input(Fore.YELLOW + '(1) Encryption (2) Decryption: ' + Fore.WHITE)

            #choice = input()

            if imports.own.will_go_to_start.remove_098(choice.lower()) == "esc":

                imports.own.will_go_to_start.main()

            elif imports.own.will_go_to_start.remove_098(choice.lower()) == "1":

                    os.system('cls')
                    print(Fore.RED + "\nEnter 'esc' (for exit)" + Fore.WHITE)
                    sen = input(Fore.YELLOW + 'Enter text: ' + Fore.WHITE)
                    
                    if imports.own.will_go_to_start.remove_098(sen.lower()) == "esc":
                        imports.own.will_go_to_start.main()  
                        
                    else:
                        print(Fore.RED + "\nEnter 'esc' (for exit)" + Fore.WHITE)
                        key = int(input(Fore.YELLOW + 'Enter key: ' + Fore.WHITE))
                    
                        if imports.own.will_go_to_start.remove_098(str(key).lower()) == "esc":
                            imports.own.will_go_to_start.main()
                        
                        else:
                            print(" ")
                            #print(24 * '*')
                            print(Fore.YELLOW + "Encripted message: " + Fore.WHITE + Encryption(sen, key))
                            #print(24 * '*')
                            #print('\nSpecial symbols (!,# etc and numbers) are deleted...')
                            choice_2 = input(Fore.YELLOW + "\nContinue?" + Fore.WHITE + " [" + Fore.GREEN + "yes" + Fore.WHITE + "/" + Fore.RED + "no" + Fore.WHITE + "]")

                            

                            if imports.own.will_go_to_start.remove_098(choice_2.lower()) == "no" or imports.own.will_go_to_start.remove_098(choice_2.lower()) == "n":

                                os.system('cls')
                                print(" ")
                                imports.own.will_go_to_start.main()

                            elif imports.own.will_go_to_start.remove_098(choice_2.lower()) == "esc":

                                imports.own.will_go_to_start.main()

                            else:
                        
                                cuaser_cipher_start()

            elif imports.own.will_go_to_start.remove_098(choice.lower()) == "2":

                    os.system('cls')
                    print(Fore.RED + "\nEnter 'esc' (for exit)" + Fore.WHITE)
                    csen = input(Fore.YELLOW + 'Enter text: ' + Fore.WHITE)
                    
                    if imports.own.will_go_to_start.remove_098(csen.lower()) == "esc":
                         imports.own.will_go_to_start.main()

                    else:
                        print(Fore.RED + "\nEnter 'esc' (for exit)" + Fore.WHITE)
                        key = int(input(Fore.YELLOW + 'Enter key: ' + Fore.WHITE))
                        if imports.own.will_go_to_start.remove_098(str(key).lower()) == "esc":
                             imports.own.will_go_to_start.main()
                           
                        else:
                            print(" ")
                            #print(24 * '*')
                            print(Fore.YELLOW + "Decripted message: " + Fore.WHITE + Decryption(csen, key))
                            #print(24 * '*')
                            #print('\nSpecial symbols (!,# etc and numbers) are deleted..')
                            choice_3 = input(Fore.YELLOW + "\nContinue?" + Fore.WHITE + " [" + Fore.GREEN + "yes" + Fore.WHITE + "/" + Fore.RED + "no" + Fore.WHITE + "]")

                            #con = ord(getch())

                            if imports.own.will_go_to_start.remove_098(choice_3.lower()) == "no" or imports.own.will_go_to_start.remove_098(choice_3.lower()) == "n":

                                os.system('cls')
                                print(" ")
                                imports.own.will_go_to_start.main()

                            elif imports.own.will_go_to_start.remove_098(choice_3.lower()) == "esc":

                                imports.own.will_go_to_start.main()

                            else:
                        
                                if imports.own.will_go_to_start.remove_098(choice_3.lower()) == "esc":

                                    imports.own.will_go_to_start.main()

                                else:
                                     
                                    cuaser_cipher_start()
            else:
                    
                    cuaser_cipher_start()