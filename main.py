from csv_helper import *
from effectiveness_helper import *
from pprint import pprint
import random
import time

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
    #Starting menu
    print(logo)
    time.sleep(1)
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
        time.sleep(0.3)
        print('Welcome to the World of Pythonmon!')
        time.sleep(1)
        print('Select your Pokemon:')
        time.sleep(1)
        print(makepokemonchoice(pokemonlist))
        chosenpokemon = ''
        while chosenpokemon not in pokemonlist:
            chosenpokemon = spellcheck(input())
        chosenbasestats = pokemondictfinal[chosenpokemon]
        chosenbasestats['nature'] = random.choice(naturelist)
        randomEViv(chosenbasestats)
        chosentruestats = calctruestats(chosenbasestats)
        giveothervalues(chosentruestats)
        bag = {'Pokedollars': 500, 'Potions': 0, 'Super potions': 0, 'Hyper potions': 0}
        gamestate = True
        #Starts the game
        while gamestate == True:
            time.sleep(1)
            print('> Search\n> View bag\n> Pokecenter\n> Pokeshop\n> End')
            gamechoice = ''
            while gamechoice not in ['End', 'Search', 'Pokecenter', 'Pokeshop', 'View bag']:
                gamechoice = spellcheck(input())
            time.sleep(1)

            if gamechoice == 'End': #Ends the game
                gamestate = False

            if gamechoice == 'View bag':
                print('Pokedollars' + ': ' + str(bag['Pokedollars']))
                print('Potions' + ': ' + str(bag['Potions']))
                print('Super potions' + ': ' + str(bag['Super potions']))
                print('Hyper potions' + ': ' + str(bag['Hyper potions']))

            if gamechoice == 'Pokecenter': #Pokecenter option
                gamewait(1)
                print('What would you like to do?')
                pokecenteroption = ''
                while pokecenteroption != 'Leave':
                    time.sleep(0.5)
                    print('> Heal\n> Leave')
                    pokecenteroption = spellcheck(input())
                    if pokecenteroption ==  'Heal':
                        gamewait(4)
                        chosentruestats['HP'] = chosentruestats['MAXHP']
                        print('Your pokemon has been healed.')

            if gamechoice == 'Pokeshop':
                gamewait(1)
                print('What would you like to buy?')
                pokeshopoption = ''
                while pokeshopoption != 'Leave':
                    time.sleep(0.5)
                    print('> Potion\n> Super potion\n> Hyper potion\n> Leave')
                    pokeshopoption = spellcheck(input())
                    price = 0
                    purchase = 0.1
                    if pokeshopoption == 'Potion':
                        time.sleep(0.5)
                        print('Potions restore 20 HP.')
                        print('How many would you like to buy?')
                        while isinstance(purchase, int) != True:
                            try:
                                purchase = int(input())
                            except:
                                print('That is not a valid number.')
                        if purchase > 0:
                            price = purchase*100
                            if bag['Pokedollars'] < price:
                                print('You do not have enough pokedollars to purchase the item.')
                            else:
                                bag['Pokedollars'] -= price
                                bag['Potions'] += purchase
                    if pokeshopoption == 'Super potion':
                        time.sleep(0.5)
                        print('Super potions restore 60 HP.')
                        print('How many would you like to buy?')
                        while isinstance(purchase, int) != True:
                            try:
                                purchase = int(input())
                            except:
                                print('That is not a valid number.')
                        if purchase > 0:
                            price = purchase*250
                            if bag['Pokedollars'] < price:
                                print('You do not have enough pokedollars to purchase the item.')
                            else:
                                bag['Pokedollars'] -= price
                                bag['Super potions'] += purchase
                    if pokeshopoption == 'Hyper potion':
                        time.sleep(0.5)
                        print('Hyper potions restore 120 HP.')
                        print('How many would you like to buy?')
                        while isinstance(purchase, int) != True:
                            try:
                                purchase = int(input())
                            except:
                                print('That is not a valid number.')
                        if purchase > 0:
                            price = purchase*400
                            if bag['Pokedollars'] < price:
                                print('You do not have enough pokedollars to purchase the item.')
                            else:
                                bag['Pokedollars'] -= price
                                bag['Hyper Potions'] += purchase

            if gamechoice == 'Search': #Searchs for pokemon
                weather = 'None' #Resets weather
                enemypokemon = random.choice(pokemonlist)
                enemybasestats = pokemondictfinal[enemypokemon]
                enemybasestats['nature'] = random.choice(naturelist)
                randomEViv(enemybasestats)
                enemytruestats = calctruestats(enemybasestats)
                giveothervalues(enemytruestats)
                gamewait(3)
                print("You've encountered a wild " + str(enemypokemon) + '.')
                time.sleep(0.5)
                print('What do you want to do?')
                print('> Fight\n> Bag\n> Run')
                battleoption = ''
                while battleoption not in ['Fight', 'Bag', 'Run']:
                    battleoption = spellcheck(input())
                if battleoption == 'Fight':
                    time.sleep(0.5)
                    printpokemoves(chosenpokemon)
                    chosenmove = ''
                    while chosenmove not in pokemoveslist[chosenpokemon]:
                        chosenmove = spellcheck(input())
                    chosenmovefinder = movesdictfinal[removespacelower(chosenmove)] #Gives data for chosenmove
                    chosenmovetype = typeidtotype(chosenmovefinder['type_id']) #Gives move type
                    chosentypes = [chosentruestats['Type 1'], chosentruestats['Type 2']] #Makes a list of chosen pokemon's types
                    enemytypes = [chosentruestats['Type 1'], chosentruestats['Type 2']]
                    if chosenmovefinder['damage_class_id'] == 2:
                        chosenburn = burnmodcalc(chosentruestats['nonvolatile'])
                        chosendamage = damagecalc(chosentruestats['Attack'], enemytruestats['Defense'], chosenmovefinder['power'], chosentruestats['atkstage'], weather, chosenburn, chosenmovetype, chosentypes, enemytypes)
                    if chosenmovefinder['damage_class_id'] == 3:
                        chosenburn = 1
                        chosendamage = damagecalc(chosentruestats['Sp. Atk'], enemytruestats['Sp. Def'], chosenmovefinder['power'], chosentruestats['spatkstage'], weather, chosenburn, chosenmovetype, chosentypes, enemytypes)



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

def damagecalc(attack, enemydefense, pow, atkstage, weather, burn, movetype, attackertypes, defendertypes):
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



naturelist = [0, 1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]

def gamewait(n):
    i = 0
    while i < n:
        print('.\n')
        i += 1
        time.sleep(0.8)


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

def printpokemoves(pokemon):
    string = ''
    for x in pokemoveslist[pokemon]:
        string += '> ' + x + '\n'
    print(string)

pokemoveslist = {'Charizard': ['Air slash','Flamethrower','Dragon breath','Heat wave'],
'Greninja': ['Surf','Ice beam','Water shuriken','Dark pulse'],
'Raichu': ['Thunderbolt','Swift','Electro ball','Thunder wave'],
'Lucario': ['Aura sphere','Close combat','Meteor mash','Thunder punch'],
'Empoleon': ['Ice beam','Surf','Flash cannon','Hydro pump']}

def removespacelower(s):
    lowered = lowercase(s)
    fixed = lowered.replace(' ', '')
    return fixed

gamestart()
