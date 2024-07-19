import os

def installs_start(name):

            if name == "python-3.10.6":
                os.system("start " + os.environ["OXDAN-DRAGON-PYTHON"] + "\\imports\\own\\imports\\installs\\python-3.10.6-amd64.exe")
                
            if name == "nmap-7.94-setup":
                os.system("start " + os.environ["OXDAN-DRAGON-PYTHON"] + "\\imports\\own\\imports\\installs\\nmap-7.94-setup.exe")
                
            if name == "git":
                os.system("start " + os.environ["OXDAN-DRAGON-PYTHON"] + "\\imports\\own\\imports\\installs\\Git-2.37.2.2-64-bit.exe")
                
            if name == "miniconda3":
                os.system("start " + os.environ["OXDAN-DRAGON-PYTHON"] + "\\imports\\own\\imports\\installs\\Miniconda3-latest-Windows-x86_64.exe")
