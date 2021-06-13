import matplotlib.pyplot as plt

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
