#tello input test
#tello can be controlled by command line
#This code is originally tello_test.py
#it's modified to run with python3

from tello3 import Tello
import sys
from datetime import datetime
import time


start_time = str(datetime.now())
t1 = time.time()

#file_name = sys.argv[1]

#f = open(file_name, "r")
#commands = f.readlines()

tello = Tello()
while True:

    command = input("write command:")

    if not command:
        break

    if command != '' and command != '\n':
        command = command.rstrip()

        if command.find('delay') != -1:
            sec = float(command.partition('delay')[2])
            print('delay %s' % sec)
            time.sleep(sec)
            pass
        else:
            tello.send_command(command)

    if 'end' in command:
        print('...')
        tello.on_close()
        break

    if time.time()-t1 > 20: #max 20 secs
        tello.send_command('land')
        tello.on_close() #land and kill socket connection
        break

log = tello.get_log()

out = open('log/' + start_time + '.txt', 'w')
for stat in log:
    stat.print_stats()
    str = stat.return_stats()
    out.write(str)