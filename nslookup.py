import subprocess
from requests import get
from colors import *

if __name__ == '__main__':

    while True:

        print()
        inp = input('''%sEnter URL : %s''' % (green, end))
        result = get('http://api.hackertarget.com/dnslookup/?q=' + inp).text
        print()
        print(f'%s{result}%s' % (yellow, end))
        print()
        again = input('''%sWould you like to another scan yes(y)/no(n) : %s''' % (green, end))
        if again == "y" or again == "Y":
            print()
        else:
            bh = subprocess.run('python3 bheem.py', shell=True)
            print(bh)
            break
