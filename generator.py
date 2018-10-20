"""
This program generates values for a charSheet object and then outputs the result.
Date:   10/19/18
Author: rogandley
"""

import random as r
import array as arr
import genLib

def main():
    print("DnD 5e Character Generator\n")

    stats = createStats()

main()




def rollTheDice():
    # generate a number based on 4d6 drop lowest
    rollsArray = []
    for x in range(4):
        rollsArray.append(r.randint(1,6))
    # remove the maximum rolled number from the array
    rollsArray.pop(rollsArray.index(max(rollsArray)))
    value = sum(rollsArray)
    # return the sum
    return value


"""
Class to hold the stat array for a character
"""

class Stats():
    def __init__(self, stre, dex, con, inte, wis, cha):
        self.stre = stre
        self.dex = dex
        self.con = con
        self.inte = inte
        self.wis = wis
        self.cha = cha

def setStats(stats, stre, dex, con, inte, wis, cha):
    stats.str = stre
    stats.dex = dex
    stats.con = con
    stats.int = inte
    stats.wis = wis
    stats.cha = cha