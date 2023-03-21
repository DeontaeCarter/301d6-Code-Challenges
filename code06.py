#!/usr/bin/env python3

import os

# Execute the `whoami` command and capture the output
my_name = os.system("whoami")
print(my_name)

# Execute the `ip a` command and capture the output
address = os.system("ip a")
print(address)

# Execute the `lshw -short` command and capture the output
extract = os.system("lshw -short")
print(extract)

#The code at the top is what I came up with and but it doesn't work as expected^^ so I asked chat GPT to help

#This is the ChatGpt updated code.

import os

# Use os.popen() to execute the `whoami` command and capture its output
my_name = os.popen("whoami").read().strip()
print(my_name)

# Use os.popen() to execute the `ip a` command and capture its output
address = os.popen("ip a").read().strip()
print(address)

# Use os.popen() to execute the `lshw -short` command and capture its output
extract = os.popen("lshw -short").read().strip()
print(extract)
