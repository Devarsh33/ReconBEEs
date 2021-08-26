import os
from colors import *
import subprocess

if __name__ == '__main__':
    while True:

        print()
        website = input("%sEnter URL : %s" % (green, end))

        scan = os.popen(f'wafw00f {website}').read()
        print(scan)

        print()
        again = input('''%sWould you like to another scan ? yes(y)/no(n) : %s''' % (green, end))
        if again == "y" or again == "Y":
            print()
        else:
            bh = subprocess.run('python3 bees.py', shell=True)
            print(bh)
            break
