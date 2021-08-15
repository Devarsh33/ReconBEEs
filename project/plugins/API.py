import subprocess
from colors import *
import requests


# Taking input

def censys():
    while True:
        while True:
            print()
            censysapi = input('''%sEnter censys API key : %s''' % (green, end))
            if not censysapi:
                print('''%sCan not be empty API%s''' % (bad, end))
            else:
                break
        while True:
            censyssapi = input("%sEnter censys Secret API key : %s" % (green, end))
            if not censyssapi:
                print('''%sCan not be empty API%s''' % (bad, end))
            else:
                res = requests.get("https://censys.io/api/v1/data", auth=(censysapi, censyssapi))
                if res.status_code != 200:
                    bol = False
                else:
                    bol = True
                break

        if bol:
            a_file = open("config.ini", "r")
            list_of_lines = a_file.readlines()
            list_of_lines[140] = f"apikey ={censysapi}\n"
            a_file = open("config.ini", "w")
            a_file.writelines(list_of_lines)
            a_file.close()
            b_file = open("config1.ini", "r")
            list_of_lines1 = b_file.readlines()
            list_of_lines1[140] = f"apikey ={censysapi}\n"
            b_file = open("config1.ini", "w")
            b_file.writelines(list_of_lines1)
            b_file.close()
            a_file = open("config.ini", "r")
            list_of_lines = a_file.readlines()
            list_of_lines[141] = f"secret ={censyssapi}\n"
            a_file = open("config.ini", "w")
            a_file.writelines(list_of_lines)
            a_file.close()
            b_file = open("config1.ini", "r")
            list_of_lines1 = b_file.readlines()
            list_of_lines1[141] = f"apikey ={censyssapi}\n"
            b_file = open("config1.ini", "w")
            b_file.writelines(list_of_lines1)
            b_file.close()
            break

        else:
            print()
            print("%s%s Unknown API keys Please Enter Correct API keys%s" % (bad, red, end))

def alienvault():
    while True:
        print()
        alienvaultapi = input('''%sEnter alienvault API key : %s''' % (green, end))
        if not alienvaultapi:
            print('''%sCan not be empty API%s''' % (bad, end))
        else:
            a_file = open("config.ini", "r")
            list_of_lines = a_file.readlines()
            list_of_lines[120] = f"apikey ={alienvaultapi}\n"
            a_file = open("config.ini", "w")
            a_file.writelines(list_of_lines)
            a_file.close()
            b_file = open("config1.ini", "r")
            list_of_lines1 = b_file.readlines()
            list_of_lines1[120] = f"apikey ={alienvaultapi}\n"
            b_file = open("config1.ini", "w")
            b_file.writelines(list_of_lines1)
            b_file.close()
            break


def virustotal():
    while True:
        print()
        virustotalapi = input('''%sEnter virustotal API key : %s''' % (green, end))
        if not virustotalapi:
            print('''%sCan not be empty API%s''' % (bad, end))
        else:
            a_file = open("config.ini", "r")
            list_of_lines = a_file.readlines()
            list_of_lines[262] = f"apikey ={virustotalapi}\n"
            a_file = open("config.ini", "w")
            a_file.writelines(list_of_lines)
            a_file.close()
            b_file = open("config1.ini", "r")
            list_of_lines1 = b_file.readlines()
            list_of_lines1[262] = f"apikey ={virustotalapi}\n"
            b_file = open("config1.ini", "w")
            b_file.writelines(list_of_lines1)
            b_file.close()
            break


if __name__ == '__main__':

    while True:

        print('''
        %s1.%s %sCensys API key%s
        %s2.%s %sAlienvault API key%s
        %s3.%s %sVirustotal API key%s''' % (
            red, end, yellow, end, red, end, yellow, end, red, end, yellow, end))

        print()
        value = int(input('''%sEnter Value : %s''' % (green, end)))
        try:
            operations = [censys, alienvault, virustotal]
            operations[value - 1]()

        except:

            print()
            print("%s%s Enter Value between 1 to 4%s" % (bad, red, end))
            print()

        print()
        again = input('''%sWould you like to enter another API yes(y)/no(n) : %s''' % (green, end))

        if again == "y" or again == "Y":
            print()
        else:
            bh = subprocess.run('python3 bheem.py', shell=True)
            print(bh)
            break
