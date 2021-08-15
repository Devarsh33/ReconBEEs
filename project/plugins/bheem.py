import subprocess
from colors import *
import sys
import os


def banner():
    print('''

%s██████╗ ██╗  ██╗███████╗███████╗███╗   ███╗%s     %s-------------------------------------------%s
%s██╔══██╗██║  ██║██╔════╝██╔════╝████╗ ████║%s     %s[ Created by Devarsh Parmar(STARLORD3307) ]%s
%s██████╔╝███████║█████╗  █████╗  ██╔████╔██║%s     %s-------------------------------------------%s
%s██╔══██╗██╔══██║██╔══╝  ██╔══╝  ██║╚██╔╝██║%s     %s-------------------------------------------%s
%s██████╔╝██║  ██║███████╗███████╗██║ ╚═╝ ██║%s      %s[ Brought to you by www.spinthehack.in ]%s
%s╚═════╝ ╚═╝  ╚═╝╚══════╝╚══════╝╚═╝     ╚═╝%s     %s-------------------------------------------%s
        %s(An Advance Recon Tool)%s		                      %sYoutube : Spin The Hack%s          

        ''' % (
        yellow, end, red, end, yellow, end, green, end, yellow, end, red, end, yellow, end, red, end, yellow, end,
        green, end, yellow, end, red, end, red, end, red, end))


def menu():
    print('''
    ----------------------------------------------------
    %s1.%s %sFind a Target for me%s
    %s2.%s %sBasic Recon%s
    %s3.%s %sAdvance Recon%s
    %s4.%s %sCensys Scan%s
    %s5.%s %sDetect CMS%s
    %s6.%s %sDetect Honeypot%s
    %s7.%s %sDetect WAF(Web APP Firewall)%s
    %s8.%s %sNSlookup%s
    %s9.%s %sReverseIP%s
    %s10.%s %sFind Brokenlinks%s
    %s11.%s %sFind SQLi%s
    %s12.%s %sFind XSS%s
    %s13.%s %sAdd API for advance recon%s
    %s14.%s %sQuit%s
    ----------------------------------------------------
    ''' % (red, end, green, end, red, end, green, end, red, end, green, end, red, end, green, end,
           red, end, green, end, red, end, green, end, red, end, green, end, red, end, green, end,
           red, end, green, end, red, end, green, end, red, end, green, end, red, end, green, end, red, end, green,
           end, red, end, green, end))


def suroot():
    if os.geteuid() != 0:
        exit("%sYou need to run this script as a root, try with su command and%s %sdon't run this script with sudo%s" % (yellow, end, red, end))


if __name__ == '__main__':
    suroot()
    banner()
    menu()
    inp = int(input("Enter Your Choice : "))
    try:
        operations = ['target', 'basic', 'advance', 'censys', 'detectCMS', 'detecthoneypot', 'detectWAF', 'nslookup',
                      'reverseip', 'brokenlink', 'sqli', 'xss', 'API', 'quitt']
        if inp == 14:
            subprocess.run("kill $(pgrep -f 'python3 bheem.py')", shell=True)
        else:
            n = operations[inp - 1]
            subprocess.run(f'python3 {n}.py', shell=True)

    except:

        print()
        print("%s%s Enter Value between 1 to 14%s" % (bad, red, end))
        bh = subprocess.run('python3 bheem.py', shell=True)
        print(bh)
