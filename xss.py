from colors import *
import os
import subprocess

if __name__ == '__main__':

    while True:
        print()
        file_input = input("%sEnter the File Path Which contains subdomains : %s" % (green, end))

        f = os.path.exists(file_input)

        if f:

            sql = os.popen(f'cat {file_input} | gf xss | tee -a /root/Desktop/xss.txt').read()
            print(sql)
            print("%s%s Your output Saved in /root/Desktop as a xss.txt%s" % (info, red, end))

        else:

            print()
            print("%s%s File not Found...!!%s" % (bad, red, end))

        print()
        again = input('''%sWould you like to another scan ? yes(y)/no(n) : %s''' % (green, end))
        if again == "y" or again == "Y":
            print()
        else:
            bh = subprocess.run('python3 bheem.py', shell=True)
            print(bh)
            break
