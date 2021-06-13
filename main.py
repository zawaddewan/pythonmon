from csv_helper import *
from effectiveness_helper import *
from statcharts import *
from battleandstatcalculations import *
from tinygamemechanics import *
import matplotlib.pyplot as plt
from pprint import pprint
import random
import time

def gamestart():
    #Starting menu
    print(logo)
    time.sleep(1)
    option = ''
    while option not in ['1']:
        time.sleep(0.5)
        print('1. Play')
        print('2. Credits\n')
        option = input()
        if option ==  '2':
            time.sleep(0.5)
            print('Charizard ASCII art: https://www.asciiart.eu/video-games/pokemon')
            print('Pokemon CSV data: https://gist.github.com/armgilles/194bcff35001e7eb53a2a8b441e8b2c6')
            print('Moves CSV data: https://github.com/veekun/pokedex/blob/master/pokedex/data/csv/moves.csv')
    if option == '1':
        time.sleep(0.5)
        print('Welcome to the World of Pythonmon!')
        time.sleep(1)
        print('Select your Pokemon:')
        time.sleep(1)
        printpoke()
        chosenpokemon = ''
        while chosenpokemon not in ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20']:
            chosenpokemon = input()
        chosenpokemon = pokelist[int(chosenpokemon) - 1]
        chosenbasestats = pokemondictfinal[chosenpokemon]
        chosenbasestats['nature'] = random.choice(naturelist)
        randomEViv(chosenbasestats)
        chosentruestats = calctruestats(chosenbasestats)
        giveothervalues(chosentruestats, chosenpokemon)
        bag = {'Pokedollars': 500, 'Potions': 0, 'Super potions': 0, 'Hyper potions': 0}
        gamestate = True
        #Starts the game
        time.sleep(0.5)
        print("You are currently in Pythontown.")
        while gamestate == True:
            time.sleep(0.5)
            print('1. Search\n2. View bag\n3. Pokecenter\n4. Pokeshop\n5. End game\n')
            gamechoice = ''
            while gamechoice not in ['1','2','3','4','5']:
                gamechoice = input()
            time.sleep(0.5)

            if gamechoice == '5': #Ends the game
                gamestate = False

            if gamechoice == '2':
                print('Pokedollars' + ': ' + str(bag['Pokedollars']))
                print('Potions' + ': ' + str(bag['Potions']))
                print('Super potions' + ': ' + str(bag['Super potions']))
                print('Hyper potions' + ': ' + str(bag['Hyper potions']))

            if gamechoice == '3': #Pokecenter option
                gamewait(1)
                print('What would you like to do?')
                pokecenteroption = ''
                while pokecenteroption != '2':
                    time.sleep(0.5)
                    print('1. Heal\n2. Leave\n')
                    pokecenteroption = input()
                    if pokecenteroption ==  '1':
                        gamewait(4)
                        chosentruestats['HP'] = chosentruestats['MAXHP']
                        chosentruestats['nonvolatile'] = '0'
                        print('Your pokemon has been healed.')

            if gamechoice == '4': #Pokeshop option
                gamewait(1)
                print('What would you like to buy?')
                pokeshopoption = ''
                while pokeshopoption != '4':
                    time.sleep(0.5)
                    print('1. Potion\n2. Super potion\n3. Hyper potion\n4. Leave\n')
                    pokeshopoption = spellcheck(input())
                    price = 0
                    purchase = 0.1
                    if pokeshopoption == '1':
                        time.sleep(0.5)
                        print('Potions restore 20 HP and cost 100 pokedollars each.')
                        print('How many would you like to buy?')
                        while isinstance(purchase, int) != True:
                            try:
                                purchase = int(input())
                            except:
                                print('That is not a valid number.')
                        if purchase > 0:
                            price = purchase*100
                            if bag['Pokedollars'] < price:
                                time.sleep(0.5)
                                print('You do not have enough pokedollars to purchase the item.')
                            else:
                                time.sleep(0.5)
                                bag['Pokedollars'] -= price
                                bag['Potions'] += purchase
                                print('You have purchased ' + str(purchase) + ' potions(s).')
                    if pokeshopoption == '2':
                        time.sleep(0.5)
                        print('Super potions restore 60 HP and cost 250 pokedollars each.')
                        print('How many would you like to buy?')
                        while isinstance(purchase, int) != True:
                            try:
                                purchase = int(input())
                            except:
                                print('That is not a valid number.')
                        if purchase > 0:
                            price = purchase*250
                            if bag['Pokedollars'] < price:
                                time.sleep(0.5)
                                print('You do not have enough pokedollars to purchase the item.')
                            else:
                                time.sleep(0.5)
                                bag['Pokedollars'] -= price
                                bag['Super potions'] += purchase
                                print('You have purchased ' + str(purchase) + ' super potion(s).')
                    if pokeshopoption == '3':
                        time.sleep(0.5)
                        print('Hyper potions restore 120 HP and cost 400 pokedollars each.')
                        print('How many would you like to buy?')
                        while isinstance(purchase, int) != True:
                            try:
                                purchase = int(input())
                            except:
                                print('That is not a valid number.')
                        if purchase > 0:
                            price = purchase*400
                            if bag['Pokedollars'] < price:
                                time.sleep(0.5)
                                print('You do not have enough pokedollars to purchase the item.')
                            else:
                                time.sleep(0.5)
                                bag['Pokedollars'] -= price
                                bag['Hyper potions'] += purchase
                                print('You have purchased ' + str(purchase) + ' hyper potions(s).')

            if gamechoice == '1': #Searchs for pokemon
                weather = 'None' #Resets weather
                enemypokemon = random.choice(pokelist)
                enemybasestats = pokemondictfinal[enemypokemon]
                enemybasestats['nature'] = random.choice(naturelist)
                randomEViv(enemybasestats)
                enemytruestats = calctruestats(enemybasestats)
                giveothervalues(enemytruestats, enemypokemon)
                chosentypes = [chosentruestats['Type 1'], chosentruestats['Type 2']] #Makes a list of chosen pokemon's types
                enemytypes = [enemytruestats['Type 1'], enemytruestats['Type 2']]
                chosenmove = 'None'
                chosenmovefinder = {'type_id': 0, 'power': 0, 'pp': 0, 'accuracy': 0, 'priority': 0, 'damage_class_id': 0, 'effect_id': 0, 'effect_chance': 0, 'stat_change1': 0, 'stat_change2': 0, 'affects_who': 0, 'stat_stage': 0, 'stat_chance': 0} #Gives data for chosenmove
                chosenmovetype = 'None' #Gives move type
                gamewait(3)
                print("You've encountered a wild " + str(enemypokemon) + '.\n')
                battlestate = True
