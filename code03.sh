#!/bin/bash

# Script: File Permissions
# Author: Deontae Carter
# Date of latest revision: 3/15/2023
# Purpose: Create a bash script that alters file permissions of everything in a directory.


# Prompts user for input directory path.

read -p "Type in the directory path you would like to edit permissions on?" Directory

# Prompts user for input permissions number

read -p "Type the command code to change the permissions" chmod 777

# Navigates to the directory input by the user and changes all files inside it to the input setting.

ls -l "$Directory"

# Prints to the screen the directory contents and the new permissions settings of everything in the directory.

chmod -R "$Code" "$Directory"

#end