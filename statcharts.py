import matplotlib.pyplot as plt
import math

def statcharts(c, p, es, e):
    fig, ax = plt.subplots()
    statlabels = ["Attack", "Defense", "Sp. Atk", "Sp. Def", "Speed"]
    a = c["Attack"] * max(2, 2 + c["atkstage"])/max(2, 2 - c["atkstage"])
    d = c["Defense"] * max(2, 2 + c["defstage"])/max(2, 2 - c["defstage"])
    spa = c["Sp. Atk"] * max(2, 2 + c["spatkstage"])/max(2, 2 + c["spatkstage"])
    spd = c["Sp. Def"] + max(2, 2 + c["spdefstage"])/max(2, 2 + c["spdefstage"])
    statlist = [a, d, spa, spd, c["Speed"]]
    plt.barh(statlabels, statlist)
    plt.title("Pokemon Stats")
    ax.invert_yaxis()

def hpcharts(c, p, es, e):
    hplabels = ["Enemy " + e, "Player " + p]
    hplist = [es["HP"], c["HP"]]
    plt.figure(figsize=(12,6))
    plt.barh(hplabels, hplist)
    plt.title("Health of Pokemon")
    if c["MAXHP"] > es["MAXHP"]:
        plt.xlim([0, int(c["MAXHP"])])
    else:
        plt.xlim([0, int(es["MAXHP"])])