<<<<<<< HEAD
                plt.ion()
                statcharts(chosentruestats, chosenpokemon, enemytruestats, enemypokemon)
                hpcharts(chosentruestats, chosenpokemon, enemytruestats, enemypokemon)
                plt.show()
=======
                time.sleep(0.5)
                print('Show plots?')
                time.sleep(0.5)
                print('1. Yes\n2. No\n')
                plotoption = ''
                while plotoption not in ['1','2']:
                    plotoption = input()
                    if plotoption == '1':
                        plt.ion()
                        pokecharts(chosentruestats, chosenpokemon, enemypokemon)
                        plt.show()
>>>>>>> 8a620169a8ae8ec0fec8377a6748916167be727f
                runtimes = 1
                while battlestate == True:
                    time.sleep(0.5)
                    print('Your ' + chosenpokemon + "'s HP: " + str(chosentruestats['HP']) + '\nThe wild ' + enemypokemon + "'s HP: " + str(enemytruestats['HP']))
                    print('What do you want to do?')
                    turnend = False
                    turnendfrombattle = False
                    while turnend == False:
                        print('1. Fight\n2. Bag\n3. Run\n')
                        battleoption = ''
                        while battleoption not in ['1', '2', '3']:
                            battleoption = input()
                        if battleoption == '1':
                            time.sleep(0.5)
                            printpokemoves(chosentruestats)
                            chosenmove = ''
                            #Choosing pokemon move and calculating damage
                            while chosenmove not in ['1','2','3','4']:
                                chosenmove = input()
                            chosenmove = chosentruestats['moves'][int(chosenmove) - 1]
                            chosenmovefinder = movesdictfinal[removespacelower(chosenmove)] #Gives data for chosenmove
                            chosenmovetype = typeidtotype(chosenmovefinder['type_id']) #Gives move type
                            if chosenmovefinder['damage_class_id'] == 2:
                                chosenburn = burnmodcalc(chosentruestats['nonvolatile'])
                                chosendamage = damagecalc(chosenmove, chosentruestats['Attack'], enemytruestats['Defense'], chosenmovefinder['power'], chosentruestats['atkstage'], enemytruestats['defstage'],weather, chosenburn, chosenmovetype, chosentypes, enemytypes)
                            if chosenmovefinder['damage_class_id'] == 3:
                                chosenburn = 1
                                chosendamage = damagecalc(chosenmove, chosentruestats['Sp. Atk'], enemytruestats['Sp. Def'], chosenmovefinder['power'], chosentruestats['spatkstage'], enemytruestats['spdefstage'], weather, chosenburn, chosenmovetype, chosentypes, enemytypes)
                                #Choosing enemy pokemon move and calculating damage
                            turnend = True
                            turnendfrombattle = True
                        if battleoption == '2':
                            print('1. Potions' + ': ' + str(bag['Potions']))
                            print('2. Super potions' + ': ' + str(bag['Super potions']))
                            print('3. Hyper potions' + ': ' + str(bag['Hyper potions']))
                            print('4. Leave')
                            bagoption = ''
                            while bagoption != '4':
                                bagoption = str(input())
                                if bagoption == '1':
                                    if bag['Potions'] > 0:
                                        healing = 0
                                        while chosentruestats['HP'] < chosentruestats['MAXHP'] and healing < 20:
                                            chosentruestats['HP'] += 1
                                            healing += 1
                                        bagoption = '4'
                                        bag['Potions'] -= 1
                                        turnend = True
                                    else:
                                        print('You do not have potions.')
                                        bagoption = '4'
                                if bagoption == '2':
                                    if bag['Super potions'] > 0:
                                        healing = 0
                                        while chosentruestats['HP'] < chosentruestats['MAXHP'] and healing < 60:
                                            chosentruestats['HP'] += 1
                                            healing += 1
                                        bagoption = '4'
                                        bag['Super potions'] -= 1
                                        turnend = True
                                    else:
                                        print('You do not have super potions.')
                                        bagoption = '4'
                                if bagoption == '3':
                                    if bag['Hyper potions'] > 0:
                                        healing = 0
                                        while chosentruestats['HP'] < chosentruestats['MAXHP'] and healing < 120:
                                            chosentruestats['HP'] += 1
                                            healing += 1
                                        bagoption = '4'
                                        bag['Hyper potions'] -= 1
                                        turnend = True
                                    else:
                                        print('You do not have hyper potions.')
                                        bagoption = '4'
                                if bagoption == '4':
                                    turnend == False
                        if battleoption == '3':
                            if chosentruestats['Speed'] > enemytruestats['Speed']:
                                battlestate = False
                                time.sleep(0.5)
                                print('You got away safely!')
                                turnend = True
                            else:
                                if random.randrange(0,100) < ((chosentruestats['Speed'] * 128) / enemytruestats['Speed'] + 30 * runtimes) % 256:
                                    battlestate = False
                                    time.sleep(0.5)
                                    print('You got away safely!')
                                    turnend = True
                                else:
                                    runtimes += 1
                                    turnend = True
                                    time.sleep(0.5)
                                    print('You did not get away.')
                        #Calculations for enemy damage
                        enemymove = random.choice(pokemoveslist[enemypokemon])
                        enemymovefinder = movesdictfinal[removespacelower(enemymove)]
                        enemymovetype = typeidtotype(enemymovefinder['type_id'])
                        if enemymovefinder['damage_class_id'] == 2:
                            enemyburn = burnmodcalc(enemytruestats['nonvolatile'])
                            enemydamage = damagecalc(enemymove, enemytruestats['Attack'], enemytruestats['Defense'], enemymovefinder['power'], enemytruestats['atkstage'], chosentruestats['defstage'], weather, enemyburn, enemymovetype, enemytypes, chosentypes)
                        if enemymovefinder['damage_class_id'] == 3:
                            enemyburn = 1
                            enemydamage = damagecalc(enemymove, enemytruestats['Sp. Atk'], chosentruestats['Sp. Def'], enemymovefinder['power'], enemytruestats['spatkstage'], chosentruestats['spdefstage'], weather, enemyburn, enemymovetype, enemytypes, chosentypes)
                        #Choosing who goes first
                        chosenspeed = chosentruestats['Speed'] * (1 + (chosentruestats['spdstage'] / 2))
                        enemyspeed = enemytruestats['Speed'] * (1 + (enemytruestats['spdstage'] / 2))

                    if battlestate == False:
                        print('')

                    elif (chosenmovefinder['priority'] > enemymovefinder['priority']) or ((chosenmovefinder['priority'] == enemymovefinder['priority']) and (chosenspeed > enemyspeed)) or turnend == True: #Situation for chosen pokemon attacking first
                        chosenstall = stallfinder('chosen', chosenmove, chosentruestats, chosenpokemon, enemypokemon)

                        if turnend == False or turnendfrombattle == True:
                            if chosenstall in [True, 'confusion']: # Sends stall message
                                if chosentruestats['nonvolatile'] == 'Frozen':
                                    time.sleep(0.5)
                                    print('Your ' + chosenpokemon + ' is frozen solid!\n')
                                if chosentruestats['nonvolatile'] == 'Asleep':
                                    time.sleep(0.5)
                                    print('Your ' + chosenpokemon + ' is fast asleep.\n')
                                if chosentruestats['nonvolatile'] == 'Paralyzed':
                                    time.sleep(0.5)
                                    print('Your ' + chosenpokemon + " is paralyzed! It can't move!\n")
                                if chosenstall == 'confusion':
                                    confuseddamage = damagecalc('stallbyconfusion', chosentruestats['Attack'], chosentruestats['Defense'], 40, chosentruestats['atkstage'], chosentruestats['defstage'], weather, chosenburn, 'Normal', 'None', 'None')
                                    chosentruestats['HP'] -= confuseddamage
                                    time.sleep(0.5)
                                    print('Your ' + chosenpokemon + ' hurt itself in its confusion!\n')

                                chosenstall = False

                            elif chosenmovefinder['damage_class_id'] == 1:
                                consultspeciallist('chosen', chosentruestats, enemytruestats, chosenpokemon, enemypokemon, chosenmove, enemymove, chosenmove, enemymove) #For moves such as sing, swords dance, etc...

                            else:
                                if chosenmove == 'Guillotine':
                                    time.sleep(0.5)
                                    print('Your ' + chosenpokemon + ' used ' + chosenmove + '.\n')
                                    if random.randrange(0,100) < chosenmovefinder['accuracy']:
                                        enemytruestats['HP'] = 0
                                        time.sleep(0.5)
                                        print('The wild ' + enemypokemon + ' has fainted.\n')
                                        time.sleep(0.5)
                                        print('You have won the battle!\n')
                                        battlestate = False
                                    else:
                                        time.sleep(0.5)
                                        print('Your ' + chosenpokemon + ' has missed.\n')

                                else:
                                    time.sleep(0.5)
                                    print('Your ' + chosenpokemon + ' used ' + chosenmove + '.\n')
                                    if random.randrange(0,100) < chosenmovefinder['accuracy']:
                                        if chosenmove == 'Outrage':
                                            outrager('chosen', chosentruestats, chosenpokemon, enemypokemon)
                                        if chosenmove == 'Thrash':
                                            thrasher('chosen', chosentruestats, chosenpokemon, enemypokemon)
                                        enemytruestats['HP'] -= chosendamage
                                        time.sleep(0.5)
                                        effectivenessmessage(calcEffectiveness(chosenmovetype,enemytypes[0],enemytypes[1]))
                                        setstatuseffects('chosen', chosenmovefinder, enemytypes, chosentruestats, enemytruestats, chosenpokemon, enemypokemon)
                                        recoilcalc('chosen', chosenmove, chosendamage, chosentruestats, chosenpokemon, enemypokemon)
                                        if enemytruestats['HP'] <= 0:
                                            time.sleep(0.5)
                                            print('The wild ' + enemypokemon + ' has fainted.\n')
                                            time.sleep(0.5)
                                            print('You have won the battle!\n')
                                            battlestate = False
                                    else:
                                        time.sleep(0.5)
                                        print('Your ' + chosenpokemon + ' has missed.\n')
                        else:
                            chosenmove = 'None'
                            chosenmovefinder = {'type_id': 0, 'power': 0, 'pp': 0, 'accuracy': 0, 'priority': 0, 'damage_class_id': 0, 'effect_id': 0, 'effect_chance': 0, 'stat_change1': 0, 'stat_change2': 0, 'affects_who': 0, 'stat_stage': 0, 'stat_chance': 0} #Gives data for chosenmove
                            chosenmovetype = 'None' #Gives move type

                        if enemytruestats['HP'] > 0:
                            enemystall = stallfinder('enemy', enemymove, enemytruestats, chosenpokemon, enemypokemon)

                            if enemystall in [True, 'confusion']: # Sends stall message
                                if enemytruestats['nonvolatile'] == 'Frozen':
                                    time.sleep(0.5)
                                    print('The wild ' + enemypokemon + ' is frozen solid!\n')
                                if enemytruestats['nonvolatile'] == 'Asleep':
                                    time.sleep(0.5)
                                    print('The wild ' + enemypokemon + ' is fast asleep.\n')
                                if enemytruestats['nonvolatile'] == 'Paralyzed':
                                    time.sleep(0.5)
                                    print('The wild ' + enemypokemon + " is paralyzed! It can't move!\n")
                                if enemytruestats == 'confusion':
                                    confuseddamage = damagecalc('stallbyconfusion', enemytruestats['Attack'], enemytruestats['Defense'], 40, enemytruestats['atkstage'], enemytruestats['defstage'], weather, enemyburn, 'Normal', 'None', 'None')
                                    enemytruestats['HP'] -= confuseddamage
                                    time.sleep(0.5)
                                    print('The wild ' + enemypokemon + ' hurt itself in its confusion!\n')
                                if enemytruestats['flinched'] == True:
                                    time.sleep(0.5)
                                    print('The wild ' + enemypokemon + " has flinched!\n")
                                enemystall = False

                            elif enemymovefinder['damage_class_id'] == 1:
                                consultspeciallist('enemy', enemytruestats, chosentruestats, chosenpokemon, enemypokemon, enemymove, chosenmove, chosenmove, enemymove) #For moves such as sing, swords dance, etc...

                            else:
                                if enemymove == 'Guillotine':
                                    time.sleep(0.5)
                                    print('The wild ' + enemypokemon + ' used ' + enemymove + '.\n')
                                    if random.randrange(0,100) < enemymovefinder['accuracy']:
                                        chosentruestats['HP'] = 0
                                        time.sleep(0.5)
                                        print('Your ' + chosenpokemon + ' has fainted.\n')
                                        time.sleep(0.5)
                                        print('You have lost the battle...\n')
                                        battlestate = False
                                        gamestate = False
                                        time.sleep(0.5)
                                        print('Game over...\n')
                                    else:
                                        time.sleep(0.5)
                                        print('The wild ' + enemypokemon + ' has missed.\n')
                                else:
                                    time.sleep(0.5)
                                    print('The wild ' + enemypokemon + ' used ' + enemymove + '.\n')
                                    if random.randrange(0,100) < enemymovefinder['accuracy']:
                                        if enemymove == 'Outrage':
                                            outrager('enemy', enemytruestats, chosenpokemon, enemypokemon)
                                        if chosenmove == 'Thrash':
                                            thrasher('enemy', enemytruestats, chosenpokemon, enemypokemon)
                                        chosentruestats['HP'] -= enemydamage
                                        time.sleep(0.5)
                                        effectivenessmessage(calcEffectiveness(enemymovetype,chosentypes[0],chosentypes[1]))
                                        setstatuseffects('enemy', enemymovefinder, chosentypes, enemytruestats, chosentruestats, chosenpokemon, enemypokemon)
                                        recoilcalc('enemy', enemymove, enemydamage, chosentruestats, chosenpokemon, enemypokemon)
                                        if chosentruestats['HP'] <= 0:
                                            time.sleep(0.5)
                                            print('Your ' + chosenpokemon + ' has fainted.\n')
                                            time.sleep(0.5)
                                            print('You have lost the battle...\n')
                                            battlestate = False
                                            gamestate = False
                                            time.sleep(0.5)
                                            print('Game over...\n')
                                    else:
                                        time.sleep(0.5)
                                        print('The wild ' + enemypokemon + ' has missed.\n')
                    else: #THIS IS FOR IF ENEMY HAS HIGHER PRIORITY OR IS FASTER SO IT GOES FIRST
                        enemystall = stallfinder('enemy', enemymove, enemytruestats, chosenpokemon, enemypokemon)

                        if enemystall in [True, 'confusion']: # Sends stall message
                            if enemytruestats['nonvolatile'] == 'Frozen':
                                time.sleep(0.5)
                                print('The wild ' + enemypokemon + ' is frozen solid!\n')
                            if enemytruestats['nonvolatile'] == 'Asleep':
                                time.sleep(0.5)
                                print('The wild ' + enemypokemon + ' is fast asleep.\n')
                            if enemytruestats['nonvolatile'] == 'Paralyzed':
                                time.sleep(0.5)
                                print('The wild ' + enemypokemon + " is paralyzed! It can't move!\n")
                            if enemytruestats == 'confusion':
                                confuseddamage = damagecalc('stallbyconfusion', enemytruestats['Attack'], enemytruestats['Defense'], 40, enemytruestats['atkstage'], enemytruestats['defstage'], weather, enemyburn, 'Normal', 'None', 'None')
                                enemytruestats['HP'] -= confuseddamage
                                time.sleep(0.5)
                                print('The wild ' + enemypokemon + ' hurt itself in its confusion!\n')

                            enemystall = False

                        elif enemymovefinder['damage_class_id'] == 1:
                            consultspeciallist('enemy', enemytruestats, chosentruestats, chosenpokemon, enemypokemon, enemymove, chosenmove, chosenmove, enemymove) #For moves such as sing, swords dance, etc...

                        else:
                            if enemymove == 'Guillotine':
                                time.sleep(0.5)
                                print('The wild ' + enemypokemon + ' used ' + enemymove + '.\n')
                                if random.randrange(0,100) < enemymovefinder['accuracy']:
                                    chosentruestats['HP'] = 0
                                    time.sleep(0.5)
                                    print('Your ' + chosenpokemon + ' has fainted.\n')
                                    time.sleep(0.5)
                                    print('You have lost the battle...\n')
                                    battlestate = False
                                    gamestate = False
                                    time.sleep(0.5)
                                    print('Game over...\n')
                                else:
                                    time.sleep(0.5)
                                    print('The wild ' + enemypokemon + ' has missed.\n')
                            else:
                                time.sleep(0.5)
                                print('The wild ' + enemypokemon + ' used ' + enemymove + '.\n')
                                if random.randrange(0,100) < enemymovefinder['accuracy']:
                                    if enemymove == 'Outrage':
                                        outrager('enemy', enemytruestats, chosenpokemon, enemypokemon)
                                    if chosenmove == 'Thrash':
                                        thrasher('enemy', enemytruestats, chosenpokemon, enemypokemon)
                                    chosentruestats['HP'] -= enemydamage
                                    time.sleep(0.5)
                                    effectivenessmessage(calcEffectiveness(enemymovetype,chosentypes[0],chosentypes[1]))
                                    setstatuseffects('enemy', enemymovefinder, chosentypes, enemytruestats, chosentruestats, chosenpokemon, enemypokemon)
                                    recoilcalc('enemy', enemymove, enemydamage, chosentruestats, chosenpokemon, enemypokemon)
                                    if chosentruestats['HP'] <= 0:
                                        time.sleep(0.5)
                                        print('Your ' + chosenpokemon + ' has fainted.\n')
                                        time.sleep(0.5)
                                        print('You have lost the battle...\n')
                                        battlestate = False
                                        gamestate = False
                                        time.sleep(0.5)
                                        print('Game over...\n')
                                else:
                                    time.sleep(0.5)
                                    print('The wild ' + enemypokemon + ' has missed.\n')

                        if chosentruestats['HP'] > 0:
                            chosenstall = stallfinder('chosen', chosenmove, chosentruestats, chosenpokemon, enemypokemon)

                            if chosenstall in [True, 'confusion']: # Sends stall message
                                if chosentruestats['nonvolatile'] == 'Frozen':
                                    time.sleep(0.5)
                                    print('Your ' + chosenpokemon + ' is frozen solid!\n')
                                if chosentruestats['nonvolatile'] == 'Asleep':
                                    time.sleep(0.5)
                                    print('Your ' + chosenpokemon + ' is fast asleep.\n')
                                if chosentruestats['nonvolatile'] == 'Paralyzed':
                                    time.sleep(0.5)
                                    print('Your ' + chosenpokemon + " is paralyzed! It can't move!\n")
                                if chosenstall == 'confusion':
                                    confuseddamage = damagecalc('stallbyconfusion', chosentruestats['Attack'], chosentruestats['Defense'], 40, chosentruestats['atkstage'], chosentruestats['defstage'], weather, chosenburn, 'Normal', 'None', 'None')
                                    chosentruestats['HP'] -= confuseddamage
                                    time.sleep(0.5)
                                    print('Your ' + chosenpokemon + ' hurt itself in its confusion!\n')
                                if chosentruestats['flinched'] == True:
                                    time.sleep(0.5)
                                    print('Your ' + chosenpokemon + " has flinched!\n")

                                chosenstall = False

                            elif chosenmovefinder['damage_class_id'] == 1:
                                consultspeciallist('chosen', chosentruestats, enemytruestats, chosenpokemon, enemypokemon, chosenmove, enemymove, chosenmove, enemymove) #For moves such as sing, swords dance, etc...

                            else:
                                if chosenmove == 'Guillotine':
                                    time.sleep(0.5)
                                    print('Your ' + chosenpokemon + ' used ' + chosenmove + '.\n')
                                    if random.randrange(0,100) < chosenmovefinder['accuracy']:
                                        enemytruestats['HP'] = 0
                                        time.sleep(0.5)
                                        print('The wild ' + enemypokemon + ' has fainted.\n')
                                        time.sleep(0.5)
                                        print('You have won the battle!\n')
                                        battlestate = False
                                    else:
                                        time.sleep(0.5)
                                        print('Your ' + chosenpokemon + ' has missed.\n')
                                else:
                                    time.sleep(0.5)
                                    print('Your ' + chosenpokemon + ' used ' + chosenmove + '.\n')
                                    if random.randrange(0,100) < chosenmovefinder['accuracy']:
                                        if chosenmove == 'Outrage':
                                            outrager('chosen', chosentruestats, chosenpokemon, enemypokemon)
                                        if chosenmove == 'Thrash':
                                            thrasher('chosen', chosentruestats, chosenpokemon, enemypokemon)
                                        enemytruestats['HP'] -= chosendamage
                                        time.sleep(0.5)
                                        effectivenessmessage(calcEffectiveness(chosenmovetype,enemytypes[0],enemytypes[1]))
                                        setstatuseffects('chosen', chosenmovefinder, enemytypes, chosentruestats, enemytruestats, chosenpokemon, enemypokemon)
                                        recoilcalc('chosen', chosenmove, chosendamage, chosentruestats, chosenpokemon, enemypokemon)
                                        if enemytruestats['HP'] <= 0:
                                            time.sleep(0.5)
                                            print('The wild ' + enemypokemon + ' has fainted.\n')
                                            time.sleep(0.5)
                                            print('You have won the battle!\n')
                                            battlestate = False
                                    else:
                                        time.sleep(0.5)
                                        print('Your ' + chosenpokemon + ' has missed.\n')
                    applyeffects(chosentruestats, enemytruestats, chosenpokemon, enemypokemon)
                    plt.close('all')
                    statcharts(chosentruestats, chosenpokemon, enemytruestats, enemypokemon)
                    hpcharts(chosentruestats, chosenpokemon, enemytruestats, enemypokemon)
                    plt.show()

                resetstatus(chosentruestats)
                time.sleep(1)
                if gamestate == True and turnendfrombattle == True:
                    print('You have gained 500 pokedollars from winning!\n')
<<<<<<< HEAD
                    plt.close('all')
=======
                    bag['Pokedollars'] += 500
                else:
                    turnend = False
>>>>>>> 8a620169a8ae8ec0fec8377a6748916167be727f







gamestart()
