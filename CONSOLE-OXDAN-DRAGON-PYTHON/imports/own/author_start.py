import os
from time import sleep
from colorama import Fore
import imports.own.will_go_to_start
from pydub import AudioSegment
from pydub.playback import play

def author_start():

        os.system("cls")
        os.system("MODE CON:COLS=183 LINES=23")
        print("                                                                                                                                                                                       ")
        sleep(0.01)
        print(Fore.YELLOW + "        @@@BY!^:::^!YB@@@         :!!!~           ^!!!^       @J!!!!!!!!!77J5G&@                  @&###&@                Y@@@@@@P           G@@@@Y          @GYYYYYYYY555PB@           ")
        sleep(0.01)
        print("      @@@G~           ~G@@@        J&@@G^        Y&@@P^       @~              :7B@               @5.....Y@               Y@@    @B^         G@@@@Y          @7             ^5@         ")
        sleep(0.01)
        print("     @@@5    :JPGPJ:    5@@@        ^P@@&J     !#@@#!         @!    5GGGPPJ!     Y@             @B.      G@              Y@@@  @@@#~        G@@@@Y          @P      :7^      P@        ")
        sleep(0.01)
        print("    @@@&    ^&     &^    &@@@         7#@@B~ :P@@@Y           @!   .#       B^    P@           @&^   :   :&@             Y@@@@&@@@@@7       G@@@@Y           @:     7@&.     ?@        ")
        sleep(0.01)
        print("    @@@&    ^&     &^    &@@@          :5@@@P#@@B~            @!   .#        G    ~@          @@7   :B:   !@@            Y@@@@G!&@@@@J      G@@@@Y           @:     7@@:     ?@        ")
        sleep(0.01)
        print("     @@@5    :JPGPJ:    5@@@             !&@@@@J              @!   .#        &    ^@         @@5    P@5    Y@@           Y@@@@G ~#@@@@Y     G@@@@Y           @:     ^Y!      5@        ")
        sleep(0.01)
        print("      @@@G~           ~G@@@             ^P@@@@@P^             @!   .#        B    ~@        @@B.   ?@@@?    G@@          Y@@@@G  :B@@@@P    G@@@@Y           @:             ?@         ")
        sleep(0.01)
        print(Fore.RED + "        @@@BY!^:::^!YB@@@              ?&@@G!G@@&?            @!   .#       #~    P@       @@&^    !777!    :&@@         Y@@@@G    P@@@@B:  G@@@@Y           @:     ^?77?J5B@          ")
        sleep(0.01)
        print("                                     ~G@@&?   ?&@@G~          @!    5GGGGG57.   .5@       @@@7               !@@@        Y@@@@G     Y@@@@#~ G@@@@Y          @P.     ^&@                ")
        sleep(0.01)
        print("                                    Y@@@P:     ^P@@@Y         @~              :7B@       @@@5    ?PPPPPPP?    Y@@@       Y@@@@G      J@@@@&!G@@@@Y          @7       5@                ")
        sleep(0.01)
        print("                                  !B@@#7         7#@@#!       @J!!!!!!!!!!7?YG&@        @@@B    !@       @~    G@@@      Y@@@@G       7@@@@@&@@@@Y          @GYYYYYYY#@   @@@@         ")
        sleep(0.01)
        print("                                  !!!!:           :!!!!                                @@@@BYYY5&@       @#5YYYB@@@@     Y@@@@G        ~#@@@    @Y                       @@  @@        ")
        sleep(0.01)
        print("                                                                                                                         Y@@@@G         ^B@@@  @@Y                        @@@@         ")
        sleep(0.01)
        print("                                                                                                                         Y@@@@G           P@@@@@@Y                                     ")
        sleep(0.01)
        print(Fore.WHITE + "                                                                                                                                                                                       ")
        sleep(0.01)
        print("                                                                                       <^BY OXDAN PRADUCTION!^>                                                                        ")
        sleep(0.01)
        print(" ")

        # Load the MP3 audio file
        audio_file = AudioSegment.from_mp3('resources/music/undertale.mp3')

        # Play the audio file
        play(audio_file)
        
        imports.own.will_go_to_start.main()