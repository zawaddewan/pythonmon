from csv_helper import *
from effectiveness_helper import *
from battleandstatcalculations import *
from tinygamemechanics import *
from pprint import pprint
import random
import time

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
        printpoke()
        chosenpokemon = ''
        while chosenpokemon not in pokelist:
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
                                time.sleep(0.3)
                                print('You do not have enough pokedollars to purchase the item.')
                            else:
                                time.sleep(0.3)
                                bag['Pokedollars'] -= price
                                bag['Potions'] += purchase
                                print('You have purchased ' + str(purchase) + ' potions(s).')
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
                                time.sleep(0.3)
                                print('You do not have enough pokedollars to purchase the item.')
                            else:
                                time.sleep(0.3)
                                bag['Pokedollars'] -= price
                                bag['Super potions'] += purchase
                                print('You have purchased ' + str(purchase) + ' super potion(s).')
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
                                time.sleep(0.3)
                                print('You do not have enough pokedollars to purchase the item.')
                            else:
                                time.sleep(0.3)
                                bag['Pokedollars'] -= price
                                bag['Hyper Potions'] += purchase
                                print('You have purchased ' + str(purchase) + ' hyper potions(s).')

            if gamechoice == 'Search': #Searchs for pokemon
                weather = 'None' #Resets weather
                enemypokemon = random.choice(pokelist)
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
                    #Choosing pokemon move and calculating damage
                    while chosenmove not in pokemoveslist[chosenpokemon]:
                        chosenmove = spellcheck(input())
                    chosenmovefinder = movesdictfinal[removespacelower(chosenmove)] #Gives data for chosenmove
                    chosenmovetype = typeidtotype(chosenmovefinder['type_id']) #Gives move type
                    chosentypes = [chosentruestats['Type 1'], chosentruestats['Type 2']] #Makes a list of chosen pokemon's types
                    enemytypes = [chosentruestats['Type 1'], chosentruestats['Type 2']]
                    if chosenmovefinder['damage_class_id'] == 2:
                        chosenburn = burnmodcalc(chosentruestats['nonvolatile'])
                        chosendamage = damagecalc(chosentruestats['Attack'], enemytruestats['Defense'], chosenmovefinder['power'], chosentruestats['atkstage'], enemytruestats['defstage'],weather, chosenburn, chosenmovetype, chosentypes, enemytypes)
                    if chosenmovefinder['damage_class_id'] == 3:
                        chosenburn = 1
                        chosendamage = damagecalc(chosentruestats['Sp. Atk'], enemytruestats['Sp. Def'], chosenmovefinder['power'], chosentruestats['spatkstage'], enemytruestats['spdefstage'], weather, chosenburn, chosenmovetype, chosentypes, enemytypes)
                    #Choosing enemy pokemon move and calculating damage
                    enemymove = random.choice(pokemoveslist[enemypokemon])
                    enemymovefinder = movesdictfinal[removespacelower(enemymove)]
                    enemymovetype = typeidtotype(enemymovefinder['type_id'])
                    if enemymovefinder['damage_class_id'] == 2:
                        enemyburn = burnmodcalc(enemytruestats['nonvolatile'])
                        enemydamage = damagecalc(enemytruestats['Attack'], enemytruestats['Defense'], enemymovefinder['power'], enemytruestats['atkstage'], chosentruestats['defstage'], weather, enemyburn, enemymovetype, enemytypes, chosentypes)
                    if enemymovefinder['damage_class_id'] == 3:
                        enemyburn = 1
                        enemydamage = damagecalc(enemytruestats['Sp. Atk'], chosentruestats['Sp. Def'], enemymovefinder['power'], enemytruestats['spatkstage'], chosentruestats['spdefstage'], weather, enemyburn, enemymovetype, enemytypes, chosentypes)



gamestart()
