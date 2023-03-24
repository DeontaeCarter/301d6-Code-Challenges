#!/usr/bin/env python3

# Get user input and convert to lowercase
hero = input("Who is the lamest superhero?: ").lower()

# Define variables for comparison
worst_hero1 = "cyclops"
worst_hero2 = "wolverine"

# Check if user input matches the first worst hero
if hero == worst_hero1:
    print("He is useless")

# Check if user input matches the second worst hero
if hero == worst_hero2:
    print("He is also weak")

# If user input does not match either worst hero
elif hero != worst_hero1 and hero != worst_hero2:
    print("Why are they on the team?")

# If all other conditions are not met
else:
    print("They are the lamest")
