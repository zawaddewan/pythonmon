from csv_helper import *
from effectiveness_helper import *
from tinygamemechanics import *
from pprint import pprint
import random
import time

naturelist = [0, 1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]

def hpcalc(base, IV, EV):
    return (((2 * base + IV + ((EV / 4) // 1)) * 50) / 100) // 1 + 50 + 10

def natmodcalc(nature, stat): #Calculates how a stat will be affected by the given nature
    if nature == 0 or nature == 6 or nature == nature == 12 or nature == 18 or nature == 24:
        return 1
    elif nature <= 4:
        if stat == 'atk':
            return 1.1
        elif (nature == 1 and stat == 'def') or (nature == 2 and stat == 'spd') or (nature == 3 and stat == 'spatk') or (nature == 4 and stat == 'spdef'):
            return 0.9
        else:
            return 1
    elif nature == 5 or nature == 7 or nature == 8 or nature == 9:
        if stat == 'def':
            return 1.1
        elif (nature == 5 and stat == 'atk') or (nature == 7 and stat == 'spd') or (nature == 8 and stat == 'spatk') or (nature == 9 and stat == 'spdef'):
            return 0.9
        else:
            return 1
    elif nature == 10 or nature == 11 or nature == 13 or nature == 14:
        if stat == 'spd':
            return 1.1
        elif (nature == 10 and stat == 'atk') or (nature == 11 and stat == 'def') or (nature == 13 and stat == 'spatk') or (nature == 14 and stat == 'spdef'):
            return 0.9
        else:
            return 1
    elif nature == 15 or nature == 16 or nature == 17 or nature == 19:
        if stat == 'spatk':
            return 1.1
        elif (nature == 15 and stat == 'atk') or (nature == 16 and stat == 'def') or (nature == 17 and stat == 'spd') or (nature == 19 and stat == 'spdef'):
            return 0.9
        else:
            return 1
    elif nature >= 20 and nature <= 23:
        if stat == 'spdef':
            return 1.1
        elif (nature == 21 and stat == 'atk') or (nature == 22 and stat == 'def') or (nature == 22 and stat == 'spd') or (nature == 23 and stat == 'spatk'):
            return 0.9
        else:
            return 1

def othercalc(base, IV, EV, nature, stat):
    nmod = natmodcalc(nature, stat)
    return (((((2 * base + IV + ((EV / 4) // 1)) * 50) / 100) // 1 + 5) * nmod) // 1

def damagecalc(attack, enemydefense, pow, atkstage, enemydefstage, weather, burn, movetype, attackertypes, defendertypes):
    effectiveness = calcEffectiveness(movetype, defendertypes[0], defendertypes[1])
    modifier = modifiercalc(weather, movetype, attackertypes, effectiveness, burn)
    damage = (((((((2 * 50) / 5) + 2) * pow * (attack * (1 + (atkstage / 2)))) / enemydefense ) / 50) + 2) * modifier
    return int(damage // 1)

def modifiercalc(weather, movetype, attackertypes, effectiveness, burn):
    modifier = 1
    if (movetype == 'water' and weather == 'rain') or (movetype == 'fire' and weather == 'harsh sunlight'):
        modifier *= 1.5
    elif (movetype == 'water' and weather == 'harsh sunlight') or (movetype == 'fire' and weather == 'rain'):
        modifier *= 0.5
    if movetype in attackertypes:
        modifier *= 1.5
    modifier *= burn
    rand = (random.randint(85, 100)) * 0.01
    modifier *= rand
    modifier *= effectiveness
    if random.randint(0, 24) == 0:
        modifier += 1.5
    return modifier

def typeidtotype(id):
    if id == 1:
        return 'normal'
    if id == 2:
        return 'fighting'
    if id == 3:
        return 'flying'
    if id == 4:
        return 'poison'
    if id == 5:
        return 'ground'
    if id == 6:
        return 'rock'
    if id == 7:
        return 'bug'
    if id == 8:
        return 'ghost'
    if id == 9:
        return 'steel'
    if id == 10:
        return 'fire'
    if id == 11:
        return 'water'
    if id == 12:
        return 'grass'
    if id == 13:
        return 'electric'
    if id == 14:
        return 'pyschic'
    if id == 15:
        return 'ice'
    if id == 16:
        return 'dragon'
    if id == 17:
        return 'dark'
    if id == 18:
        return 'fairy'

def randomivs(dict):
    dict['hpiv'] = random.randint(0, 31)
    dict['atkiv'] = random.randint(0, 31)
    dict['defiv'] = random.randint(0, 31)
    dict['spatkiv'] = random.randint(0, 31)
    dict['spdefiv'] = random.randint(0, 31)
    dict['spdiv'] = random.randint(0, 31)

def randomevs(dict):
    evlist = ['hp', 'atk', 'def', 'spatk', 'spdef', 'spd']
    totalev = 0
    dict['hpev'] = 0
    dict['atkev'] = 0
    dict['defev'] = 0
    dict['spatkev'] = 0
    dict['spdefev'] = 0
    dict['spdev'] = 0
    while totalev <= 510:
        currentev = random.choice(evlist)
        if currentev == 'hp':
            dict['hpev'] += 1
        if currentev == 'atk':
            dict['atkev'] += 1
        if currentev == 'def':
            dict['defev'] += 1
        if currentev == 'spatk':
            dict['spatkev'] += 1
        if currentev == 'spdef':
            dict['spdefev'] += 1
        if currentev == 'spd':
            dict['spdev'] += 1
        totalev += 1

def givestatstages(dict):
    dict['atkstage'] = 0
    dict['defstage'] = 0
    dict['spatkstage'] = 0
    dict['spdefstage'] = 0
    dict['spdstage'] = 0

def givestatuses(dict):
    dict['nonvolatile'] = '0'
    dict['volatile'] = []

def randomEViv(dict):
    randomivs(dict)
    randomevs(dict)

def giveothervalues(dict):
    givestatstages(dict)
    givestatuses(dict)

def burnmodcalc(status):
    if status == 'burn':
        return 0.5
    else:
        return 1

def calctruestats(dict):
    newdict = {}
    newdict['Type 1'] = dict['Type 1']
    newdict['Type 2'] = dict['Type 2']

    hpstat = int(hpcalc(int(dict['HP']), dict['hpiv'], dict['hpev']))
    newdict['MAXHP'] = hpstat
    newdict['HP'] = hpstat

    atkstat = int(othercalc(int(dict['Attack']), dict['atkiv'], dict['atkev'], dict['nature'], 'atk'))
    newdict['Attack'] = atkstat

    defstat = int(othercalc(int(dict['Defense']), dict['defiv'], dict['defev'], dict['nature'], 'def'))
    newdict['Defense'] = defstat

    spatkstat = int(othercalc(int(dict['Sp. Atk']), dict['spatkiv'], dict['spatkev'], dict['nature'], 'spatk'))
    newdict['Sp. Atk'] = spatkstat

    spdefstat = int(othercalc(int(dict['Sp. Def']), dict['spdefiv'], dict['spdefev'], dict['nature'], 'spdef'))
    newdict['Sp. Def'] = spdefstat

    spdstat = int(othercalc(int(dict['Speed']), dict['spdiv'], dict['spdev'], dict['nature'], 'spd'))
    newdict['Speed'] = spdstat

    return newdict
