import matplotlib.pyplot as plt
<<<<<<< HEAD

def statcharts(c, p, es, e):
    fig, ax = plt.subplots()
    statlabels = ["Attack", "Defense", "Sp. Atk", "Sp. Def", "Speed"]
    statlist = [c["Attack"], c["Defense"], c["Sp. Atk"], c["Sp. Def"], c["Speed"]]
    plt.barh(statlabels, statlist)
    ax.invert_yaxis()

def hpcharts(c, p, es, e):
    hplabels = ["Enemy " + e, "Player " + p]
    hplist = [es["HP"], c["HP"]]
    plt.figure(figsize=(12,6))
    plt.barh(hplabels, hplist)
    if c["MAXHP"] > es["MAXHP"]:
        plt.xlim([0, int(c["MAXHP"])])
    else:
        plt.xlim([0, int(es["MAXHP"])])
=======
from csv_helper import *
from effectiveness_helper import *
from battleandstatcalculations import *
from tinygamemechanics import *
from pprint import pprint
import random
import time

def pokecharts(c, p, e):
    plt.rcdefaults()
    fig, ax = plt.subplots()
    statlabels = ['Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed']
    statlist = [c['Attack'], c['Defense'], c['Sp. Atk'], c['Sp. Def'], c['Speed']]
    hplabels = ["Enemy " + e, "Player " + p, ]
    hplist = [c["HP"], c["HP"]]
    statchart = plt.figure(1)
    plt.barh(statlabels, statlist)
    plt.title("Pokemon Stats")
    hpchart = plt.figure(2, figsize=(12,6))
    plt.barh(hplabels, hplist)
    plt.title("Health of Pokemon")
    ax.invert_yaxis()
>>>>>>> 8a620169a8ae8ec0fec8377a6748916167be727f
