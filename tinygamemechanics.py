from csv_helper import *
from effectiveness_helper import *
from battleandstatcalculations import *
from pprint import pprint
import random
import time

pokemoveslist = {'Charizard': ['Air slash','Flamethrower','Dragon breath','Heat wave'],
'Greninja': ['Surf','Ice beam','Water shuriken','Dark pulse'],
'Raichu': ['Thunderbolt','Swift','Electro ball','Thunder wave'],
'Lucario': ['Aura sphere','Close combat','Meteor mash','Thunder punch'],
'Empoleon': ['Ice beam','Surf','Flash cannon','Hydro pump'],
'Gyarados': ['Waterfall','Thrash','Crunch','Outrage'],
'Smeargle': ['Sketch','Sketch','Sketch','Sketch'],
'Steelix': ['Crunch','Earthquake','Iron head','Stone edge'],
'Ho-oh': ['Sacred fire','Shadow ball','Earth power','Thunderbolt'],
'Talonflame': ['Acrobatics','Brave bird','Flare blitz','Swords dance'],
'Probopass': ['Stone edge','Thunderbolt','Thunder wave','Flash cannon'],
'Genesect': ['X-scissor','Bug buzz','Thunderbolt','Shadow claw'],
'Blissey': ['Double-edge','Thunder punch','Sing','Soft-boiled'],
'Crobat': ['Acrobatics','Cross poison','Zen headbutt','Confuse ray'],
'Golurk': ['Earthquake','Hammer arm','Shadow ball','Shadow punch'],
'Shiftry': ['Leaf blade','Throat chop','X-scissor','Swords dance'],
'Pinsir': ['X-scissor','Swords dance','Guillotine','Close combat'],
'Ampharos': ['Thunderbolt','Dragon pulse','Signal beam','Zap cannon'],
'Bidoof': ['Swords dance','Super fang','Crunch','Hyper fang'],
'Clawitzer': ['Aura sphere','Surf','Flash cannon','Sludge wave']}

pokelist = ['Charizard', 'Greninja', 'Raichu', 'Lucario', 'Empoleon', 'Gyarados', 'Smeargle', 'Steelix', 'Ho-oh', 'Talonflame', 'Probopass', 'Genesect', 'Blissey', 'Crobat', 'Golurk', 'Shiftry', 'Pinsir', 'Ampharos', 'Bidoof', 'Clawitzer']

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

logofile = open('logo2.txt')
logo = logofile.read()

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
    if s[0] >= 'a' and s[0] <= 'z':
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

def gamewait(n):
    i = 0
    while i < n:
        print('.\n')
        i += 1
        time.sleep(0.8)


def printpoke():
    string = ''
    i = 1
    for keys in pokemoveslist.keys():
        string += str(i) + '. ' + keys + '\n'
        i += 1
    print(string)

def printpokemoves(pokemon):
    string = ''
    i = 1
    for x in pokemoveslist[pokemon]:
        string += str(i) + '. ' + x + '\n'
        i += 1
    print(string)

def effectivenessmessage(effectiveness):
    if effectiveness == 0:
        print('It was not effective...')
    if effectiveness > 1:
        print('It was super effective!')
    if effectiveness < 1:
        print('It was not very effective...')


def removespacelower(s):
    lowered = lowercase(s)
    fixed = lowered.replace(' ', '')
    fixed = fixed.replace('-', '')
    return fixed
