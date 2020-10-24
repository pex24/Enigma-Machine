import os

os.system('cls')

with open('MenuScreen.txt','r') as ms:
    for lines in ms:
        print(lines.strip('\n'))

input()
os.system('cls')

with open('WelcomeScreen.txt', 'r') as ws:
    for lines in ws:
        print(lines.strip('\n'))

input()
os.system('cls')

with open('InfoScreen.txt', 'r') as info:
    for lines in info:
        print(lines.strip('\n'))

input()
os.system('cls')

with open('EncryptScreen.txt', 'r') as info:
    for lines in info:
        print(lines.strip('\n'))

message = input('')
os.system('cls')

with open('DecryptScreen.txt', 'r') as info:
    for lines in info:
        print(lines.strip('\n'))

input()
os.system('cls')

with open('OutputScreen.txt', 'r') as info:
    for lines in info:
        print(lines.strip('\n'))

input()
os.system('cls')

with open('ExitScreen.txt', 'r') as info:
    for lines in info:
        print(lines.strip('\n'))

input(exit())