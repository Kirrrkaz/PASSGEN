import requests, os, sys, time, itertools
from requests import get


time.sleep(2)
os.system("bash rq.sh")
def menu() :
    print("\033[91m1. \033[92mGenerator\033[0m")
    print("\033[91m2. \033[92mMashHack\033[0m")
    print("\033[91m3. \033[92mExit\033[0m")
def control() :
    ctrl = input("What you want to do : ")
    if ctrl == "1" :
        os.system("clear")
        gen()
    elif ctrl == "2" :
        os.system("clear")
        mh()
    elif ctrl == "3" :
        print("exit...")
        time.sleep(2)
        exit()
    else :
        print("\033[91mInvalid number\033[0m")


def gen():
    print("\033[91m \033[92m╔═══╗╔══╗╔══╗╔══╗╔═══╗╔═══╗╔╗ ╔╗\033[0m")
    print("\033[91m \033[92m║╔═╗║║╔╗║║╔═╝║╔═╝║╔══╝║╔══╝║╚═╝║\033[0m")
    print("\033[91m \033[92m║╚═╝║║╚╝║║╚═╗║╚═╗║║╔═╗║╚══╗║╔╗ ║\033[0m")
    print("\033[91m \033[92m║╔══╝║╔╗║╚═╗║╚═╗║║║╚╗║║╔══╝║║╚╗║\033[0m")
    print("\033[91m \033[92m║║   ║║║║╔═╝║╔═╝║║╚═╝║║╚══╗║║ ║║\033[0m")
    print("\033[91m \033[92m╚╝   ╚╝╚╝╚══╝╚══╝╚═══╝╚═══╝╚╝ ╚╝\033[0m")

    def split(s):
        return [char for char in password]

    password = str(input('pass: '))
    tailpass = str(input('tail-pass: '))
    MyList = [password]
    lenght = len(password)

    NewPass = split(password)

    def rSubset(NewPass):
        return list(itertools.permutations(NewPass))
    NewPass = (rSubset(NewPass))
    
    f = open('file.txt', 'w')

    for i in NewPass:
        line = ''.join(str(x) for x in i)
        line = line + tailpass
        f.write(line + '\n')
    f.close()
    print('succes!')
    time.sleep(1)
    print('Exit to main menu...')
    time.sleep(1)
    os.system("clear")
    menu()
    control()

 
os.system("clear")
print("\033[94m########################## \033[31mVr. 3.0\033[0m \033[94m#########################  ")
print("\033[1;96mCoded by github.com/Kirrrkaz\033[0m")

ip = get("https://api.ipify.org").text
ip_c = input("\033[95;107mDo you want to see your current ip ? : \033[0m").lower()
if ip_c == "yes" or ip_c == "y" :
   print(f"\033[1;93mYou are currently using with ip :\033[0m \033[91;107m{ip}\033[0m ")
elif ip_c == "no" or ip_c == "n" :
   print("\033[93;101mi hope you know what you are doing. :) \033[0m")
else :
   print("invalid option!! type yes or no ")
menu()
control()
