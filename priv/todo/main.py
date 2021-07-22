import curses

def main(stdscr):
    y, x = stdscr.getmaxyx()
    stdscr.addstr(y, x, '')
    stdscr.getch()

curses.wrapper(main)
