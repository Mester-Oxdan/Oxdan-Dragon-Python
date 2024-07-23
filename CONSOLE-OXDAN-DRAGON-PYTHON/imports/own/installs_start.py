import os

def installs_start(name):

            if name == "python-3.10.6":
                os.system("start " + os.environ["OXDAN-DRAGON-PYTHON"] + "\\imports\\own\\imports\\installs\\python.exe")
                
            if name == "nmap-7.94-setup":
                os.system("start " + os.environ["OXDAN-DRAGON-PYTHON"] + "\\imports\\own\\imports\\installs\\nmap.exe")
                
            if name == "git":
                os.system("start " + os.environ["OXDAN-DRAGON-PYTHON"] + "\\imports\\own\\imports\\installs\\git.exe")
                
            if name == "virtualbox":
                os.system("start " + os.environ["OXDAN-DRAGON-PYTHON"] + "\\imports\\own\\imports\\installs\\virtualbox.exe")
                
            if name == "protonvpn":
                os.system("start " + os.environ["OXDAN-DRAGON-PYTHON"] + "\\imports\\own\\imports\\installs\\protonvpn.exe")
                
            if name == "wireshark":
                os.system("start " + os.environ["OXDAN-DRAGON-PYTHON"] + "\\imports\\own\\imports\\installs\\wireshark.exe")
                

            if name == "miniconda3":
                os.system("start " + os.environ["OXDAN-DRAGON-PYTHON"] + "\\imports\\own\\imports\\installs\\miniconda3.exe")
