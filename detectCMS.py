import subprocess
import builtwith
from colors import *

if __name__ == '__main__':

    while True:

        print()
        url = input('''%sEnter URL%s(%s Type with http:// or https:// %s)%s : %s''' % (green, end, red, end, green, end))

        try:

            print()
            website = builtwith.parse(url)

            for key, value in website.items():
                print(key + ":", ", ".join(value))

        except:

            print()
            print(f"%s CMS not found....!! %s" % (bad, end))

        print()
        again = input('''%sWould you like to enter another API yes(y)/no(n) : %s''' % (green, end))
        if again == "y" or again == "Y":
            print()
        else:
            bh = subprocess.run('python3 bees.py', shell=True)
            print(bh)
            break
