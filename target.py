import random
from googlesearch import search
from colors import *
import subprocess

if __name__ == '__main__':

    while True:
        try:
            f = open("target.txt", "r")  # open file in read mode
            lines = f.readlines()  # return all lines of the file as a list
            ran = random.randint(0, len(lines) - 1)  # return any random number
            target = lines[ran]  # return any line of text
            f.close()

            print()
            for i in search(target, tld="com", num=10, stop=10, pause=2):
                print(f'%s{i}%s' % (yellow, end))

        except BaseException as error:
            print(f'%s {error} %s' % (bad, end))

        print()
        again = input('''%sWould you like to another scan ? yes(y)/no(n) : %s''' % (green, end))
        if again == "y" or again == "Y":
            print()
        else:
            bh = subprocess.run('python3 bees.py', shell=True)
            print(bh)
            break
