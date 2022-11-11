#!/bin/python3
# Written by Michael Beavitt on 08/11/2022

name = input("What is your name? \n")

if name == "Michael":
    print("Nice name!")
else:
    print("Hi, " + name + "!")

age = int(input("What is your age? \n"))

if age >= 20 and age < 30:
    print("Hi young grasshopper!")
elif age >= 30 and age <40:
    print("You're a proper adult!")
else:
    print("You're getting on a bit...!")

colour = input("What is your colour? \n")

if colour.lower() == "green":
    print("I like that colour too")
else:
    print("hmm, that's ok I guess...")

likeornot = input("Do you like python? \n")

if likeornot.lower() == "yes":
    print("Me too!")
elif likeornot.lower() == "no":
    print("That's heresy!")
else:
    print("weird answer...")

worldflat = input("Is the world flat? \n")

if worldflat.lower() == "yes":
    print("you're an oddball")
elif worldflat.lower() == "maybe":
    print("you're on the fence??")
elif worldflat.lower() == "no":
    print("That's correct!")
else:
    print("weird answer...")
