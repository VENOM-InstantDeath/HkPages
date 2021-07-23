import re
from datetime import datetime

meses = {1: 'enero',
         2: 'febrero',
         3: 'marzo',
         4: 'abril',
         5: 'mayo',
         6: 'junio',
         7: 'julio',
         8: 'agosto',
         9: 'septiembre',
         10: 'octubre',
         11: 'noviembre',
         12: 'diciembre'}

dias = {1: 31,
        2: 0,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31}

now = datetime.now()

if now.year % 4 == 0:
    dias[2] = 29
else:
    dias[2] = 28

def main():
    while True:
        x = input('> ')
        if len(re.findall('[+-]')) > 1:
            print('')
        elif not len(re.findall('[+-]')):
            print('No hay ningún cálculo que hacer')
        x = re.split('[+-]', x)
        if len(x) != 2:
            continue
        for i in x:
            if i.count('/'):
                ###############  REGEX QUE MATCHEE d/m/y  ###########
                if not re.match('[1-3][0-9]?/[01][0-2]?/', i)
