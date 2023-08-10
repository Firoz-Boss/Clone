#!/bin/python3
#author:
#_______________import modules_______________
from os import system as cmd
from time import sleep as slp
from random import randint as rint
from random import choice as rsrt
#_______________Basic Colours___________________
red = "\033[ 1 ; 31m"
green = "\033[ 1 ; 32m"
white = "\033[ 1 ; 37m"
blue = "\033[ 1 ; 35m"
# Define the list numX
numX = []
#_______________________LOGO_____________________
def logo():
    cmd("clear")
    print(f"""{white}    {white}""")
    print(f"{white}--------------------------------------------------------------------------")
    print(f" 		  [ {green} + {white}] Tool Name : Firoz Ahmed")
    print(f" 		  [  {green} + {white}] Tool Version : 0.0.1")
    print(f" 		  [  {green} + {white}] Creator Whatsapp : +8801871528249")
    print(f"{white}--------------------------------------------------------------------------")
def random_number():
    logo()
    print(f" {red} Input valid BD sim code")
    print(f" {green} Example : {white} 018, 017, 013, 019, 016, 015")
    try:
        code = int(number)
    except:
        print(f" {red} WRONG INPUT, TRY AGAIN")
        main()
    try:
        number = int(input(f" {green} [+] Cloning Limit"))
    except:
        limit = 5000

    for i in range(limit):
        number = number + 1
        numX.append(number)
    print(numX)
    main()

#_________________Main Menu__________________
def main():
    logo()
    print(f" {green} 01 {white} Random Clone")
    print(f" {green} 01 {white}  ")
    print(f" {green} 01 {white}  ")
    print(f" {green} 01 {white}  ")
    print(f" {green} 01 {white}  ")
    print(f" {white}--------------------------------------------------------------------------")
    mch = input(f" [{green}>>{white}] Choose an option: ")
    if mch in ["1", "01"]:
        random_number()
    else:
        slp(1)
        main()

main()
