import subprocess
from requests import get
from colors import bad, info, red, green, end

if __name__ == '__main__':

    while True:

        print()
        inp = input('''%sEnter IP : %s''' % (green, end))
        honey = 'https://api.shodan.io/labs/honeyscore/%s?key=C23OXE0bVMrul2YeqcL7zxb6jZ4pj2by' % inp
        try:
            result = get(honey).text
        except:
            result = None
            print('%s No information available' % bad + '\n')
        if result:
            try:
                if float(result) < 0.5:
                    color = green
                else:
                    color = red
                probability = str(float(result) * 10)
                print()
                print('%s Honeypot Probabilty: %s%s%%%s' %
                      (info, color, probability, end) + '\n')
            except:

                print()
                print('''%sInvalid IP%s''' % (red, end))

            print()
            again = input('''%sWould you like to another scan yes(y)/no(n) : %s''' % (green, end))
            if again == "y" or again == "Y":
                print()
            else:
                bh = subprocess.run('python3 bheem.py', shell=True)
                print(bh)
                break
