import time
import os
import platform
import fileReader2
from enum import Enum







menuOptions = [ ['Tools', 'Features', 'About', 'Exit'],
                ['Update Row', 'Add New Row', 'Delete Row', 'Display Data Table', 'Build Table', 'Search'],
                ['Fact Generator', 'Histogram'],
                ['Created by Roman, Morgan, and Kyle for CS3100'] ]

Page = Enum('Page',{'MAIN':0,'TOOLS':1,'FEATURES':2,'ABOUT':3})

footerInfo = ['Use the UP and DOWN arrow keys to navigate. Press ENTER to select an option. Press BACKSPACE to return to main menu.']
toolTips = [['Print and Edit a CSV file.',
            'Play around with data-related programs.',
            'Credits, README',
            'Quits program and returns to terminal'],
            [],
            ['Enter two countries to generate a page of comparisons.',
             'Generate a visual histogram of country data.']]

#Color Codes
GREEN = "\033[32m"
BLACK = "\033[30m"
WHITE = "\033[37m"
BGWHITE = "\033[47m"



height, width = os.get_terminal_size().lines, os.get_terminal_size().columns
printLines = []

pageNo = Page.MAIN

for line in range(height):
   #printlines.append([text,textColor,textBG])
    printLines.append([f"{"#"*width}",None,None])

# Utility Functions
def clear_screen():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def print_color(text, text_color=None,background_color=None):
    style = ""
    if text_color:
        style += text_color
    if background_color:
        style += background_color
    print(f"{style}{text}\033[0m")

def display_menu():
    
    clear_screen()
    

    titleText = (["World Population Data", GREEN, None])
    printLines[0] = titleText

    #for opt in menuOptions[pageNo]





    #print menu
    for line in range(len(printLines)-1):
        print_color(printLines[line][0],printLines[line][1],printLines[line][2])


display_menu()

    
    
