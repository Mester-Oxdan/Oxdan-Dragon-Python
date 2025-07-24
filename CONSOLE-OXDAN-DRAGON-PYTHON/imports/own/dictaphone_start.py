import pyaudio
import wave
import keyboard
from colorama import Fore
import imports.own.will_go_to_start
import colorama

def dictaphone_start():
    # Audio recording parameters
    CHUNK = 1024  # Buffer size
    FORMAT = pyaudio.paInt16  # 16-bit resolution
    CHANNELS = 2  # Stereo recording
    RATE = 44100  # Sample rate (44.1kHz)
    WAVE_OUTPUT_FILENAME = "output_recorded_voice.wav"

    # Initialize PyAudio object
    p = pyaudio.PyAudio()

    # Open stream
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    print(Fore.RED + "\nPress 'Esc' for exit" + Fore.WHITE)
    frames = []

    try:
        print(Fore.YELLOW + "[!] Recording Started!" + Fore.WHITE)
        while True:
            if keyboard.is_pressed('esc'):
                break
            data = stream.read(CHUNK)
            frames.append(data)

    except Exception as e:
        print(colorama.Fore.RED + "\n(!ERROR!) " + colorama.Fore.WHITE + "=" + colorama.Fore.GREEN + f" (!{str(e)}!)\n" + colorama.Fore.WHITE)
        #print(f"\n(!ERROR!) {str(e)}")

    # Stop and close the stream
    stream.stop_stream()
    stream.close()
    p.terminate()

    # Save the recorded audio to a .wav file
    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()

    print(Fore.GREEN + "[!] Recording Finished!" + Fore.WHITE)
    imports.own.will_go_to_start.main()