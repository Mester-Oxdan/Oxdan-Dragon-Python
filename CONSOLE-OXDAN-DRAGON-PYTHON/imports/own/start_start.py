import os
import sys
import subprocess
import importlib.util
import venv
import platform

def get_system_pip_path():
    """Find the pip executable in the system environment."""
    # Try to locate pip using the same Python executable running this script
    python_path = sys.executable
    scripts_dir = os.path.join(os.path.dirname(python_path), "Scripts")
    pip_path = os.path.join(scripts_dir, "pip.exe")
    
    if os.path.exists(pip_path):
        return pip_path
    else:
        print(f"Error: pip not found at {pip_path}. Ensure pip is installed for the system Python.")
        sys.exit(1)

def install_pywin32_system():
    """Install pywin32 in the system environment and run post-installation."""
    pip_path = get_system_pip_path()
    python_path = sys.executable

    # Install pywin32
    print("Installing pywin32 in system environment...")
    result = subprocess.run(
        [pip_path, "install", "--no-cache-dir", "pywin32"],
        capture_output=True,
        text=True
    )
    if result.returncode == 0:
        print("Successfully installed pywin32.")
        # Run post-installation script
        postinstall_script = os.path.join(os.path.dirname(pip_path), "pywin32_postinstall.py")
        if os.path.exists(postinstall_script):
            print("Running pywin32 post-installation script...")
            result = subprocess.run(
                [python_path, postinstall_script, "-install"],
                capture_output=True,
                text=True
            )
            if result.returncode == 0:
                print("Post-installation completed successfully.")
            else:
                print(f"Post-installation failed: {result.stderr}")
                sys.exit(1)
        else:
            print("Warning: pywin32 post-installation script not found.")
    else:
        print(f"Failed to install pywin32: {result.stderr}")
        sys.exit(1)
# Test import
try:
    import win32api
    print("Successfully imported win32api.")
except ImportError as e:
    print(f"Failed to import win32api: {e}")
    # Run the installation
    install_pywin32_system()

# List of required packages
REQUIRED_PACKAGES = [
    "colorama",
    "keyboard",
    "gitpython",
    "requests",
    "winotify",
    "pygame",
    "pysocks",  # Corrected 'socks' to 'pysocks' (assuming this is the intended package)
    "aiohttp",
    "pydub",
    "pyaudio",
    "numpy",
    "pywin32",
    "typing_extensions",
    "pyautogui",
    "Pillow",
    "opencv-python",
    "pyglet",
    "pymem",
    "pynput",
    "pywifi",
    "comtypes",
    "phonenumbers",
    "opencage",
    "pycountry",
    "geopy",
    "pycaw",
    "tkcalendar",
    "currency_converter",
    "forex-python",
    "googletrans",
    "click",
    "pygments",
    "rich",
    "chess",
    "neat-python",
    "wmi",
    "SpeechRecognition",
    "pyttsx3",
    "speedtest-cli",

]

def create_venv(venv_path):
    """Create a virtual environment if it doesn't exist."""
    if not os.path.exists(venv_path):
        print(f"Creating virtual environment at {venv_path}...")
        venv.create(venv_path, with_pip=True)
    else:
        print(f"Virtual environment already exists at {venv_path}.")

def get_pip_path(venv_path):
    """Get the path to the pip executable in the virtual environment."""
    if platform.system() == "Windows":
        return os.path.join(venv_path, "Scripts", "pip")
    else:
        return os.path.join(venv_path, "bin", "pip")

def get_venv_python_path(venv_path):
    """Get the path to the Python executable in the virtual environment."""
    if platform.system() == "Windows":
        return os.path.join(venv_path, "Scripts", "python")
    else:
        return os.path.join(venv_path, "bin", "python")

def install_package(package, pip_path):
    """Install a package using pip in the virtual environment."""
    print(f"Installing {package}...")
    result = subprocess.run([pip_path, "install", package], capture_output=True, text=True)
    if result.returncode == 0:
        print(f"Successfully installed {package}.")
    else:
        print(f"Failed to install {package}: {result.stderr}")
        sys.exit(1)

def check_and_install_packages(venv_path):
    """Check if packages are installed in system or virtual environment; install if missing."""
    pip_path = get_pip_path(venv_path)
    venv_python_path = get_venv_python_path(venv_path)

    for package in REQUIRED_PACKAGES:
        # Step 1: Check system environment
        spec = importlib.util.find_spec(package)
        if spec is not None:
            print(f"{package} is already installed in the system environment.")
            continue  # Skip installation if found in system

        # Step 2: Check virtual environment
        result = subprocess.run(
            [venv_python_path, "-c", f"import importlib.util; print(importlib.util.find_spec('{package}'))"],
            capture_output=True, text=True
        )
        if "None" not in result.stdout:
            print(f"{package} is already installed in the virtual environment.")
            continue  # Skip installation if found in virtual environment

        # Step 3: Install if missing in both
        print(f"{package} not found in system or virtual environment. Installing in virtual environment...")
        install_package(package, pip_path)

