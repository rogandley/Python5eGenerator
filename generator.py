"""
This program generates values for a charSheet object and then outputs the result.
Date:   10/19/18
Author: rogandley
"""

import random
import genLib

def main():
    print("DnD 5e Character Generator\n")








def rollTheDice():
    # generate a number based on 4d6 drop lowest
    return


"""
Class to hold the stat array for a character
"""

class Stats():
    _slots = ((int, 'str'), (int, 'dex'), (int, 'con'), (int, 'int'), (int, 'wis'), (int, 'cha'))

def createStats():
    return Stats(0, 0, 0, 0, 0, 0)

def setStats(stats, str, dex, con, int, wis, cha):
    stats.str = str
    stats.dex = dex
    stats.con = con
    stats.int = int
    stats.wis = wis
    stats.cha = cha