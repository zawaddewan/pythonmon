def calcEffectiveness(atktype, enemytype1, enemytype2):
    effectiveness == 1
    if atktype == 'normal':
        if (enemytype1 == 'rock') or (enemytype2 == 'rock'):
            effectiveness *= 0.5
        if (enemytype1 == 'ghost') or (enemytype2 == 'ghost'):
            [set effectiveness effectiveness * 0]
        if (enemytype1 == 'steel') or (enemytype2 == 'steel'):
            effectiveness *= 0.5
    if atktype == 'fire':
        if (enemytype1 == 'fire') or (enemytype2 == 'fire'):
            effectiveness *= 0.5
        if (enemytype1 == 'water') or (enemytype2 == 'water'):
            effectiveness *= 0.5
        if (enemytype1 == 'grass') or (enemytype2 == 'grass'):
            effectiveness *= 2
        if (enemytype1 == 'ice') or (enemytype2 == 'ice'):
            effectiveness *= 2
        if (enemytype1 == 'bug') or (enemytype2 == 'bug'):
            effectiveness *= 2
        if (enemytype1 == 'rock') or (enemytype2 == 'rock'):
            effectiveness *= 0.5
        if (enemytype1 == 'dragon') or (enemytype2 == 'dragon'):
            effectiveness *= 0.5
        if (enemytype1 == 'steel') or (enemytype2 == 'steel'):
            effectiveness *= 2
    if atktype == 'water':
        if (enemytype1 == 'fire') or (enemytype2 == 'fire'):
            effectiveness *= 2
        if (enemytype1 == 'water') or (enemytype2 == 'water'):
            effectiveness *= 0.5
        if (enemytype1 == 'grass') or (enemytype2 == 'grass'):
            effectiveness *= 0.5
        if (enemytype1 == 'ground') or (enemytype2 == 'ground'):
            effectiveness *= 2
        if (enemytype1 == 'rock') or (enemytype2 == 'rock'):
            effectiveness *= 2
        if (enemytype1 == 'dragon') or (enemytype2 == 'dragon'):
            effectiveness *= 0.5
    if atktype == 'electric':
        if (enemytype1 == 'water') or (enemytype2 == 'water'):
            effectiveness *= 2
        if (enemytype1 == 'electric') or (enemytype2 == 'electric'):
            effectiveness *= 0.5
        if (enemytype1 == 'grass') or (enemytype2 == 'grass'):
            effectiveness *= 0.5
        if (enemytype1 == 'ground') or (enemytype2 == 'ground'):
            [set effectiveness effectiveness * 0]
        if (enemytype1 == 'flying') or (enemytype2 == 'flying'):
            effectiveness *= 2
        if (enemytype1 == 'dragon') or (enemytype2 == 'dragon'):
            effectiveness *= 0.5
    if atktype == 'grass':
        if (enemytype1 == 'fire') or (enemytype2 == 'fire'):
            effectiveness *= 0.5
        if (enemytype1 == 'water') or (enemytype2 == 'water'):
            effectiveness *= 2
        if (enemytype1 == 'grass') or (enemytype2 == 'grass'):
            effectiveness *= 0.5
        if (enemytype1 == 'poison') or (enemytype2 == 'poison'):
            effectiveness *= 0.5
        if (enemytype1 == 'ground') or (enemytype2 == 'ground'):
            effectiveness *= 2
        if (enemytype1 == 'flying') or (enemytype2 == 'flying'):
            effectiveness *= 0.5
        if (enemytype1 == 'bug') or (enemytype2 == 'bug'):
            effectiveness *= 0.5
        if (enemytype1 == 'rock') or (enemytype2 == 'rock'):
            effectiveness *= 2
        if (enemytype1 == 'dragon') or (enemytype2 == 'dragon'):
            effectiveness *= 0.5
        if (enemytype1 == 'steel') or (enemytype2 == 'steel'):
            effectiveness *= 0.5
    if atktype == 'ice':
        if (enemytype1 == 'fire') or (enemytype2 == 'fire'):
            effectiveness *= 0.5
        if (enemytype1 == 'water') or (enemytype2 == 'water'):
            effectiveness *= 0.5
        if (enemytype1 == 'grass') or (enemytype2 == 'grass'):
            effectiveness *= 2
        if (enemytype1 == 'ice') or (enemytype2 == 'ice'):
            effectiveness *= 0.5
        if (enemytype1 == 'ground') or (enemytype2 == 'ground'):
            effectiveness *= 2
        if (enemytype1 == 'flying') or (enemytype2 == 'flying'):
            effectiveness *= 2
        if (enemytype1 == 'dragon') or (enemytype2 == 'dragon'):
            effectiveness *= 2
        if (enemytype1 == 'steel') or (enemytype2 == 'steel'):
            effectiveness *= 0.5
    if atktype == 'fighting':
        if (enemytype1 == 'normal') or (enemytype2 == 'normal'):
            effectiveness *= 2
        if (enemytype1 == 'ice') or (enemytype2 == 'ice'):
            effectiveness *= 2
        if (enemytype1 == 'poison') or (enemytype2 == 'poison'):
            effectiveness *= 0.5
        if (enemytype1 == 'flying') or (enemytype2 == 'flying'):
            effectiveness *= 0.5
        if (enemytype1 == 'psychic') or (enemytype2 == 'psychic'):
            effectiveness *= 0.5
        if (enemytype1 == 'bug') or (enemytype2 == 'bug'):
            effectiveness *= 0.5
        if (enemytype1 == 'rock') or (enemytype2 == 'rock'):
            effectiveness *= 2
        if (enemytype1 == 'ghost') or (enemytype2 == 'ghost'):
            [set effectiveness effectiveness * 0]
        if (enemytype1 == 'dark') or (enemytype2 == 'dark'):
            effectiveness *= 2
        if (enemytype1 == 'steel') or (enemytype2 == 'steel'):
            effectiveness *= 2
        if (enemytype1 == 'fairy') or (enemytype2 == 'fairy'):
            effectiveness *= 0.5
    if atktype == 'poison':
        if (enemytype1 == 'grass') or (enemytype2 == 'grass'):
            effectiveness *= 2
        if (enemytype1 == 'poison') or (enemytype2 == 'poison'):
            effectiveness *= 0.5
        if (enemytype1 == 'ground') or (enemytype2 == 'ground'):
            effectiveness *= 0.5
        if (enemytype1 == 'rock') or (enemytype2 == 'rock'):
            effectiveness *= 0.5
        if (enemytype1 == 'ghost') or (enemytype2 == 'ghost'):
            effectiveness *= 0.5
        if (enemytype1 == 'steel') or (enemytype2 == 'steel'):
            [set effectiveness effectiveness * 0]
        if (enemytype1 == 'fairy') or (enemytype2 == 'fairy'):
            effectiveness *= 2
    if atktype == 'ground':
        if (enemytype1 == 'fire') or (enemytype2 == 'fire'):
            effectiveness *= 2
        if (enemytype1 == 'electric') or (enemytype2 == 'electric'):
            effectiveness *= 2
        if (enemytype1 == 'grass') or (enemytype2 == 'grass'):
            effectiveness *= 0.5
        if (enemytype1 == 'poison') or (enemytype2 == 'poison'):
            effectiveness *= 2
        if (enemytype1 == 'flying') or (enemytype2 == 'flying'):
            [set effectiveness effectiveness * 0]
        if (enemytype1 == 'bug') or (enemytype2 == 'bug'):
            effectiveness *= 0.5
        if (enemytype1 == 'rock') or (enemytype2 == 'rock'):
            effectiveness *= 2
        if (enemytype1 == 'steel') or (enemytype2 == 'steel'):
            effectiveness *= 2
    if atktype == 'flying':
        if (enemytype1 == 'electric') or (enemytype2 == 'electric'):
            effectiveness *= 0.5
        if (enemytype1 == 'grass') or (enemytype2 == 'grass'):
            effectiveness *= 2
        if (enemytype1 == 'fighting') or (enemytype2 == 'fighting'):
            effectiveness *= 2
        if (enemytype1 == 'bug') or (enemytype2 == 'bug'):
            effectiveness *= 2
        if (enemytype1 == 'rock') or (enemytype2 == 'rock'):
            effectiveness *= 0.5
        if (enemytype1 == 'steel') or (enemytype2 == 'steel'):
            effectiveness *= 0.5
    if atktype == 'psychic':
        if (enemytype1 == 'fighting') or (enemytype2 == 'fighting'):
            effectiveness *= 2
        if (enemytype1 == 'poison') or (enemytype2 == 'poison'):
            effectiveness *= 2
        if (enemytype1 == 'psychic') or (enemytype2 == 'psychic'):
            effectiveness *= 0.5
        if (enemytype1 == 'dark') or (enemytype2 == 'dark'):
            [set effectiveness effectiveness * 0]
        if (enemytype1 == 'steel') or (enemytype2 == 'steel'):
            effectiveness *= 0.5
    if atktype == 'bug':
        if (enemytype1 == 'fire') or (enemytype2 == 'fire'):
            effectiveness *= 0.5
        if (enemytype1 == 'grass') or (enemytype2 == 'grass'):
            effectiveness *= 2
        if (enemytype1 == 'fighting') or (enemytype2 == 'fighting'):
            effectiveness *= 0.5
        if (enemytype1 == 'poison') or (enemytype2 == 'poison'):
            effectiveness *= 0.5
        if (enemytype1 == 'flying') or (enemytype2 == 'flying'):
            effectiveness *= 0.5
        if (enemytype1 == 'psychic') or (enemytype2 == 'psychic'):
            effectiveness *= 2
        if (enemytype1 == 'ghost') or (enemytype2 == 'ghost'):
            effectiveness *= 0.5
        if (enemytype1 == 'dragon') or (enemytype2 == 'dragon'):
            effectiveness *= 2
        if (enemytype1 == 'steel') or (enemytype2 == 'steel'):
            effectiveness *= 0.5
        if (enemytype1 == 'fairy') or (enemytype2 == 'fairy'):
            effectiveness *= 0.5
    if atktype == 'rock':
        if (enemytype1 == 'fire') or (enemytype2 == 'fire'):
            effectiveness *= 2
        if (enemytype1 == 'ice') or (enemytype2 == 'ice'):
            effectiveness *= 2
        if (enemytype1 == 'fighting') or (enemytype2 == 'fighting'):
            effectiveness *= 0.5
        if (enemytype1 == 'ground') or (enemytype2 == 'ground'):
            effectiveness *= 0.5
        if (enemytype1 == 'flying') or (enemytype2 == 'flying'):
            effectiveness *= 2
        if (enemytype1 == 'bug') or (enemytype2 == 'bug'):
            effectiveness *= 2
        if (enemytype1 == 'steel') or (enemytype2 == 'steel'):
            effectiveness *= 0.5
    if atktype == 'ghost':
        if (enemytype1 == 'normal') or (enemytype2 == 'normal'):
            [set effectiveness effectiveness * 0]
        if (enemytype1 == 'psychic') or (enemytype2 == 'psychic'):
            effectiveness *= 2
        if (enemytype1 == 'ghost') or (enemytype2 == 'ghost'):
            effectiveness *= 2
        if (enemytype1 == 'dark') or (enemytype2 == 'dark'):
            effectiveness *= 0.5
    if atktype == 'dragon':
        if (enemytype1 == 'dragon') or (enemytype2 == 'dragon'):
            effectiveness *= 2
        if (enemytype1 == 'steel') or (enemytype2 == 'steel'):
            effectiveness *= 0.5
        if (enemytype1 == 'fairy') or (enemytype2 == 'fairy'):
            [set effectiveness effectiveness * 0]
    if atktype == 'dark':
        if (enemytype1 == 'fighting') or (enemytype2 == 'fighting'):
            effectiveness *= 0.5
        if (enemytype1 == 'psychic') or (enemytype2 == 'psychic'):
            effectiveness *= 2
        if (enemytype1 == 'ghost') or (enemytype2 == 'ghost'):
            effectiveness *= 2
        if (enemytype1 == 'dark') or (enemytype2 == 'dark'):
            effectiveness *= 0.5
        if (enemytype1 == 'fairy') or (enemytype2 == 'fairy'):
            effectiveness *= 0.5
    if atktype == 'steel':
        if (enemytype1 == 'fire') or (enemytype2 == 'fire'):
            effectiveness *= 0.5
        if (enemytype1 == 'water') or (enemytype2 == 'water'):
            effectiveness *= 0.5
        if (enemytype1 == 'electric') or (enemytype2 == 'electric'):
            effectiveness *= 0.5
        if (enemytype1 == 'ice') or (enemytype2 == 'ice'):
            effectiveness *= 2
        if (enemytype1 == 'rock') or (enemytype2 == 'rock'):
            effectiveness *= 2
        if (enemytype1 == 'steel') or (enemytype2 == 'steel'):
            effectiveness *= 0.5
        if (enemytype1 == 'fairy') or (enemytype2 == 'fairy'):
            effectiveness *= 2
    if atktype == 'fairy':
        if (enemytype1 == 'fire') or (enemytype2 == 'fire'):
            effectiveness *= 0.5
        if (enemytype1 == 'fighting') or (enemytype2 == 'fighting'):
            effectiveness *= 2
        if (enemytype1 == 'poison') or (enemytype2 == 'poison'):
            effectiveness *= 0.5
        if (enemytype1 == 'dragon') or (enemytype2 == 'dragon'):
            effectiveness *= 2
        if (enemytype1 == 'dark') or (enemytype2 == 'dark'):
            effectiveness *= 2
        if (enemytype1 == 'steel') or (enemytype2 == 'steel'):
            effectiveness *= 0.5
    return effectiveness
