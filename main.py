from csv_helper import *
import time
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

logofile = open('logo2.txt')
logo = logofile.read()

pokemonlist = ['Charizard', 'Greninja', 'Raichu', 'Lucario', 'Empoleon']
lowercasepoke = list(map(lowercase, pokemonlist))

def makepokemonchoice(list):
    i = 0
    string = ''
    while i < len(list):
        string += '> ' + list[i] + '\n'
        i += 1
    return string

def gamestart():
    print(logo)
    time.sleep(1)
    print('> Play')
    print('> Credits')
    option = ''
    while option not in ['credits', 'play']:
        option = lowercase(input())
    if option ==  'credits':
        print('Charizard ASCII art: https://www.asciiart.eu/video-games/pokemon')
        while option != 'play':
            option = lowercase(input())
    if option == 'play':
        print('Welcome to the World of Pythonmon!')
        time.sleep(1)
        print('Select your Pokemon:')
        time.sleep(1)
        print(makepokemonchoice(pokemonlist))
        chosenpokemon = ''
        while chosenpokemon not in lowercasepoke:
            chosenpokemon = lowercase(input())

gamestart()

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
