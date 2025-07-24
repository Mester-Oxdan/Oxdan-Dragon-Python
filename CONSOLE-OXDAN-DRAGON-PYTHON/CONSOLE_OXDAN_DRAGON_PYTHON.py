import imports.own.start_start
import argparse
import os
import sys
import subprocess
import importlib.util
import venv
import platform

files_dir = os.path.dirname(__file__)
os.environ["OXDAN-DRAGON-PYTHON"] = files_dir 

#path_to_png = os.path.join(os.environ["OXDAN-DRAGON-PYTHON"],"..","IMAGES","ALL","icon.png")

def execute_direct_command(command_str):
    from imports.own import will_go_to_start

    # Fill the command queue
    will_go_to_start.command_queue = [
        cmd.strip() for cmd in command_str.split("|") if cmd.strip()
    ]

    # Start the main loop
    will_go_to_start.main()



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Oxdan Dragon CLI")

    parser.add_argument(
        "command",
        nargs=argparse.REMAINDER,
        help="Command to run directly (without entering full console)",
    )

    args = parser.parse_args()

    if args.command:
        # Run the command passed like a direct input
        import shlex
        joined = " ".join(args.command)
        direct_command = joined if "|" in joined else joined.replace("|", " | ")
        print(f"Executing: {direct_command}")
        execute_direct_command(direct_command)
    else:
        # Run full console
        
        imports.own.start_start.start_start()