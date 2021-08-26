import subprocess
from colors import *

if __name__ == '__main__':

    while True:
        try:
            print()

            # Entering Target name
            target = input('''%sEnter Target : %s''' % (green, end))

            # Scan with Subfinder
            scan = subprocess.run(f"subfinder -d {target} -t 100 -o /root/.config/{target}-tbasic-recon.txt",
                                  shell=True)

            print(scan)

            # Filter output with HTTPX

            filtertar = subprocess.run(f"cat /root/.config/{target}-tbasic-recon.txt | httpx -threads 200 | tee -a "
                                       f"/root/Desktop/{target}-basic-recon.txt", shell=True)

            print(filtertar)

            remt = subprocess.run(f"rm -rf /root/.config/{target}-tbasic-recon.txt", shell=True, stdout=subprocess.PIPE,
                                  stderr=subprocess.STDOUT)

            print(f"%s Your output saved in /root/Desktop/ as a {target}-basic-recon.txt %s" % (yellow, end))

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
