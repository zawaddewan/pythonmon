from csv_helper import *
from pprint import pprint
import random

def lowercase(s):
    newstring = ''
    i = 0
    while i < len(s):
        if s[i] >= 'A' and s[i] <= 'Z':
            newstring += chr(ord(s[i]) + 32)
        else:
            newstring += s[i]
        i += 1
    return newstring

def forceupper(s):
    newstring = ''
    if s[0] > 'a' and s[0] < 'z':
        newstring += chr(ord(s[0]) - 32)
    else:
        newstring += s[0]
    i = 1
    while i < len(s):
        newstring += s[i]
        i += 1
    return newstring

def spellcheck(s):
    return forceupper(lowercase(s))

logofile = open('logo2.txt')
logo = logofile.read()

pokemonlist = ['Charizard', 'Greninja', 'Raichu', 'Lucario', 'Empoleon']

def makepokemonchoice(list):
    i = 0
    string = ''
    while i < len(list):
        string += '> ' + list[i] + '\n'
        i += 1
    return string

def gamestart():
    print(logo)
    print('> Play')
    print('> Credits')
    option = ''
    while option not in ['Credits', 'Play']:
        option = spellcheck(input())
    if option ==  'Credits':
        print('Charizard ASCII art: https://www.asciiart.eu/video-games/pokemon')
        while option != 'Play':
            option = spellcheck(input())
    if option == 'Play':
        print('Welcome to the World of Pythonmon!')
        print('Select your Pokemon:')
        print(makepokemonchoice(pokemonlist))
        chosenpokemon = ''
        while chosenpokemon not in pokemonlist:
            chosenpokemon = spellcheck(input())
        chosenbasestats = pokemondictfinal[chosenpokemon]
        chosenbasestats['nature'] = random.choice(naturelist)
        randomEViv(chosenbasestats)
        chosentruestats = calctruestats(chosenbasestats)
        gamestate = True
        while gamestate == True:
            print('> Search\n> Pokecenter\n> End')
            gamechoice = ''
            while gamechoice not in ['End', 'Search', 'Pokecenter', 'Pokeshop']:
                gamechoice = spellcheck(input())
            if gamechoice == 'end':
                gamestate = False
            if gamechoice == 'search':
                enemypokemon = random.choice(pokemonlist)
                enemybasestats = pokemondictfinal[enemypokemon]
                enemybasestats['nature'] = random.choice(naturelist)
                randomEViv(enemybasestats)
                enemytruestats = calctruestats(enemybasestats)
                gamewait(3)
                print("You've encountered a wild " + str(enemypokemon) + '.')
                print('What do you want to do?')
                print('> Fight\n> Bag\n> Run')
                battleoption = ''
                while battleoption not in ['Fight', 'Bag', 'Run']:
                    battleoption = spellcheck(input())
                if battleoption = 'Fight':
                    printpokemoves(chosenpokemon)
                    chosenmove = ''
                    while chosenmove not in pokemoveslist[chosenpokemon]:
                        chosenmove = spellcheck(input())

                print(chosentruestats, enemytruestats)



movesfile = open('moves.csv')
moves = movesfile.read()
movesheader = get_headers(moves)
movesdata = get_data(moves)
movesdict = make_dict(movesdata)
#Below is the final moves data as a dictionary
movesdictfinal = combine_dict(movesdict, movesheader)

pokemonfile = open('pokemon.csv')
pokemon = pokemonfile.read()
pokemonheader = get_headers(pokemon)
pokemondata = get_data(pokemon)
pokemondict = make_dict_moves(pokemondata)
#Below is the final pokemon stats data as a dictionary
pokemondictfinal = combine_dict(pokemondict, pokemonheader)


p1nature = 0 #Later, random number generation from 0-24 will determine natures
p2nature = 0

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

def damagecalc(attack, enemydefense, pow, critmod, atkstage, weather, movetype):
    modifier = modifiercalc(weather, movetype, attackertypes, effectiveness, burn)
    damage = (((((((2 * 50) / 5) + 2) * pow * (attack * (1 + (atkstage / 2)))) / defense ) / 50) + 2) * modifier
    return damage

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

print(modifiercalc('rain', 'water', ['water', 'ground'], 1.5, 1))

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

naturelist = [0, 1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]

def gamewait(n):
    i = 0
    while i < n:
        print('.\n')
        i += 1


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

def randomEViv(dict):
    randomivs(dict)
    randomevs(dict)

def calctruestats(dict):
    newdict = {}
    newdict['Type 1'] = dict['Type 1']
    newdict['Type 2'] = dict['Type 2']

    hpstat = hpcalc(int(dict['HP']), dict['hpiv'], dict['hpev'])
    newdict['HP'] = hpstat

    atkstat = othercalc(int(dict['Attack']), dict['atkiv'], dict['atkev'], dict['nature'], 'atk')
    newdict['Attack'] = atkstat

    defstat = othercalc(int(dict['Defense']), dict['defiv'], dict['defev'], dict['nature'], 'def')
    newdict['Defense'] = defstat

    spatkstat = othercalc(int(dict['Sp. Atk']), dict['spatkiv'], dict['spatkev'], dict['nature'], 'spatk')
    newdict['Sp. Atk'] = spatkstat

    spdefstat = othercalc(int(dict['Sp. Def']), dict['spdefiv'], dict['spdefev'], dict['nature'], 'spdef')
    newdict['Sp. Def'] = spdefstat

    spdstat = othercalc(int(dict['Speed']), dict['spdiv'], dict['spdev'], dict['nature'], 'spd')
    newdict['Speed'] = spdstat

    return newdict

def printpokemoves(pokemon):
    i = 0
    for x in pokemoveslist[pokemon]:
        print('> ' + x + '\n')

gamestart()
