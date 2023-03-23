#!/usr/bin/env python3

lame = input("Who is the lamest?: ").lower()  # convert input to lowercase
weak = "cyclops"
weaker = "wolverine"

if lame == weak:
    print("They are useless")
    if lame == weaker:
        print("Also weak")
    else:
        print("They are useless")
elif lame != weak and lame != weaker:
    print("I don't know who that is")
else:
    print("They are not the lamest")
