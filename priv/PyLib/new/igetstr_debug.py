import curses
from curses.textpad import rectangle

def clr(stdscr, y, x, l):
    p = 0
    for i in range(l-x+1):
        stdscr.addstr(y, x+p, ' ')
        p += 1

def redraw(stdscr, s, e, y, x, l):
    clr(stdscr, y, x, l)
    page = len(s)//(l-x+1+1)  # E NO ESTÁAAA!!!!!!!
    b = s[((l-x+1)*(page+1))-(l-x+1):((l-x+1+1)*(page+1))] 
    for i in (2,3,4):
        stdscr.move(i, 0)
        stdscr.clrtoeol()
    stdscr.addstr(2, 0, str(b))
    stdscr.addstr(3, 0, str(page))
    stdscr.addstr(4, 0, str(len(b)))
    k = ""
    for i in b:
        k += i
    stdscr.addstr(y, x, k)

def igetstr(stdscr, y, x, l, strl=150):
    tp = 0
    p  = 0
    e  = 0

    s  = []
    
    ll = 0      # Left Limit
    rl = 0      # Right Limit
    pl = l-x+1  # Pointer Limit
    er = 0      # E var Right Limit
    el = 0      # E var Left Limit

    stdscr.move(y, x)

    k = ""
    while True:

        stdscr.move(15,0);stdscr.clrtobot()
        stdscr.addstr(15,0, f"y: {y}\nx: {x}\nl: {l}\npl: {pl}\nk: {k}\np: {p}\ne: {e}\nll: {ll}\nrl: {rl}\ner: {er}\ns: {str(s)}\nlen(s): {len(s)}")
        stdscr.move(y, x+p)

        k = stdscr.get_wch()

        if k == 260:  # left
            if p:
                p -= 1
                e -= 1
                redraw(stdscr, s, e, y, x, l)
        
        elif k == 261:  # right
            if e != len(s):
                p += 1
                e += 1
                if p == l-x+1:
                    p = 0
                redraw(stdscr, s, e, y, x, l)

        elif k == 263:  # backspace
            if e:
                s.pop(e-1)
                stdscr.addch(y, x+p-1, ' ')
                e -= 1
                p -= 1
                if not p and e:
                    p = l-x+1
                redraw(stdscr, s, e, y, x, l)
            pass

        elif k == '\n':
            k = ""
            for i in s:
                k += i
            return k

        else:
            if type(k) == int:
                continue
            if e != strl:
                if p == l-x+1:
                    p = 0
                if p != l-x+1:
                    p += 1
                s.insert(e, k)
                e += 1
                redraw(stdscr, s, e, y, x, l)

def main(stdscr):
    while True:
        k = stdscr.get_wch()
        stdscr.clear()
        if k == 'q':
            break
        stdscr.addstr(str(k))
        continue
    rectangle(stdscr, 10, 20, 12, 60)
    s = igetstr(stdscr, 11, 21, 59)
    stdscr.clear()
    stdscr.addstr(0,0,s)
    stdscr.getch()

curses.wrapper(main)
