# A Python Class that contains system functions for running terminal commands including installing necessary Python modules.
import sys
import subprocess
import platform

class SystemManager:
    def install(self, package):
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])

    def install_system_package(self, package_name):
        try:
            subprocess.check_call(["sudo", "apt-get", "install", "-y", package_name])
        except subprocess.CalledProcessError:
            print(f"Failed to install {package_name}. Please install it manually.")

    def check_and_install_curses(self):
        # Check for the platform and install the necessary package
        system = platform.system()

        if system == "Windows":
            try:
                import curses
            except ImportError:
                print("Installing windows-curses for Windows...")
                self.install('windows-curses')

        elif system == "Linux":
            try:
                import curses
            except ImportError:
                print("Installing python3-curses for Linux...")
                self.install_system_package('python3-curses')

        elif system == "Darwin": # macOS
            try:
                import curses
            except ImportError:
                print("Installing ncurses for macOS...")
                self.install_system_package('ncurses')

        else:
            print(f"Unsupported system: {system}. Please install the necessary packagees manually.")