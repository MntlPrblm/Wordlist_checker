import os
from time import sleep
from urllib.request import urlopen

def clear():
    if os.name == "posix":
        _ = os.system('clear')
    else:
        _ = os.system('cls')

def start():
    users_password = input("Please enter password to check: ")
    wordlist = input("Enter path to wordlist: ")
    if os.path.exists(wordlist) == False:
        clear()
        print("Wordlist not found")
        sleep(3)
        start()
    f = open(wordlist, "r", encoding="ISO-8859-1")
    wordlist = f.read().splitlines()
    f.close()
    print("Checking...")
    for password in wordlist:
        if password == users_password:
            print("Password in wordlist")
            quit()
    clear()
    print("Password not in wordlist")



if __name__=='__main__':
    start()
