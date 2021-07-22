import curses

def menu(stdscr, y, x, d):
    curses.use_default_colors()
    curses.init_pair(15, 0, 15)
    it = list(d.keys())
    p = 0
    for i in d:
        stdscr.addstr(y+p, x, i)
        p += 1
    p = 0
    stdscr.addstr(y+p,x, it[p], curses.color_pair(15))
    while True:
        k = stdscr.getch()
        if k == 259:
            if p:
                stdscr.addstr(y+p, x, it[p])
                p -= 1
                stdscr.addstr(y+p, x, it[p], curses.color_pair(15))
        if k == 258:
            if p != len(it)-1:
                stdscr.addstr(y+p, x, it[p])
                p += 1
                stdscr.addstr(y+p, x, it[p], curses.color_pair(15))
        if k == 10:
            res=d[it[p]]()
            if res:
                return res
            return

if __name__ == "__main__":
    def main(stdscr):
        curses.use_default_colors()
        curses.init_pair(15, 0, 15)
        menu(stdscr, 10, 20, {"exit": exit, "print": lambda: stdscr.addstr(1,0,"hello")})
    curses.wrapper(main)
