from csv_helper import *

print("Welcome to the world of Pythonmon!")

p1nature = 0 #Later, random number generation from 0-24 will determine natures
p2nature = 0

def hpcalc(base, IV, EV):
    return ((((2 * base + IV + (EV / 4)) * 50) / 100) + 50 + 10) // 1

def natmodcalc(nature, stat): #Calculates how a stat will be affected by the given nature
    if nature == 0 or nature == 6 or nature == nature == 12 or nature == 18 or nature == 24:
        return 1
    elif nature <= 4:
        if stat == "atk":
            return 1.1
        elif (nature == 1 and stat == "def") or (nature == 2 and stat == "spd") or (nature == 3 and stat == "spatk") or (nature == 4 and stat == "spdef"):
            return 0.9
    elif nature == 5 or nature == 7 or nature == 8 or nature == 9:
        if stat == "def":
            return 1.1
        elif (nature == 5 and stat == "atk") or (nature == 7 and stat == "spd") or (nature == 8 and stat == "spatk") or (nature == 9 and stat == "spdef"):
            return 0.9
    elif nature == 10 or nature == 11 or nature == 13 or nature == 14:
        if stat == "spd":
            return 1.1
        elif (nature == 10 and stat == "atk") or (nature == 11 and stat == "def") or (nature == 13 and stat == "spatk") or (nature == 14 and stat == "spdef"):
            return 0.9
    elif nature == 15 or nature == 16 or nature == 17 or nature == 19:
        if stat == "spatk":
            return 1.1
        elif (nature == 15 and stat == "atk") or (nature == 16 and stat == "def") or (nature == 17 and stat == "spd") or (nature == 19 and stat == "spdef"):
            return 0.9
    elif nature >= 20 and nature <= 23:
        if stat == "spdef":
            return 1.1
        elif (nature == 21 and stat == "atk") or (nature == 22 and stat == "def") or (nature == 22 and stat == "spd") or (nature == 23 and stat == "spatk"):
            return 0.9
    
def othercalc(base, IV, EV, nature, stat):
    nmod = natmodcalc(nature, stat)
    return ((((2 * base + IV + (EV / 4)) * 50) / 100) + 5) * nmod
    
