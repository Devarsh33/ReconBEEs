import subprocess
import os
from colors import *

if __name__ == '__main__':

    while True:

        print()
        target = input('''%sEnter a Target : %s''' % (green, end))

        # amass method

        print()
        choice = input('''%sDO YOU WANT TO BRUTEFORCE THE WEBSITE DIRECTORIES ? YES (y)/NO (n) : %s''' % (green, end))

        if choice == 'y' or choice == 'Y':
            print()
            print("%sIt may take time...!!%s" % (yellow, end))
            print()
            scan = subprocess.run(f'amass enum -brute -d {target} -config config.ini -o /root/.config/{target}-amass.txt', shell=True)
            print(scan)

        else:
            print()
            scan = subprocess.run(f'amass enum -brute -d {target} -config config1.ini -o /root/.config/{target}-amass.txt', shell=True)
            print(scan)


        # crt.sh method

        scancrt = subprocess.run(f'./crt.sh {target} > /root/.config/{target}-crt.txt', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        print(scancrt.stdout.decode())

        # sorting

        sort = os.popen(f'sort -u /root/.config/{target}-amass.txt /root/.config/{target}-crt.txt > /root/.config/{target}-sort.txt').read()
        print(sort)

        # final recon

        final = subprocess.run(f'cat /root/.config/{target}-sort.txt | waybackurls | tee -a /root/Desktop/'
                               f'{target}-advancere.txt', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        print(final.stdout.decode())
        print(f'%s Your Output saved in /root/Desktop as a {target}-advancere.txt %s' % (red, end))

        # remove files

        remove = os.popen(f'rm -rf /root/.config/{target}-amass.txt /root/.config/{target}-crt.txt /root/.config/{target}-sort.txt').read()
        print(remove)

        print()
        again = input('''%sWould you like to another scan ? yes(y)/no(n) : %s''' % (green, end))
        if again == "y" or again == "Y":
            print()
        else:
            bh = subprocess.run('python3 bheem.py', shell=True)
            print(bh)
            break

