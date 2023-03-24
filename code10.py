#!/usr/bin/env python3

#!/usr/bin/env python3

# # Create a new file if it does not exist
# f = open("demofile.txt", "w")

# # How to open a file
# f = open("demofile.txt")

# # How to open a file and read it
# f = open("demofile.txt", "r")
# print(f.read())

# # How to return the five first characters of a file
# f = open("demofile.txt", "r")
# print(f.read(5))

# # Close a file when you're finished
# f = open("demofile.txt", "r")
# print(f.readline())


# # main
# import os
# # Create a new file if it does not exist
# x = open("X-Men.txt", "w")
# # Append three lines
# x = open("X-Men.txt", "a")
# x.write("Storm is the best \n")
# x.write("Storm is the weather Goddess \n")
# x.write("Winds heed my command!")
# # Print the first line
# x = open("X-Men.txt", "r")
# print(x.read(1))
# # Close a file when you're finished
# x = open("X-Men.txt", "r")
# print(x.readline())
# #Delete the file
# os.remove("X-Men.txt")
# # End


import os

# Create a new file if it does not exist
with open("X-Men.txt", "w") as x:
    # Append three lines
    x.write("Storm is the best \n")
    x.write("Storm is the weather Goddess \n")
    x.write("Winds heed my command!")

# Print the first line
with open("X-Men.txt", "r") as x:
    print(x.readline())

# Delete the file
os.remove("X-Men.txt")
