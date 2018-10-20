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