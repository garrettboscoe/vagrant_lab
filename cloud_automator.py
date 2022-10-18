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
[1] Create AWS Bucket
[2] Delete AWS Bucket
[3] List AWS Buckets
[4] Scan all reserved TCP ports on a website
[5] 
[6] 
[7] 
[8] 
[9] 
[10] 
[99] End Program
======================================================================================
"""

if not os.geteuid()==0:
    sys.exit('This script must be run as root! Try sudo python cloud-automator.py')

loop=True
while loop:
    print(banner)
    x = input ("Select An Option:")
    if x == '1':
        print("[1] Create Bucket")
        bucketName = input("What would you like to name the bucket?\n")
        bucketRegion = input("Which region would you like to use?\n")
        createBucketCommand = "aws s3api create-bucket --bucket "+ bucketName + " --region " + bucketRegion + ""
        os.system(createBucketCommand)

        

    elif x == '2':
        print ("[2] Delete Bucket")
        deleteBucketName = input("What is the name of the bucket you would like to delete?\n")
        deleteRegionName = input("Which region is the bucket you would like to delete located?\n")
        os.system("aws s3api delete-bucket --bucket " + deleteBucketName + " --region " + deleteRegionName +"")


    elif x == '3':
        print("[3] List Buckets")
        os.system("aws s3api list-buckets --no-cli-pager")
    
    elif x == '4':
        print ("[4] Scan all reserved ports on a website")
        websiteName = input("What website would you like to scan? (Recommended - scanme.nmap.org\n)")
        os.system("nmap -v scanme.nmap.org")

 
    elif x == '5':
        print ("Executing T1040 - Network Sniffing")
 

    elif x == '6':
        print ("Executing T1087 - Account Discovery")

    elif x == '7':
        print ("Executing T1002 - Data Compressed")

    elif x == '8':
        print ("Executing T1132 - Data Encoding")
        time.sleep(1)

    elif x == '9':
        print("Hello")

    elif x == '10':
        print("Cleaning this up")  

    elif x == '99':
        quit()
