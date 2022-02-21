import sys
import random
from time import sleep
from screen import Screen
from colorama import Fore, Style


def commander():
    """ Function to handle command line usage"""
    args = sys.argv
    args1 = args[1:2] # First element of args is the file name
    args2 = args[2:3] # Second element of args is the file name

    if len(args2) == 0:
        wait = 5
    else:
        wait = int(args2[0])

    if len(args1) == 0:
        print('You have not passed any commands in!')

    else:
        a = args1[0]
        if a == '--help':
            print('Basic command line program')
            print('Options:')
            print('    --help -> show this basic help menu.')
            print('    --rec wait[optional] ->  start screen recording, wait is the time in seconds to wait before recording.')
            print('    --shot wait[optional] -> take a screenshot, wait is the time in seconds to wait before taking a screenshot.')

        elif a == '--rec':
            print(Fore.GREEN+'Focus on the window you want to record')
            sleep(2)
            print(Fore.GREEN+'Recording starts in {} seconds'.format(wait))
            sleep(wait)
            shutter = Screen()
            shutter.record()

        elif a == '--shot':
            print(Fore.GREEN+'Focus on the window you want to take a screenshot of')
            sleep(2)
            print(Fore.GREEN+'Taking a screenshot in {} seconds'.format(wait))
            sleep(wait)
            shutter = Screen()
            shutter.shot()

        else:
            print('Unknown command: ' + a)
            print(Fore.MAGENTA+'Use --help for more info')

    print(Style.RESET_ALL)
			
if __name__ == '__main__':
	commander()