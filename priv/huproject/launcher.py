import clock
import shlex

while True:
    cmd = input("command: ")
    cmd = shlex.split(cmd)
    if cmd[0] == 'exit':
        exit()
    if len(cmd) == 2:
        print(clock.clock(cmd[0], cmd[1]))
