import subprocess
from requests import get
from colors import *

if __name__ == '__main__':

    while True:

        print()
        inp = input('''%sEnter IP : %s''' % (green, end))
        lookup = 'https://api.hackertarget.com/reverseiplookup/?q=%s' % inp
        try:
            result = get(lookup).text
            print()
            print(f'%s{result}%s' % (yellow, end))
        except:
            print('%s Invalid IP address' % bad)

        print()
        again = input('''%sWould you like to another scan yes(y)/no(n) : %s''' % (green, end))
        if again == "y" or again == "Y":
            print()
        else:
            bh = subprocess.run('python3 bees.py', shell=True)
            print(bh)
            break
