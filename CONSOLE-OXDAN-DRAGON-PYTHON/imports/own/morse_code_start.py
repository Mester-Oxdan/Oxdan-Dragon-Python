from msvcrt import getch
import os
from colorama import Fore
import colorama
import imports.own.will_go_to_start

ENGLISH_TO_MORSE = {
    'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.', 'g': '--.', 'h': '....',
    'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---', 'p': '.--.',
    'q': '--.-', 'r': '.-.', 's': '...', 't': '-', 'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-',
    'y': '-.--', 'z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    '.': '.-.-.-', ',': '--..--', '?': '..--..', '\'': '.----.', '!': '-.-.--', '/': '-..-.',
    '(': '-.--.', ')': '-.--.-', '&': '.-...', ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.',
    '-': '-....-', '_': '..--.-', '"': '.-..-.', '$': '...-..-', '@': '.--.-.', ' ': ' '
}

# Generate MORSE_TO_ENGLISH from ENGLISH_TO_MORSE
MORSE_TO_ENGLISH = {value: key for key, value in ENGLISH_TO_MORSE.items()}

def english_to_morse(message):
    morse = []  # Will contain Morse versions of letters
    for char in message:
        if char in ENGLISH_TO_MORSE:
           morse.append(ENGLISH_TO_MORSE[char])
    return " ".join(morse)

def morse_to_english(message):
    words = message.split("   ")  # Split the message into words using three spaces as the delimiter
    english_message = []

    for word in words:
        letters = word.split(" ")  # Split each word into letters
        english_word = []

        for code in letters:
            if code in MORSE_TO_ENGLISH:
                english_word.append(MORSE_TO_ENGLISH[code])

        english_message.append("".join(english_word))  # Join the letters to form the word

    return " ".join(english_message)  # Join the words to form the full message


def morse_code_start():

        os.system('cls')

        while True:

            print(Fore.RED + "\nEnter 'esc' (for exit)")
            choice_4 = input(Fore.YELLOW + "(1) Morse to English (2) English to Morse: " + Fore.WHITE)

            #key = ord(getch())

            if imports.own.will_go_to_start.remove_098(choice_4.lower()) == "1": # 1

               os.system("cls")
               print(Fore.RED + "\nEnter 'esc' (for exit)")
               morse = input(Fore.YELLOW + "Enter text to decipher: " + Fore.WHITE)
               english = morse_to_english(morse)
               #print(Fore.YELLOW + " \n!English version! " + Fore.WHITE)
               print(Fore.YELLOW + "Decrypted message: " + Fore.WHITE + english)
               getch()
               morse_code_start()

            elif imports.own.will_go_to_start.remove_098(choice_4.lower()) == "2":

                os.system("cls")
                print(Fore.RED + "\nEnter 'esc' (for exit)")
                english = input(Fore.YELLOW + "Enter text to cipher: " + Fore.WHITE).upper()
                morse = english_to_morse(english.lower())
                #print(Fore.YELLOW + " \n!Morse Code version! " + Fore.WHITE)
                print(Fore.YELLOW + "Encrypted message: " + Fore.WHITE + morse)
                getch()
                morse_code_start()

            elif imports.own.will_go_to_start.remove_098(choice_4.lower()) == "esc":
            
                imports.own.will_go_to_start.main()

            else:
                
                if imports.own.will_go_to_start.remove_098(choice_4.lower()) == "esc":
            
                    imports.own.will_go_to_start.main()
                
                else:
                    
                    morse_code_start()
