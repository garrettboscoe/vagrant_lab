#!/usr/bin/env python3.10

#author - @libertyunix

#Import our modules
import sys
import os
import subprocess
import time
import keyboard

os.system("curl 'https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip' -o 'awscliv2.zip')
os.system("unzip awscliv2.zip")
os.system("sudo ./aws/install")

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
[5] Determine operating system using an IP Address
[6] Determine the top ports on an IP address
[7] Scan ports on an IP address (TCP SYN scan)
[8] 
[9] Run Vagrant
[10] Destroy Vagrant
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
        os.system("nmap -v " + websiteName + "")

 
    elif x == '5':
        print("[5] Operating system scan")
        osipAddress = input("What IP address would you like to scan?")
        os.system("nmap -O " + osipAddress + "")
 

    elif x == '6':
        print ("[6] Determine the top ports on an IP address")
        topipAddress = input("What IP address would you like to scan?")
        scanNum = input("How many of the top ports would you like to scan?")
        os.system("nmap --top-ports " + scanNum + " " + topipAddress + "")

    elif x == '7':
        print ("[7] Scan ports on an IP address (TCP SYN scan)")
        scanipAddress = input("What IP address would you like to scan?")
        os.system("nmap -sS " + scanipAddress + "")

    elif x == '8':
        print("[8] Initialize Vagrant")
        os.system("sudo vagrant init")

    elif x == '9':
        print("[9] Run vagrant")
        os.system("vagrant up")

    elif x == '10':
        print("[10] Vagrant destroy")
        os.system("vagrant destroy")

    elif x == '99':
        quit()
