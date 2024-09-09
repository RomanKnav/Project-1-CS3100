import sys
import subprocess
import platform




def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

def install_system_package(package_name):
    try:
        subprocess.check_call(["sudo", "apt-get", "install", "-y", package_name])
    except subprocess.CalledProcessError:
        print(f"Failed to install {package_name}. Please install it manually.")

def check_and_install_curses():
    # Check for the platform and install the necessary package
    system = platform.system()

    if system == "Windows":
        try:
            import curses
        except ImportError:
            print("Installing windows-curses for Windows...")
            install('windows-curses')

    elif system == "Linux":
        try:
            import curses
        except ImportError:
            print("Installing python3-curses for Linux...")
            install_system_package('python3-curses')

    elif system == "Darwin": # macOS
        try:
            import curses
        except ImportError:
            print("Installing ncurses for macOS...")
            install_system_package('ncurses')

    else:
        print(f"Unsupported system: {system}. Please install the necessary packagees manually.")



check_and_install_curses()

import fileReader2 
import UI
import curses
curses.wrapper(UI.main)
