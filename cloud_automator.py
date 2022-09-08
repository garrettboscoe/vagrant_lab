#!/usr/bin/env python3.10

#author - @libertyunix

#Import our modules
import sys
import os
import subprocess
import time
import keyboard

#Create a banner
banner = """

 _______  _        _______           ______     _______          _________ _______  _______  _______ _________ _______  _______ 
(  ____ \( \      (  ___  )|\     /|(  __  \   (  ___  )|\     /|\__   __/(  ___  )(       )(  ___  )\__   __/(  ___  )(  ____ )
| (    \/| (      | (   ) || )   ( || (  \  )  | (   ) || )   ( |   ) (   | (   ) || () () || (   ) |   ) (   | (   ) || (    )|
| |      | |      | |   | || |   | || |   ) |  | (___) || |   | |   | |   | |   | || || || || (___) |   | |   | |   | || (____)|
| |      | |      | |   | || |   | || |   | |  |  ___  || |   | |   | |   | |   | || |(_)| ||  ___  |   | |   | |   | ||     __)
| |      | |      | |   | || |   | || |   ) |  | (   ) || |   | |   | |   | |   | || |   | || (   ) |   | |   | |   | || (\ (   
| (____/\| (____/\| (___) || (___) || (__/  )  | )   ( || (___) |   | |   | (___) || )   ( || )   ( |   | |   | (___) || ) \ \__
(_______/(_______/(_______)(_______)(______/   |/     \|(_______)   )_(   (_______)|/     \||/     \|   )_(   (_______)|/   \__/

================== A Tool for Automating the Borning Stuff in the Cloud ==============
                          Please Select An Option Below
======================================================================================
[1] 
[2] 
[3] 
[4] 
[5] 
[6] 
[7] 
[8] 
[9] 
[10] 
[99] 
======================================================================================
"""

if not os.geteuid()==0:
    sys.exit('This script must be run as root! Try sudo python cloud-automator.py')

loop=True
while loop:
    print(banner)
    x = input ("Select An Option:")
    if x == 1:
        print("Hello")

    elif x == 2:
        print ("Executing T1156 - BashRC")

    elif x == 3:
        print ("Executing T1166 - Setuid and Setgid")
    
    elif x == 4:
        print ("Executing T1009 - Binary Padding")
 

    elif x == 5:
        print ("Executing T1040 - Network Sniffing")
 

    elif x == 6:
        print ("Executing T1087 - Account Discovery")

    elif x == 7:
        print ("Executing T1002 - Data Compressed")

    elif x == 8:
        print ("Executing T1132 - Data Encoding")
        time.sleep(1)
    elif x == 9:
        print("Hello")
    elif x == 10:
        print("Cleaning this bad mother up")     
    elif x == 99:
        quit()