import time
import curses
import fileReader2
from enum import Enum



menuOptions = [ ['Tools', 'Features', 'About', 'Exit'],
                ['Update Row', 'Add New Row', 'Delete Row'],
                ['Fact Generator', 'Histogram'],
                ['Created by Roman, Morgan, and Kyle for CS3100'] ]

Page = Enum('Page',{'MAIN':0,'TOOLS':1,'FEATURES':2,'ABOUT':3})

footerInfo = ['Use the Up and Down arrow keys to navigate. Press Enter to select an option. Press BACKSPACE to return to main menu.']


def display_menu(stdscr, column, selected_row_idx, pageNo):
    
    stdscr.clear()
    height, width = stdscr.getmaxyx()

    curses.curs_set(0)
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE) #highlighted color
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLACK) #regular text color
    curses.init_pair(3, curses.COLOR_GREEN, curses.COLOR_BLACK) #title text color

    titleText = "World Population Data"
    #titleX = (width // 2) - (len(titleText) // 2)
    titleX = 0
    titleY = 0
    
    stdscr.attron(curses.color_pair(3))
    stdscr.addstr(titleY,titleX,titleText)
    stdscr.attroff(curses.color_pair(3))

    for idx, row in enumerate(menuOptions[pageNo]):
        x = column
        y = 2 + idx
        if idx == selected_row_idx:
            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(y,x,row)
            stdscr.attroff(curses.color_pair(1))
        else:
            stdscr.addstr(y,x,row)

    stdscr.addstr(height-1,0,footerInfo[0])
    stdscr.refresh()



def main(stdscr):
    current_row_idx = 0
    current_page = Page.MAIN
    display_menu(stdscr, 0, current_row_idx, current_page.value)
    while 1: 
        key = stdscr.getch()
        stdscr.clear()

        if key == curses.KEY_UP and current_row_idx > 0:
            current_row_idx -= 1
        elif key == curses.KEY_DOWN and current_row_idx < len(menuOptions[current_page.value])-1:
            current_row_idx += 1
        elif key == curses.KEY_ENTER or key in [10,13]:
            current_row_idx = 0
            # Menu Option Code
            if menuOptions[current_page.value][current_row_idx] == 'Fact Generator':
                curses.endwin()  
                fileReader2.loop()
            # Exit
            if (current_page == Page.MAIN) and (current_row_idx == len(menuOptions[current_page.value])-1):
                break
            else:
                current_page = Page(current_row_idx+1)
                stdscr.refresh()
        elif key == curses.KEY_BACKSPACE or key == 127 or key == 8:
            current_page = Page.MAIN



        display_menu(stdscr, 0, current_row_idx, current_page.value)
        stdscr.refresh()
        





    

