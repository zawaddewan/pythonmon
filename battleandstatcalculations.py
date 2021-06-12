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

def damagecalc(move, attack, enemydefense, pow, atkstage, enemydefstage, weather, burn, movetype, attackertypes, defendertypes):
    effectiveness = calcEffectiveness(movetype, defendertypes[0], defendertypes[1])
    modifier = modifiercalc(weather, movetype, attackertypes, effectiveness, burn, move)
    damage = ((((((2 * 50) / 5) + 2) * pow * (attack * max(2, 2 + atkstage)/max(2, 2 - atkstage))) / (enemydefense * max(2, 2 + enemydefstage)/max(2, 2 - enemydefstage)) / 50) + 2) * modifier
    return int(damage // 1)

def modifiercalc(weather, movetype, attackertypes, effectiveness, burn, move):
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
    if move == 'stallbyconfusion':
        modifier *= 1
    elif move in ['Cross poison', 'Leaf blade']:
        if random.randint(0, 8) == 0:
            modifier *= 1.5
        if random.randint(0, 24) == 0:
            modifier *= 1.5
    return modifier

def typeidtotype(id):
    if id == 1:
        return 'Normal'
    if id == 2:
        return 'Fighting'
    if id == 3:
        return 'Flying'
    if id == 4:
        return 'Poison'
    if id == 5:
        return 'Ground'
    if id == 6:
        return 'Rock'
    if id == 7:
        return 'Bug'
    if id == 8:
        return 'Ghost'
    if id == 9:
        return 'Steel'
    if id == 10:
        return 'Fire'
    if id == 11:
        return 'Water'
    if id == 12:
        return 'Grass'
    if id == 13:
        return 'Electric'
    if id == 14:
        return 'Pyschic'
    if id == 15:
        return 'Ice'
    if id == 16:
        return 'Dragon'
    if id == 17:
        return 'Dark'
    if id == 18:
        return 'Fairy'

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
    dict['confused'] = False
    dict['confusedturns'] = 0
    dict['asleepturns'] = 0
    dict['randsleepturns'] = 0
    dict['flinched'] = False
    dict['outrageturns'] = 0
    dict['randoutrageturns'] = 0
    dict['thrashturns'] = 0
    dict['randthrashturns'] = 0

def randomEViv(dict):
    randomivs(dict)
    randomevs(dict)

def giveothervalues(dict, pokemon):
    givestatstages(dict)
    givestatuses(dict)
    dict['moves'] = pokemoveslist[pokemon]

def burnmodcalc(status):
    if status == 'Burned':
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

def stallfinder(pokemon, move, pokemontruestats, chosenpokemon, enemypokemon):
    stall = False
    if pokemontruestats['nonvolatile'] in ['Frozen','Asleep','Paralyzed']:
        if pokemontruestats['nonvolatile'] == 'Frozen':
            if random.randrange(0,100) < 20:
                stall = False
                pokemontruestats['nonvolatile'] = '0'
                if pokemon == 'chosen':
                    print('Your ' + chosenpokemon + ' has been thawed!')
                else:
                    print('The wild ' + enemypokemon + ' has been thawed!')
            elif move in ['Fusion flare','Flame wheel','Sacred fire','Flare blitz','Scald','Steam eruption']:
                stall = False
                pokemontruestats['nonvolatile'] = '0'
                if pokemon == 'chosen':
                    print('Your ' + chosenpokemon + ' has been thawed!')
                else:
                    print('The wild ' + enemypokemon + ' has been thawed!')
            else:
                chosenstall = True
        if pokemontruestats['nonvolatile'] == 'Asleep':
            if pokemontruestats['asleepturns'] < pokemontruestats['randsleepturns']:
                stall = True
                pokemontruestats['asleepturns'] += 1
                if pokemontruestats['asleepturns'] >= pokemontruestats['randsleepturns']:
                    pokemontruestats['asleepturns'] = 0
                    pokemontruestats['randsleepturns'] = 0
                    stall = False
                    if pokemon == 'chosen':
                        print('Your ' + chosenpokemon + ' has woken up!')
                    else:
                        print('The enemy ' + enemypokemon + ' has woken up!')
            else:
                pokemontruestats['asleepturns'] = 0
                pokemontruestats['randsleepturns'] = 0
                stall = False
                if pokemon == 'chosen':
                    print('Your ' + chosenpokemon + ' has woken up!')
                else:
                    print('The enemy ' + enemypokemon + ' has woken up!')
        if pokemontruestats['nonvolatile'] == 'Paralyzed':
            if random.randrange(0,100) < 25:
                stall = True
            else:
                stall = False
        if  pokemontruestats['confused'] == True and stall == False:
            if pokemontruestats['confusedturns'] < 2:
                if random.randange(0,3) == 0:
                    stall = 'confusion'
                    pokemontruestats['confusedturns'] += 1
                else:
                    stall = False
                    pokemontruestats['confusedturns'] += 1
            elif pokemontruestats['confusedturns'] == 5:
                stall = False
                pokemontruestats['confused'] = False
                pokemontruestats['confusedturns'] = 0
                if pokemon == 'chosen':
                    print('Your ' + chosenpokemon + ' has snapped out of confusion!')
                else:
                    print('The enemy ' + enemypokemon + ' has snapped out of confusion!')
            else:
                if random.randrange(0,100) < 20:
                    stall = False
                    pokemontruestats['confused'] = False
                    pokemontruestats['confusedturns'] = 0
                    if pokemon == 'chosen':
                        print('Your ' + chosenpokemon + ' has snapped out of confusion!')
                    else:
                        print('The enemy ' + enemypokemon + ' has snapped out of confusion!')
                else:
                    if random.randrange(0,3) == 0:
                        stall = 'confusion'
                        pokemontruestats['confusedturns'] += 1
                    else:
                        stall = False
                        pokemontruestats['confusedturns'] += 1
        if pokemontruestats['flinched'] == True and stall == False:
            stall = True


    return stall

def calcwatershuriken():
    times = 2
    random = random.randrange(0,8)
    if random in [0, 1, 2]:
        times = 2
    if random in [3, 4, 5]:
        times = 3
    if random == 6:
        times = 4
    if random == 7:
        times = 5
    return times

def consultspeciallist(pokemon, pokemontruestats, defendertruestats, chosenpokemon, enemypokemon, move, defendermove, chosenmove, enemymove):
    if pokemon == 'chosen':
        time.sleep(0.5)
        print('Your ' + chosenpokemon + ' used ' + chosenmove + '.\n')
    if pokemon == 'enemy':
        time.sleep(0.5)
        print('The wild ' + enemypokemon + ' used ' + enemymove + '.\n')
    if move == 'Swords dance':
        if pokemontruestats['atkstage'] < 5:
            pokemontruestats['atkstage'] += 2
            if pokemon == 'chosen':
                time.sleep(0.5)
                print('Your ' + chosenpokemon + "'s Attack rose sharply!\n")
            else:
                time.sleep(0.5)
                print('The wild ' + enemypokemon + "'s Attack rose sharply!\n")
        elif pokemontruestats['atkstage'] == 5:
            pokemontruestats['atkstage'] += 1
            if pokemon == 'chosen':
                time.sleep(0.5)
                print('Your ' + chosenpokemon + "'s Attack rose!\n")
            else:
                time.sleep(0.5)
                print('The wild ' + enemypokemon + "'s Attack rose!\n")
        else:
            if pokemon == 'chosen':
                time.sleep(0.5)
                print('Your ' + chosenpokemon + "'s Attack cannot be increased further.\n")
            else:
                time.sleep(0.5)
                print('The wild ' + enemypokemon + "'s Attack cannot be increased further.\n")
    if move == 'Soft-boiled':
        sbhealing = 0
        while (pokemontruestats['HP'] < pokemontruestats['MAXHP']) and (sbhealing < (0.5 * pokemontruestats['MAXHP'])):
            sbhealing += 1
            pokemontruestats['HP'] += 1
        time.sleep(1)
        if pokemon == 'chosen':
            time.sleep(0.5)
            print('Your ' + chosenpokemon + ' regained health!\n')
        else:
            time.sleep(0.5)
            print('The wild ' + enemypokemon + ' regained health!\n')
    if move == 'Sing':
        if random.randrange(0,100) < 55:
            if defendertruestats['nonvolatile'] == '0':
                defendertruestats['randsleepturns'] = random.randint(1,3)
                defendertruestats['nonvolatile'] = 'Asleep'
            else:
                if pokemon == 'enemy':
                    time.sleep(0.5)
                    print('Your ' + chosenpokemon + " is already " + pokemontruestats['nonvolatile'] + ", it can't be put to sleep!\n")
                else:
                    time.sleep(0.5)
                    print('The wild ' + enemypokemon + " is already " + pokemontruestats['nonvolatile'] + ", it can't be put to sleep!\n")
        else:
            if pokemon == 'chosen':
                time.sleep(0.5)
                print('Your ' + chosenpokemon + ' has missed.\n')
            if pokemon == 'enemy':
                time.sleep(0.5)
                print('The wild ' + enemypokemon + ' has missed.\n')
    if move == 'Sketch':
        joinedsmearglemoves = ','.join(pokemontruestats['moves'])
        replacedsmearglemoves = joinedsmearglemoves.replace('Sketch', defendermove, 1)
        newsmearglemoves = replacedsmearglemoves.split(',')
        pokemontruestats['moves'] = newsmearglemoves
        if pokemon == 'chosen':
            time.sleep(0.5)
            print('Your ' + chosenpokemon + ' has copied ' + defendermove + '.\n')
        else:
            time.sleep(0.5)
            print('The wild ' + enemypokemon + ' has copied' + defendermove + '.\n')
    if move == 'Confuse ray':
        if defendertruestats['confused'] == False:
            defendertruestats['confused'] == True
            if pokemon == 'enemy':
                time.sleep(0.5)
                print('Your ' + chosenpokemon + ' has been confused!\n')
            else:
                time.sleep(0.5)
                print('The wild ' + enemypokemon + ' has been confused!\n')
        else:
            if pokemon == 'enemy':
                time.sleep(0.5)
                print('Your ' + chosenpokemon + " is already confused, it can't be confused again!\n")
            else:
                time.sleep(0.5)
                print('The wild ' + enemypokemon + " is already confused, it can't be confused again!\n")
    if move == 'Thunder wave':
        if defendertruestats['Type 1'] in ['Electric', 'Ground'] or defendertruestats['Type 2'] in ['Electric', 'Ground']:
            if pokemon == 'enemy':
                time.sleep(0.5)
                print('Your ' + chosenpokemon + ' is unable to be paralyzed.\n')
            else:
                time.sleep(0.5)
                print('The wild ' + enemypokemon + ' is unable to be paralyzed.\n')
        elif defendertruestats['nonvolatile'] == '0':
            defendertruestats['nonvolatile'] == 'Paralyzed'
            defendertruestats['Speed'] *= 0.5
            if pokemon == 'enemy':
                time.sleep(0.5)
                print('Your ' + chosenpokemon + ' has been paralyzed!\n')
            else:
                time.sleep(0.5)
                print('The wild ' + enemypokemon + ' has been paralyzed!\n')
        else:
            if pokemon == 'enemy':
                time.sleep(0.5)
                print('Your ' + chosenpokemon + ' is already ' + lowercase(defendertruestats['nonvolatile']) + ', it cannot be paralyzed.\n')
            else:
                time.sleep(0.5)
                print('The wild ' + enemypokemon + ' is already ' + lowercase(defendertruestats['nonvolatile']) + ', it cannot be paralyzed.\n')




def setstatuseffects(pokemon, movefinder, defendertypes, pokemontruestats, defendertruestats, chosenpokemon, enemypokemon):
    if movefinder['effect_id'] == 'PAR':
        if 'Electric' in defendertypes:
            if pokemon == 'enemy':
                time.sleep(0.5)
                print('Your ' + chosenpokemon + ' is unable to be paralyzed.\n')
            else:
                time.sleep(0.5)
                print('The wild ' + enemypokemon + ' is unable to be paralyzed.\n')
        elif random.randrange(0,100) < movefinder['effect_chance']:
            if typeidtotype(movefinder['type_id']) == 'Electric':
                if 'Ground' in defendertypes:
                    if pokemon == 'enemy':
                        time.sleep(0.5)
                        print('Your ' + chosenpokemon + ' is unable to be paralyzed.\n')
                    else:
                        time.sleep(0.5)
                        print('The wild ' + enemypokemon + ' is unable to be paralyzed.\n')
            elif defendertruestats['nonvolatile'] == '0':
                defendertruestats['nonvolatile'] == 'Paralyzed'
                defendertruestats['Speed'] *= 0.5
                if pokemon == 'enemy':
                    time.sleep(0.5)
                    print('Your ' + chosenpokemon + ' has been paralyzed!\n')
                else:
                    time.sleep(0.5)
                    print('The wild ' + enemypokemon + ' has been paralyzed!\n')
            else:
                if pokemon == 'enemy':
                    time.sleep(0.5)
                    print('Your ' + chosenpokemon + ' is already ' + lowercase(defendertruestats['nonvolatile']) + ', it cannot be paralyzed.\n')
                else:
                    time.sleep(0.5)
                    print('The wild ' + enemypokemon + ' is already ' + lowercase(defendertruestats['nonvolatile']) + ', it cannot be paralyzed.\n')
    if movefinder['effect_id'] == 'BRN':
        if 'Fire' in defendertypes:
             if pokemon == 'enemy':
                 time.sleep(0.5)
                 print('Your ' + chosenpokemon + ' is unable to be burned.\n')
             else:
                 time.sleep(0.5)
                 print('The wild ' + enemypokemon + ' is unable to be burned.\n')
        elif random.randrange(0,100) < movefinder['effect_chance']:
            if defendertruestats['nonvolatile'] == '0':
                defendertruestats['nonvolatile'] == 'Burned'
                if pokemon == 'enemy':
                    time.sleep(0.5)
                    print('Your ' + chosenpokemon + ' has been burned!\n')
                else:
                    time.sleep(0.5)
                    print('The wild ' + enemypokemon + ' has been burned!\n')
            else:
                if pokemon == 'enemy':
                    time.sleep(0.5)
                    print('Your ' + chosenpokemon + ' is already ' + lowercase(defendertruestats['nonvolatile']) + ', it cannot be burned.\n')
                else:
                    time.sleep(0.5)
                    print('The wild ' + enemypokemon + ' is already ' + lowercase(defendertruestats['nonvolatile']) + ', it cannot be burned.\n')
    if movefinder['effect_id'] == 'FRZ':
        if 'Ice' in defendertypes:
             if pokemon == 'enemy':
                 time.sleep(0.5)
                 print('Your ' + chosenpokemon + ' is unable to be frozen.\n')
             else:
                 time.sleep(0.5)
                 print('The wild ' + enemypokemon + ' is unable to be frozen.\n')
        elif random.randrange(0,100) < movefinder['effect_chance']:
            if defendertruestats['nonvolatile'] == '0':
                defendertruestats['nonvolatile'] == 'Frozen'
                if pokemon == 'enemy':
                    time.sleep(0.5)
                    print('Your ' + chosenpokemon + ' has been frozen!\n')
                else:
                    time.sleep(0.5)
                    print('The wild ' + enemypokemon + ' has been frozen!\n')
            else:
                if pokemon == 'enemy':
                    time.sleep(0.5)
                    print('Your ' + chosenpokemon + ' is already ' + lowercase(defendertruestats['nonvolatile']) + ', it cannot be frozen.\n')
                else:
                    time.sleep(0.5)
                    print('The wild ' + enemypokemon + ' is already ' + lowercase(defendertruestats['nonvolatile']) + ', it cannot be frozen.\n')
    if movefinder['effect_id'] == 'FLN':
        if random.randrange(0,100) < movefinder['effect_chance']:
            if defendertruestats['flinched'] == False:
                defendertruestats['flinched'] == True
    if movefinder['effect_id'] == 'CON':
        if random.randrange(0,100) < movefinder['effect_chance']:
            if defendertruestats['confused'] == False:
                defendertruestats['confused'] == True
                if pokemon == 'enemy':
                    time.sleep(0.5)
                    print('Your ' + chosenpokemon + ' has been confused!\n')
                else:
                    time.sleep(0.5)
                    print('The wild ' + enemypokemon + ' has been confused!\n')
            else:
                if pokemon == 'enemy':
                    time.sleep(0.5)
                    print('Your ' + chosenpokemon + " is already confused, it can't be confused again!\n")
                else:
                    time.sleep(0.5)
                    print('The wild ' + enemypokemon + " is already confused, it can't be confused again!\n")
    if movefinder['effect_id'] == 'PSN':
        if 'Poison' in defendertypes or 'Steel' in defendertypes:
             if pokemon == 'enemy':
                 time.sleep(0.5)
                 print('Your ' + chosenpokemon + ' is unable to be poisoned.\n')
             else:
                 time.sleep(0.5)
                 print('The wild ' + enemypokemon + ' is unable to be poisoned.\n')
        if random.randrange(0,100) < movefinder['effect_chance']:
            if defendertruestats['nonvolatile'] == '0':
                defendertruestats['nonvolatile'] == 'Poisoned'
                if pokemon == 'enemy':
                    time.sleep(0.5)
                    print('Your ' + chosenpokemon + ' has been poisoned!\n')
                else:
                    time.sleep(0.5)
                    print('The wild ' + enemypokemon + ' has been poisoned!\n')
            else:
                if pokemon == 'enemy':
                    time.sleep(0.5)
                    print('Your ' + chosenpokemon + ' is already ' + lowercase(defendertruestats['nonvolatile']) + ', it cannot be poisoned.\n')
                else:
                    time.sleep(0.5)
                    print('The wild ' + enemypokemon + ' is already ' + lowercase(defendertruestats['nonvolatile']) + ', it cannot be poisoned.\n')
    stagechanges = [movefinder['stat_change1'], movefinder['stat_change2']]
    if 'atkup' in stagechanges:
        if random.randrange(0,100) < movefinder['stat_chance']:
            if pokemon == 'chosen':
                if movefinder['affects_who'] == 'player':
                    if pokemontruestats['atkstage'] < 6:
                        pokemontruestats['atkstage'] += 1
                        time.sleep(0.5)
                        print('Your ' + chosenpokemon + "'s Attack rose!\n")
                    else:
                        time.sleep(0.5)
                        print('Your ' + chosenpokemon + "'s Attack cannot be increased further.\n")
                if movefinder['affects_who'] == 'opponent':
                    if defendertruestats['atkstage'] < 6:
                        defendertruestats['atkstage'] += 1
                        time.sleep(0.5)
                        print('The wild ' + enemypokemon + "'s Attack rose!\n")
                    else:
                        time.sleep(0.5)
                        print('The wild ' + enemypokemon + "'s Attack cannot be increased further.\n")
            if pokemon == 'enemy':
                if movefinder['affects_who'] == 'player':
                    if pokemontruestats['atkstage'] < 6:
                        pokemontruestats['atkstage'] += 1
                        time.sleep(0.5)
                        print('The wild ' + enemypokemon + "'s Attack rose!\n")
                    else:
                        time.sleep(0.5)
                        print('The wild ' + enemypokemon + "'s Attack cannot be increased further.\n")
                if movefinder['affects_who'] == 'opponent':
                    if defendertruestats['atkstage'] < 6:
                        defendertruestats['atkstage'] += 1
                        time.sleep(0.5)
                        print('Your ' + chosenpokemon + "'s Attack rose!\n")
                    else:
                        time.sleep(0.5)
                        print('Your ' + chosenpokemon + "'s Attack cannot be increased further.\n")
    if 'spdefdown' in stagechanges:
        if random.randrange(0,100) < movefinder['stat_chance']:
            if pokemon == 'chosen':
                if movefinder['affects_who'] == 'player':
                    if pokemontruestats['spdefstage'] > -6:
                        pokemontruestats['spdefstage'] -= 1
                        time.sleep(0.5)
                        print('Your ' + chosenpokemon + "'s Special Defense fell!\n")
                    else:
                        time.sleep(0.5)
                        print('Your ' + chosenpokemon + "'s Special Defense cannot be decreased further.\n")
                if movefinder['affects_who'] == 'opponent':
                    if defendertruestats['spdefstage'] > -6:
                        defendertruestats['spdefstage'] -= 1
                        time.sleep(0.5)
                        print('The wild ' + enemypokemon + "'s Special Defense fell!\n")
                    else:
                        time.sleep(0.5)
                        print('The wild ' + enemypokemon + "'s Special Defense cannot be decreased further.\n")
            if pokemon == 'enemy':
                if movefinder['affects_who'] == 'player':
                    if pokemontruestats['spdefstage'] > -6:
                        pokemontruestats['spdefstage'] -= 1
                        time.sleep(0.5)
                        print('The wild ' + enemypokemon + "'s Special Defense fell!\n")
                    else:
                        time.sleep(0.5)
                        print('The wild ' + enemypokemon + "'s Special Defense cannot be decreased further.\n")
                if movefinder['affects_who'] == 'opponent':
                    if defendertruestats['spdefstage'] > -6:
                        defendertruestats['spdefstage'] -= 1
                        time.sleep(0.5)
                        print('Your ' + chosenpokemon + "'s Special Defense fell!\n")
                    else:
                        time.sleep(0.5)
                        print('Your ' + chosenpokemon + "'s Special Defense cannot be decreased further.\n")
    if 'spddown' in stagechanges:
        if random.randrange(0,100) < movefinder['stat_chance']:
            if pokemon == 'chosen':
                if movefinder['affects_who'] == 'player':
                    if pokemontruestats['spdstage'] > -6:
                        pokemontruestats['spdstage'] -= 1
                        time.sleep(0.5)
                        print('Your ' + chosenpokemon + "'s Speed fell!\n")
                    else:
                        time.sleep(0.5)
                        print('Your ' + chosenpokemon + "'s Speed cannot be decreased further.\n")
                if movefinder['affects_who'] == 'opponent':
                    if defendertruestats['spdstage'] > -6:
                        defendertruestats['spdstage'] -= 1
                        time.sleep(0.5)
                        print('The wild ' + enemypokemon + "'s Speed fell!\n")
                    else:
                        time.sleep(0.5)
                        print('The wild ' + enemypokemon + "'s Speed cannot be decreased further.\n")
            if pokemon == 'enemy':
                if movefinder['affects_who'] == 'player':
                    if pokemontruestats['spdstage'] > -6:
                        pokemontruestats['spdstage'] -= 1
                        time.sleep(0.5)
                        print('The wild ' + enemypokemon + "'s Speed fell!\n")
                    else:
                        time.sleep(0.5)
                        print('The wild ' + enemypokemon + "'s Speed cannot be decreased further.\n")
                if movefinder['affects_who'] == 'opponent':
                    if defendertruestats['spdstage'] > -6:
                        defendertruestats['spdstage'] -= 1
                        time.sleep(0.5)
                        print('Your ' + chosenpokemon + "'s Speed fell!\n")
                    else:
                        time.sleep(0.5)
                        print('Your ' + chosenpokemon + "'s Speed cannot be decreased further.\n")
    if 'defdown' in stagechanges:
        if random.randrange(0,100) < movefinder['stat_chance']:
            if pokemon == 'chosen':
                if movefinder['affects_who'] == 'player':
                    if pokemontruestats['defstage'] > -6:
                        pokemontruestats['defstage'] -= 1
                        time.sleep(0.5)
                        print('Your ' + chosenpokemon + "'s Defense fell!\n")
                    else:
                        time.sleep(0.5)
                        print('Your ' + chosenpokemon + "'s Defense cannot be decreased further.\n")
                if movefinder['affects_who'] == 'opponent':
                    if defendertruestats['defstage'] > -6:
                        defendertruestats['defstage'] -= 1
                        time.sleep(0.5)
                        print('The wild ' + enemypokemon + "'s Defense fell!\n")
                    else:
                        time.sleep(0.5)
                        print('The wild ' + enemypokemon + "'s Defense cannot be decreased further.\n")
            if pokemon == 'enemy':
                if movefinder['affects_who'] == 'player':
                    if pokemontruestats['defstage'] > -6:
                        pokemontruestats['defstage'] -= 1
                        time.sleep(0.5)
                        print('The wild ' + enemypokemon + "'s Defense fell!\n")
                    else:
                        time.sleep(0.5)
                        print('The wild ' + enemypokemon + "'s Defense cannot be decreased further.\n")
                if movefinder['affects_who'] == 'opponent':
                    if defendertruestats['defstage'] > -6:
                        defendertruestats['defstage'] -= 1
                        time.sleep(0.5)
                        print('Your ' + chosenpokemon + "'s Defense fell!\n")
                    else:
                        time.sleep(0.5)
                        print('Your ' + chosenpokemon + "'s Defense cannot be decreased further.\n")





def replaceasmove(outrageorthrash):
    newlist = []
    if outrageorthrash == 'outrage':
        newlist = ['Outrage', 'Outrage', 'Outrage', 'Outrage']
    if outrageorthrash == 'thrash':
        newlist = ['Thrash', 'Thrash', 'Thrash', 'Thrash']
    return newlist

def outrager(pokemon, pokemontruestats, chosenpokemon, enemypokemon):
    if pokemon == 'chosen':
        if pokemontruestats['outrageturns'] == 0:
            pokemontruestats['moves'] = replaceasmove('outrage')
            pokemontruestats['randoutrageturns'] = random.randint(2,3)
            pokemontruestats['outrageturns'] += 1
        elif pokemontruestats['outrageturns'] == pokemontruestats['randoutrageturns']:
            pokemontruestats['outrageturns'] = 0
            pokemontruestats['randoutrageturns'] = 0
            pokemontruestats['moves'] = pokemoveslist[chosenpokemon]
            if pokemontruestats['confused'] == False:
                pokemontruestats['confused'] = True
                time.sleep(0.5)
                print('Your ' + chosenpokemon + ' has become confused!\n')
        else:
            pokemontruestats['outrageturns'] += 1
    if pokemon == 'enemy':
        if pokemontruestats['outrageturns'] == 0:
            pokemontruestats['moves'] = replaceasmove('outrage')
            pokemontruestats['randoutrageturns'] = random.randint(2,3)
            pokemontruestats['outrageturns'] += 1
        elif pokemontruestats['outrageturns'] == pokemontruestats['randoutrageturns']:
            pokemontruestats['outrageturns'] = 0
            pokemontruestats['randoutrageturns'] = 0
            pokemontruestats['moves'] = pokemoveslist[enemypokemon]
            if pokemontruestats['confused'] == False:
                pokemontruestats['confused'] = True
                time.sleep(0.5)
                print('The wild ' + enemypokemon + ' has become confused!\n')
        else:
            pokemontruestats['outrageturns'] += 1

def thrasher(pokemon, pokemontruestats, chosenpokemon, enemypokemon):
    if pokemon == 'chosen':
        if pokemontruestats['thrashturns'] == 0:
            pokemontruestats['moves'] = replaceasmove('thrash')
            pokemontruestats['randthrashturns'] = random.randint(2,3)
            pokemontruestats['thrashturns'] += 1
        elif pokemontruestats['thrashturns'] == pokemontruestats['randthrashturns']:
            pokemontruestats['thrashturns'] = 0
            pokemontruestats['randthrashturns'] = 0
            pokemontruestats['moves'] = pokemoveslist[chosenpokemon]
            if pokemontruestats['confused'] == False:
                pokemontruestats['confused'] = True
                time.sleep(0.5)
                print('Your ' + chosenpokemon + ' has become confused!\n')
        else:
            pokemontruestats['thrashturns'] += 1
    if pokemon == 'enemy':
        if pokemontruestats['thrashturns'] == 0:
            pokemontruestats['moves'] = replaceasmove('thrash')
            pokemontruestats['randthrashturns'] = random.randint(2,3)
            pokemontruestats['thrashturns'] += 1
        elif pokemontruestats['thrashturns'] == pokemontruestats['randthrashturns']:
            pokemontruestats['thrashturns'] = 0
            pokemontruestats['randthrashturns'] = 0
            pokemontruestats['moves'] = pokemoveslist[enemypokemon]
            if pokemontruestats['confused'] == False:
                pokemontruestats['confused'] = True
                time.sleep(0.5)
                print('The wild ' + enemypokemon + ' has become confused!\n')
        else:
            pokemontruestats['thrashturns'] += 1


def applyeffects(chosentruestats, enemytruestats, chosenpokemon, enemypokemon):
    if chosentruestats['nonvolatile'] == 'Burned':
        time.sleep(0.5)
        print('Your ' + chosenpokemon + ' is hurt by its burn!')
        chosentruestats['HP'] -= int((chosentruestats['MAXHP'] / 16) // 1)
    if chosentruestats['nonvolatile'] == 'Poisoned':
        time.sleep(0.5)
        print('Your ' + chosenpokemon + ' is hurt by its poison!')
        chosentruestats['HP'] -= int((chosentruestats['MAXHP'] / 8) // 1)
    if enemytruestats['nonvolatile'] == 'Burned':
        time.sleep(0.5)
        print('The wild ' + enemypokemon + ' is hurt by its burn!')
        chosentruestats['HP'] -= int((chosentruestats['MAXHP'] / 16) // 1)
    if enemytruestats['nonvolatile'] == 'Poisoned':
        time.sleep(0.5)
        print('The wild ' + enemypokemon + ' is hurt by its poison!')
        chosentruestats['HP'] -= int((chosentruestats['MAXHP'] / 8) // 1)
    chosentruestats['flinched'] = False
    enemytruestats['flinched'] = False

def resetstatus(dict):
    dict['confused'] = False
    dict['confusedturns'] = 0
    dict['asleepturns'] = 0
    dict['randsleepturns'] = 0
    dict['flinched'] = False
    dict['outrageturns'] = 0
    dict['randoutrageturns'] = 0
    dict['thrashturns'] = 0
    dict['randthrashturns'] = 0
    dict['atkstage'] = 0
    dict['defstage'] = 0
    dict['spatkstage'] = 0
    dict['spdefstage'] = 0
    dict['spdstage'] = 0
