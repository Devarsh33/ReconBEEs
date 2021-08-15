from requests import get
from colors import *
import subprocess

if __name__ == '__main__':

    while True:

        print()
        ip = input('''%sEnter IP : %s''' % (green, end))

        try:
            dirty_response = get('https://censys.io/ipv4/%s/raw' % ip).text
            clean_response = dirty_response.replace('&#34;', '"')
            response = clean_response.split('<code class="json">')[1].split('</code>')[0]
            print(response + '\n')

        except:

            print("%s Invalid IP%s" % (bad, end))
        print()
        again = input('''%sWould you like to another scan yes(y)/no(n) : %s''' % (green, end))
        if again == "y" or again == "Y":
            print()
        else:
            bh = subprocess.run('python3 bheem.py', shell=True)
            print(bh)
            break