def activate_venv(venv_path):
    """Modify sys.path to use the virtual environment's site-packages."""
    if platform.system() == "Windows":
        site_packages = os.path.join(venv_path, "Lib", "site-packages")
    else:
        site_packages = os.path.join(venv_path, "lib", f"python{sys.version_info.major}.{sys.version_info.minor}", "site-packages")
    if os.path.exists(site_packages):
        sys.path.insert(0, site_packages)
    else:
        print(f"Error: site-packages not found in {venv_path}.")
        sys.exit(1)

# Set up virtual environment before imports
project_dir = os.getcwd()
if not project_dir:
    print("Error: OXDAN-DRAGON-PYTHON environment variable not set.")
    sys.exit(1)
venv_path = os.path.join(project_dir, "imports_system")
create_venv(venv_path)
check_and_install_packages(venv_path)
activate_venv(venv_path)

import msvcrt
import colorama
import keyboard
import imports.own.login
import imports.own.signup
import imports.own.instructions
import ctypes
import time
import git
import requests
import shutil
import time
from datetime import datetime

start_time = time.time()
start_time_2 = datetime.now().strftime("%H:%M:%S")

def printMenu(items, active_index):

    print(" ")
    print("                                                              ")
    print("                                                              ")
    print("                                                              ")
    print("                                                              ")
    print("                                                              ")
    print("                                                              ")
    print("                                                              ")
    print("                                                              ")
    print("                                                              ")
    #print("                                                              ")
    for index, item in enumerate(items):
        if index == active_index:
            #print(f'\033[31;47m{item}\033[0m')

            print(colorama.Fore.RED + f'{item}' + colorama.Fore.YELLOW)
        else:
            print(item)

def start_start():

    print(colorama.Fore.YELLOW)
    os.system("cls")
    #print(os.path.join(os.environ["OXDAN-DRAGON-PYTHON"],"imports/own/resources/music/steel.ogg"))
    #print(os.path.join(os.environ["OXDAN-DRAGON-PYTHON"], "resources\math_game\kenvector_future.ttf"))
    #print(os.path.join(os.environ["OXDAN-DRAGON-PYTHON"],"imports/own/config.txt"))
    #print(os.path.join(os.environ["OXDAN-DRAGON-PYTHON"],"imports/own/my_dragon_ico.jpg"))
    #msvcrt.getch()

    Menu = ["                                                              REGISTRATION", "                                                              LOGIN", "                                                              SKIP", "                                                              INSTRUCTIONS", "                                                              EXIT"]
    active_menu = 0
    keyboard.press(72)

    while True:

        key = ord(msvcrt.getch())

        if key == 27:
            
            exit(0)

        elif key == 72:

            if active_menu > 0:
                active_menu -= 1
            os.system("cls")
            
                
            #break

        elif key == 80:

            if active_menu < 4:
                active_menu += 1
            os.system("cls")

            #break

        elif key == 13:

            if active_menu == 0: # 1

                os.system("cls")
                imports.own.signup.signup()

            if active_menu == 1: # 2

                os.system("cls")
                imports.own.login.login()

            if active_menu == 2: # 3

                os.system("cls")
                print(colorama.Fore.YELLOW + "Oxdan" + colorama.Fore.RED + " Dragon" + colorama.Fore.WHITE + " [ Version: 2.2024 [ENGLISH] (PYTHON) [WINDOWS] ] ") # intro cmd (+)
                time.sleep(0.01)
                print("(p) Oxdan Praduction. ")
                time.sleep(0.01)
                imports.own.will_go_to_start.main()
                
            if active_menu == 3: # 4

                os.system("cls")
                imports.own.instructions.instructions()

            if active_menu == 4: # 5

                #os.system("cls")
                exit(0)

        elif key == 49: # 1

                os.system("cls")
                imports.own.signup.signup()

        elif key == 50: # 2

                os.system("cls")
                imports.own.login.login()
                
        elif key == 51: # 3

                os.system("cls")
                print(colorama.Fore.YELLOW + "Oxdan" + colorama.Fore.RED + " Dragon" + colorama.Fore.WHITE + " [ Version: 2.2024 [ENGLISH] (PYTHON) [WINDOWS] ] ") # intro cmd (+)
                time.sleep(0.01)
                print("(p) Oxdan Praduction. ")
                time.sleep(0.01)
                imports.own.will_go_to_start.main()

        elif key == 52: # 4

                os.system("cls")
                imports.own.instructions.instructions()

        elif key == 53: # 5

                os.system("cls")
                exit(0)
            
        else:

            continue

        printMenu(Menu, active_menu)
