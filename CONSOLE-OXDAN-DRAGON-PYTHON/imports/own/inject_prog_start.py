import imports.own.will_go_to_start
import pymem
from pymem import process
from colorama import Fore
import ctypes
import os

def inject_prog_start():
    print(Fore.RED + "\nWrite 'esc' (for exit)" + Fore.WHITE)
    dll_path = input(Fore.YELLOW + "Enter path to DLL file: " + Fore.WHITE)

    if dll_path.lower() == "esc":
        imports.own.will_go_to_start.main()
        return

    print(Fore.RED + "\nWrite 'esc' (for exit)" + Fore.WHITE)
    process_id_input = input(Fore.YELLOW + "Enter PID to target process: " + Fore.WHITE)

    if process_id_input.lower() == "esc":
        imports.own.will_go_to_start.main()
        return

    try:
        process_id = int(process_id_input)  # Convert PID input to integer
        pymem_process = pymem.Pymem(process_id)
        #print(Fore.GREEN + f"Successfully opened process with PID {process_id}." + Fore.WHITE)

        # Allocate memory in the target process for the DLL path
        dll_path_bytes = bytes(dll_path, "utf-8")
        dll_path_address = pymem.process.virtual_alloc(pymem_process.process_handle, len(dll_path_bytes) + 1)
        
        if dll_path_address == 0:
            #raise RuntimeError(".")
            print(Fore.RED + "\n(!ERROR!) " + Fore.WHITE + "=" + Fore.GREEN + " (!Failed to allocate memory in target process!)" + Fore.WHITE)

        pymem.process.write_process_memory(pymem_process.process_handle, dll_path_address, dll_path_bytes)

        # Get the address of the LoadLibraryA function from kernel32.dll
        kernel32 = pymem.process.load_library(pymem_process.process_handle, "kernel32.dll")
        load_library_address = pymem.process.get_proc_address(kernel32, "LoadLibraryA")

        if load_library_address == 0:
            #raise RuntimeError(".")
            print(Fore.RED + "\n(!ERROR!) " + Fore.WHITE + "=" + Fore.GREEN + " (!Failed to get address of LoadLibraryA!)" + Fore.WHITE)

        # Create a remote thread in the target process to load the DLL
        thread_handle = pymem.process.create_remote_thread(pymem_process.process_handle, load_library_address, dll_path_address)
        
        if thread_handle == 0:
            #raise RuntimeError("")
            print(Fore.RED + "\n(!ERROR!) " + Fore.WHITE + "=" + Fore.GREEN + " (!Failed to create remote thread!)" + Fore.WHITE)

        # Wait for the thread to finish
        ctypes.windll.kernel32.WaitForSingleObject(thread_handle, -1)  # INFINITE

        # Free the memory allocated for the DLL path
        pymem.process.virtual_free(pymem_process.process_handle, dll_path_address, len(dll_path_bytes) + 1, process.MEM_RELEASE)

        if ctypes.windll.kernel32.CloseHandle(thread_handle) == 0:
            raise RuntimeError("")
            print(Fore.RED + "\n(!ERROR!) " + Fore.WHITE + "=" + Fore.GREEN + " (!Failed to close handle to remote thread!)" + Fore.WHITE)

        if ctypes.windll.kernel32.CloseHandle(pymem_process.process_handle) == 0:
            #raise RuntimeError("")
            print(Fore.RED + "\n(!ERROR!) " + Fore.WHITE + "=" + Fore.GREEN + " (!Failed to close handle to target process!)" + Fore.WHITE)

        #print(Fore.GREEN + "DLL injected successfully!" + Fore.WHITE)
        print(Fore.GREEN + "\n(!SUCCESS!) " + Fore.WHITE + "=" + Fore.YELLOW + " (!Process opened successfully!)" + Fore.WHITE)
        imports.own.will_go_to_start.main()

    except ValueError:
        print(Fore.RED + "\n(!ERROR!) " + Fore.WHITE + "=" + Fore.GREEN + " (!Invalid PID format!)" + Fore.WHITE)
        imports.own.will_go_to_start.main()

    except pymem.exception.PymemError as e:
        print(Fore.RED + f"\n(!ERROR!) " + Fore.WHITE + "=" + Fore.GREEN + f" (!Pymem error: {e}!)" + Fore.WHITE)
        imports.own.will_go_to_start.main()

    except RuntimeError as e:
        print(Fore.RED + f"\n(!ERROR!) " + Fore.WHITE + "=" + Fore.GREEN + f" (!Runtime error: {e}!)" + Fore.WHITE)
        imports.own.will_go_to_start.main()

    except Exception as e:
        print(Fore.RED + f"\n(!ERROR!) " + Fore.WHITE + "=" + Fore.GREEN + f" (!Unexpected error: {e}!)" + Fore.WHITE)
        imports.own.will_go_to_start.main()
