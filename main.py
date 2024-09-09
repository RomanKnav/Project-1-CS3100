from sysManager import SystemManager

# Package Handling
terminal_control = SystemManager()
terminal_control.check_and_install_curses()

import fileReader2 
import UI
import curses

# Main Function
curses.wrapper(UI.main)
