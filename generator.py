"""
This program generates values for a charSheet object and then outputs the result.
Date:   10/19/18
Author: rogandley
"""

import random as r
import array as arr
from genLib.Stats import Stats
from genLib import nameLists

def rollTheDice():
    # generate a number based on 4d6 drop lowest
    rollsArray = []
    for x in range(4):
        rollsArray.append(r.randint(1,6))
    # remove the maximum rolled number from the array
    rollsArray.pop(rollsArray.index(min(rollsArray)))
    value = sum(rollsArray)
    # return the sum
    return value

def main():
    print("DnD 5e Character Generator\n")

    stats = Stats(rollTheDice(), rollTheDice(), rollTheDice(), rollTheDice(), rollTheDice(), rollTheDice())
    print("Strength:\t\t", stats.stre)
    print("Dexterity:\t\t", stats.dex)
    print("Constitution:\t", stats.con)
    print("Intelligence:\t", stats.inte)
    print("Wisdom:\t\t\t", stats.wis)
    print("Charisma:\t\t", stats.cha)

main()
