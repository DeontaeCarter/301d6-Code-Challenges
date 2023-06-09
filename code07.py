#!/usr/bin/env python3

# Import libraries

# import os

# # Declaration of variables

# ### Read user input here into a variable

# # Declaration of functions

# ### Declare a function here

# for (root, dirs, files) in os.walk("testdir"):
#     ### Add a print command here to print ==root==
#     print(root)
#     ### Add a print command here to print ==dirs==
#     print(dirs)
#     ### Add a print command here to print ==files==
#     print(files)

# Main

### Pass the variable into the function here

# End


import os

# Declare function
def generate_directory_structure(path):
    for (root, dirs, files) in os.walk(path):
        print("Root directory:", root)
        print("Sub-directories:", dirs)
        print("Files:", files)

# Get user input
path = input("Enter directory path: ")

# Call function with user input as argument
generate_directory_structure(path)
