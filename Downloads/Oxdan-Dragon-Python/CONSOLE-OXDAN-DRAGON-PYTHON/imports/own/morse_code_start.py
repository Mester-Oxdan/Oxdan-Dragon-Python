from msvcrt import getch
import os
from colorama import Fore
import colorama
import imports.own.will_go_to_start

ENGLISH_TO_MORSE = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
                    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
                    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
                    'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
                    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.'}

# Generate MORSE_TO_ENGLISH from ENGLISH_TO_MORSE
MORSE_TO_ENGLISH = {}
for key, value in ENGLISH_TO_MORSE.items():
    MORSE_TO_ENGLISH[value] = key

def english_to_morse(message):
    morse = []  # Will contain Morse versions of letters
    for char in message:
        if char in ENGLISH_TO_MORSE:
           morse.append(ENGLISH_TO_MORSE[char])
    return " ".join(morse)

def morse_to_english(message):
    message = message.split(" ")
    english = []  # Will contain English versions of letters
    for code in message:
        if code in MORSE_TO_ENGLISH:
            english.append(MORSE_TO_ENGLISH[code])
    return " ".join(english)

def morse_code_start():

        os.system('cls')

        while True:

            print(Fore.RED + "\nPress Esc (for exit)")
            print(Fore.YELLOW + "(1) Morse to English (2) English to Morse: " + Fore.WHITE)

            key = ord(getch())

            if key == 49: # 1

               os.system("cls")
               morse = input(Fore.YELLOW + "Enter Morse code (with space after each code): " + Fore.WHITE)
               english = morse_to_english(morse)
               print(Fore.YELLOW + " \n!English version! " + Fore.WHITE)
               print(" " + english)
               getch()
               morse_code_start()

            elif key == 50:

                os.system("cls")

                english = input(Fore.YELLOW + "Enter English text: " + Fore.WHITE).upper()
                morse = english_to_morse(english)
                print(Fore.YELLOW + " \n!Morse Code version! " + Fore.WHITE)
                print(" " + morse)
                getch()
                morse_code_start()

            elif key == 27:
            
                imports.own.will_go_to_start.main()

            else:
                
                if key == 27:
            
                    imports.own.will_go_to_start.main()

                morse_code_start()
