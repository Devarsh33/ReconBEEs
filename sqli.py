import subprocess
from colors import *
import os

if __name__ == '__main__':

    while True:

        print()
        file_input = input("%sEnter the File Path Which contains subdomains : %s" % (green, end))

        f = os.path.exists(file_input)

        if f:

            sql = os.popen(f'cat {file_input} | gf sqli | tee -a /root/Desktop/sqli.txt').read()
            print(sql)
            print("%s%s Your output Saved in /root/Desktop as a sqli.txt%s" % (info, red, end))

        else:

            print()
            print("%s%s File not Found...!!%s" % (bad, red, end))

        print()
        again = input('''%sWould you like to another scan ? yes(y)/no(n) : %s''' % (green, end))
        if again == "y" or again == "Y":
            print()
        else:
            bh = subprocess.run('python3 bees.py', shell=True)
            print(bh)
            break
