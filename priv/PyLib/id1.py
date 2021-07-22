import curses
from curses.textpad import rectangle

def clr(stdscr, y, x, l):
    p = 0
    for i in range(l-x+1):
        stdscr.addstr(y, x+p, ' ')
        p += 1

def igetstr(stdscr, y, x, l, strl=150):
    tp = 0
    p  = 0
    e  = 0

    s  = []
    
    ll = 0      # Left Limit
    rl = 0      # Right Limit
    pl = l-x+1  # Pointer Limit      # Chupenme un huevo comentarios de mierda
    er = 0      # E var Right Limit  # No significa lo que dicen.
    el = 0      # E var Left Limit   # Encima me da alta flojera corregirlos.

    stdscr.move(y, x)

    k = ""
    while True:

        stdscr.move(15,0);stdscr.clrtobot()
        stdscr.addstr(15,0, f"y: {y}\nx: {x}\nl: {l}\npl: {pl}\nk: {k}\np: {p}\ne: {e}\nll: {ll}\nrl: {rl}\ner: {er}\ns: {str(s)}\nlen(s): {len(s)}")
        stdscr.move(y, x+p)

        k = stdscr.get_wch()

        if k == 260:  # left
            if ll != 0 and not p:
                stdscr.addstr(3, 0, str(len(s) <= l-x+1))
                if er < rl:
                    er += 1
                else:
                    er -= 1
                ll -= 1
                rl -= 1
                clr(stdscr, y, x, l)
                for i in s[ll:er]:
                    stdscr.addch(y,x+p,i)
                    p += 1
                p = 0
                e -= 1
            elif e:
                p -= 1
                e -= 1
        
        elif k == 261:  # right
            if p == pl and e != len(s):
                stdscr.addstr(14,0,"True 1")
                p = 0
                ll += 1
                rl += 1
                er += 1
                clr(stdscr, y, x, l)
                for i in s[ll:er]:
                    stdscr.addch(y,x+p,i)
                    p += 1
                e += 1
            elif p != pl and e != rl:
                stdscr.addstr(14,0, "True 2")
                e += 1
                p += 1

        elif k == 263:  # backspace
            if ll != 0 and len(s) > pl and p != pl:  # Ya estoy tan podrido que ni quiero comentar.
                stdscr.addstr(14,0,"CHOTA 1")
                s.pop(e-1)
                tp = p
                er += 1
                clr(stdscr, y, x, l)
                p = 0
                for i in s[ll:er]:
                    stdscr.addch(y, x+p, i)
                    p += 1
                p = tp-1
                e -= 1
                er -= 1
                continue
            if ll != 0 and not p:  # Esta chota es para cuando borrás desde el inicio en segunda columna
                stdscr.addstr(14,0,"CHOTA 2")
                s.pop(e-1)
                tp = p
                ll -= 1
                rl -= 1
                if er < rl:
                    er += 1
                else:
                    er -= 1
                clr(stdscr, y, x, l)
                for i in s[ll:er]:
                    stdscr.addch(y, x+p, i)
                    p += 1
                p = 0
                e -= 1
                continue
            elif e:  # El normal
                stdscr.addstr(14,0,"CHOTA 3")
                s.pop(e-1)
                tp = p
                p = 0
                clr(stdscr, y, x, l)
                for i in s[ll:er]:
                    stdscr.addch(y, x+p, i)
                    p += 1
                p = tp-1
                e -= 1
                rl -= 1
                er -= 1
                continue

        elif k == '\n':
            ss = ""
            for i in s:
                ss += i
            return ss

        else:
            if type(k) == int:
                continue
            if e != strl:
                if e == rl and rl != strl and rl > l-x:
                    stdscr.addstr(14,0,"True 1")
                    ll += 1
                    rl += 1
                    s.insert(e,k)
                    p = 0
                    er += 1
                    for i in s[ll:er]:
                        stdscr.addch(y,x+p,i)
                        p += 1
                    e += 1
                    continue
                tp = p
                p = 0
                er += 1
                s.insert(e,k)
                for i in s[ll:er]:
                    stdscr.addch(y, x+p, i)
                    p += 1
                p = tp+1
                e += 1
                rl += 1

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
