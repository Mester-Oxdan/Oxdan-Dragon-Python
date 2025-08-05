import imports.own.will_go_to_start
import pymem
from pymem import process
from colorama import Fore
import ctypes
import os
import sys

# NtCreateThreadEx setup
ntdll = ctypes.WinDLL('ntdll')
NtCreateThreadEx = ntdll.NtCreateThreadEx

NtCreateThreadEx.restype = ctypes.c_ulong  # NTSTATUS
NtCreateThreadEx.argtypes = [
    ctypes.POINTER(ctypes.c_void_p),  # thread handle
    ctypes.c_ulong,                   # desired access
    ctypes.c_void_p,                  # object attributes (usually NULL)
    ctypes.c_void_p,                  # process handle
    ctypes.c_void_p,                  # start address
    ctypes.c_void_p,                  # parameter to start routine
    ctypes.c_ulong,                  # create suspended flag (BOOL)
    ctypes.c_ulong,                  # stack zero bits
    ctypes.c_ulong,                  # size of stack
    ctypes.c_ulong,                  # maximum stack size
    ctypes.c_void_p                  # attribute list (usually NULL)
]

def restart_as_admin():
    ctypes.windll.user32.MessageBoxW(0, "Admin privileges are required.\nThe program will restart as Administrator.", "Elevation Required", 0x40)
    path_to_script = os.path.abspath(sys.argv[0])
    params = '"' + path_to_script + '"'
    # Relaunch the same script with admin rights
    ret = ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, params, None, 1)
    if ret <= 32:
        print(Fore.RED + "Failed to elevate privileges." + Fore.WHITE)
        sys.exit(1)
    sys.exit(0)

def nt_create_remote_thread(process_handle, start_address, parameter):
    thread_handle = ctypes.c_void_p()
    status = NtCreateThreadEx(
        ctypes.byref(thread_handle),
        0x1FFFFF,           # THREAD_ALL_ACCESS
        None,
        process_handle,
        start_address,
        parameter,
        False,              # Not suspended
        0,
        0,
        0,
        None
    )
    if status != 0:
        raise ctypes.WinError(ctypes.get_last_error())
    return thread_handle.value


def inject_prog_start():
    if not ctypes.windll.shell32.IsUserAnAdmin():
        restart_as_admin()
    print(Fore.RED + "\nEnter 'esc' (for exit)" + Fore.WHITE)
    dll_path = input(Fore.YELLOW + "Enter path to DLL file: " + Fore.WHITE)

    if imports.own.will_go_to_start.remove_098(dll_path.lower()) == "esc":
        imports.own.will_go_to_start.main()
        return

    print(Fore.RED + "\nEnter 'esc' (for exit)" + Fore.WHITE)
    process_id_input = input(Fore.YELLOW + "Enter PID to target process: " + Fore.WHITE)

    if imports.own.will_go_to_start.remove_098(process_id_input.lower()) == "esc":
        imports.own.will_go_to_start.main()
        return

    try:
        process_id = int(process_id_input)  # Convert PID input to integer
        pymem_process = pymem.Pymem(process_id)

        # Allocate memory in the target process for the DLL path
        dll_path_bytes = bytes(dll_path, "utf-8")
        PAGE_READWRITE = 0x04
        MEM_COMMIT = 0x1000
        MEM_RESERVE = 0x2000

        dll_path_address = ctypes.windll.kernel32.VirtualAllocEx(
            pymem_process.process_handle,
            None,
            len(dll_path_bytes) + 1,
            MEM_RESERVE | MEM_COMMIT,
            PAGE_READWRITE
        )

        if dll_path_address == 0:
            print(Fore.RED + "\n(!ERROR!) " + Fore.WHITE + "=" + Fore.GREEN + " (!Failed to allocate memory in target process!)" + Fore.WHITE)
            imports.own.will_go_to_start.main()

        bytes_written = ctypes.c_size_t(0)
        ctypes.windll.kernel32.WriteProcessMemory(
            pymem_process.process_handle,
            dll_path_address,
            dll_path_bytes,
            len(dll_path_bytes),
            ctypes.byref(bytes_written)
        )

        # Get kernel32.dll module info from target process
        kernel32_module = pymem.process.module_from_name(pymem_process.process_handle, "kernel32.dll")
        if not kernel32_module:
            print(Fore.RED + "\n(!ERROR!) " + Fore.WHITE + "=" + Fore.GREEN + " (!Failed to find kernel32.dll in target process!)" + Fore.WHITE)
            imports.own.will_go_to_start.main()

        remote_kernel32_base = kernel32_module.lpBaseOfDll

        # Get LoadLibraryA offset in local kernel32.dll
        local_kernel32_handle = ctypes.windll.kernel32.GetModuleHandleW("kernel32.dll")
        local_load_library_addr = ctypes.windll.kernel32.GetProcAddress(local_kernel32_handle, b"LoadLibraryA")

        offset = local_load_library_addr - local_kernel32_handle

        # Calculate remote LoadLibraryA address
        load_library_address = remote_kernel32_base + offset

        if load_library_address == 0:
            print(Fore.RED + "\n(!ERROR!) " + Fore.WHITE + "=" + Fore.GREEN + " (!Failed to get remote LoadLibraryA address!)" + Fore.WHITE)
            imports.own.will_go_to_start.main()


        # Use NtCreateThreadEx instead of CreateRemoteThread
        thread_handle = nt_create_remote_thread(
            pymem_process.process_handle,
            load_library_address,
            dll_path_address
        )

        if thread_handle == 0:
            print(Fore.RED + "\n(!ERROR!) " + Fore.WHITE + "=" + Fore.GREEN + " (!Failed to create remote thread with NtCreateThreadEx!)" + Fore.WHITE)
            imports.own.will_go_to_start.main()

        # Wait for the thread to finish
        ctypes.windll.kernel32.WaitForSingleObject(thread_handle, -1)  # INFINITE

        # Free the memory allocated for the DLL path
        MEM_RELEASE = 0x8000
        ctypes.windll.kernel32.VirtualFreeEx(
            pymem_process.process_handle,
            dll_path_address,
            0,
            MEM_RELEASE
        )

        if ctypes.windll.kernel32.CloseHandle(thread_handle) == 0:
            print(Fore.RED + "\n(!ERROR!) " + Fore.WHITE + "=" + Fore.GREEN + " (!Failed to close handle to remote thread!)" + Fore.WHITE)
            imports.own.will_go_to_start.main()

        if ctypes.windll.kernel32.CloseHandle(pymem_process.process_handle) == 0:
            print(Fore.RED + "\n(!ERROR!) " + Fore.WHITE + "=" + Fore.GREEN + " (!Failed to close handle to target process!)" + Fore.WHITE)
            imports.own.will_go_to_start.main()

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
