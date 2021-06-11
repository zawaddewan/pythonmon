def calcEffectiveness(atktype, enemytype1, enemytype2):
    effectiveness = 1
    if atktype == 'Normal':
        if (enemytype1 == 'Rock') or (enemytype2 == 'Rock'):
            effectiveness *= 0.5
        if (enemytype1 == 'Ghost') or (enemytype2 == 'Ghost'):
            effectiveness *= 0
        if (enemytype1 == 'Steel') or (enemytype2 == 'Steel'):
            effectiveness *= 0.5
    if atktype == 'Fire':
        if (enemytype1 == 'Fire') or (enemytype2 == 'Fire'):
            effectiveness *= 0.5
        if (enemytype1 == 'Water') or (enemytype2 == 'Water'):
            effectiveness *= 0.5
        if (enemytype1 == 'Grass') or (enemytype2 == 'Grass'):
            effectiveness *= 2
        if (enemytype1 == 'Ice') or (enemytype2 == 'Ice'):
            effectiveness *= 2
        if (enemytype1 == 'Bug') or (enemytype2 == 'Bug'):
            effectiveness *= 2
        if (enemytype1 == 'Rock') or (enemytype2 == 'Rock'):
            effectiveness *= 0.5
        if (enemytype1 == 'Dragon') or (enemytype2 == 'Dragon'):
            effectiveness *= 0.5
        if (enemytype1 == 'Steel') or (enemytype2 == 'Steel'):
            effectiveness *= 2
    if atktype == 'Water':
        if (enemytype1 == 'Fire') or (enemytype2 == 'Fire'):
            effectiveness *= 2
        if (enemytype1 == 'Water') or (enemytype2 == 'Water'):
            effectiveness *= 0.5
        if (enemytype1 == 'Grass') or (enemytype2 == 'Grass'):
            effectiveness *= 0.5
        if (enemytype1 == 'Ground') or (enemytype2 == 'Ground'):
            effectiveness *= 2
        if (enemytype1 == 'Rock') or (enemytype2 == 'Rock'):
            effectiveness *= 2
        if (enemytype1 == 'Dragon') or (enemytype2 == 'Dragon'):
            effectiveness *= 0.5
    if atktype == 'Electric':
        if (enemytype1 == 'Water') or (enemytype2 == 'Water'):
            effectiveness *= 2
        if (enemytype1 == 'Electric') or (enemytype2 == 'Electric'):
            effectiveness *= 0.5
        if (enemytype1 == 'Grass') or (enemytype2 == 'Grass'):
            effectiveness *= 0.5
        if (enemytype1 == 'Ground') or (enemytype2 == 'Ground'):
            effectiveness *= 0
        if (enemytype1 == 'Flying') or (enemytype2 == 'Flying'):
            effectiveness *= 2
        if (enemytype1 == 'Dragon') or (enemytype2 == 'Dragon'):
            effectiveness *= 0.5
    if atktype == 'Grass':
        if (enemytype1 == 'Fire') or (enemytype2 == 'Fire'):
            effectiveness *= 0.5
        if (enemytype1 == 'Water') or (enemytype2 == 'Water'):
            effectiveness *= 2
        if (enemytype1 == 'Grass') or (enemytype2 == 'Grass'):
            effectiveness *= 0.5
        if (enemytype1 == 'Poison') or (enemytype2 == 'Poison'):
            effectiveness *= 0.5
        if (enemytype1 == 'Ground') or (enemytype2 == 'Ground'):
            effectiveness *= 2
        if (enemytype1 == 'Flying') or (enemytype2 == 'Flying'):
            effectiveness *= 0.5
        if (enemytype1 == 'Bug') or (enemytype2 == 'Bug'):
            effectiveness *= 0.5
        if (enemytype1 == 'Rock') or (enemytype2 == 'Rock'):
            effectiveness *= 2
        if (enemytype1 == 'Dragon') or (enemytype2 == 'Dragon'):
            effectiveness *= 0.5
        if (enemytype1 == 'Steel') or (enemytype2 == 'Steel'):
            effectiveness *= 0.5
    if atktype == 'Ice':
        if (enemytype1 == 'Fire') or (enemytype2 == 'Fire'):
            effectiveness *= 0.5
        if (enemytype1 == 'Water') or (enemytype2 == 'Water'):
            effectiveness *= 0.5
        if (enemytype1 == 'Grass') or (enemytype2 == 'Grass'):
            effectiveness *= 2
        if (enemytype1 == 'Ice') or (enemytype2 == 'Ice'):
            effectiveness *= 0.5
        if (enemytype1 == 'Ground') or (enemytype2 == 'Ground'):
            effectiveness *= 2
        if (enemytype1 == 'Flying') or (enemytype2 == 'Flying'):
            effectiveness *= 2
        if (enemytype1 == 'Dragon') or (enemytype2 == 'Dragon'):
            effectiveness *= 2
        if (enemytype1 == 'Steel') or (enemytype2 == 'Steel'):
            effectiveness *= 0.5
    if atktype == 'Fighting':
        if (enemytype1 == 'Normal') or (enemytype2 == 'Normal'):
            effectiveness *= 2
        if (enemytype1 == 'Ice') or (enemytype2 == 'Ice'):
            effectiveness *= 2
        if (enemytype1 == 'Poison') or (enemytype2 == 'Poison'):
            effectiveness *= 0.5
        if (enemytype1 == 'Flying') or (enemytype2 == 'Flying'):
            effectiveness *= 0.5
        if (enemytype1 == 'Psychic') or (enemytype2 == 'Psychic'):
            effectiveness *= 0.5
        if (enemytype1 == 'Bug') or (enemytype2 == 'Bug'):
            effectiveness *= 0.5
        if (enemytype1 == 'Rock') or (enemytype2 == 'Rock'):
            effectiveness *= 2
        if (enemytype1 == 'Ghost') or (enemytype2 == 'Ghost'):
            effectiveness *= 0
        if (enemytype1 == 'Dark') or (enemytype2 == 'Dark'):
            effectiveness *= 2
        if (enemytype1 == 'Steel') or (enemytype2 == 'Steel'):
            effectiveness *= 2
        if (enemytype1 == 'Fairy') or (enemytype2 == 'Fairy'):
            effectiveness *= 0.5
    if atktype == 'Poison':
        if (enemytype1 == 'Grass') or (enemytype2 == 'Grass'):
            effectiveness *= 2
        if (enemytype1 == 'Poison') or (enemytype2 == 'Poison'):
            effectiveness *= 0.5
        if (enemytype1 == 'Ground') or (enemytype2 == 'Ground'):
            effectiveness *= 0.5
        if (enemytype1 == 'Rock') or (enemytype2 == 'Rock'):
            effectiveness *= 0.5
        if (enemytype1 == 'Ghost') or (enemytype2 == 'Ghost'):
            effectiveness *= 0.5
        if (enemytype1 == 'Steel') or (enemytype2 == 'Steel'):
            effectiveness *= 0
        if (enemytype1 == 'Fairy') or (enemytype2 == 'Fairy'):
            effectiveness *= 2
    if atktype == 'Ground':
        if (enemytype1 == 'Fire') or (enemytype2 == 'Fire'):
            effectiveness *= 2
        if (enemytype1 == 'Electric') or (enemytype2 == 'Electric'):
            effectiveness *= 2
        if (enemytype1 == 'Grass') or (enemytype2 == 'Grass'):
            effectiveness *= 0.5
        if (enemytype1 == 'Poison') or (enemytype2 == 'Poison'):
            effectiveness *= 2
        if (enemytype1 == 'Flying') or (enemytype2 == 'Flying'):
            effectiveness *= 0
        if (enemytype1 == 'Bug') or (enemytype2 == 'Bug'):
            effectiveness *= 0.5
        if (enemytype1 == 'Rock') or (enemytype2 == 'Rock'):
            effectiveness *= 2
        if (enemytype1 == 'Steel') or (enemytype2 == 'Steel'):
            effectiveness *= 2
    if atktype == 'Flying':
        if (enemytype1 == 'Electric') or (enemytype2 == 'Electric'):
            effectiveness *= 0.5
        if (enemytype1 == 'Grass') or (enemytype2 == 'Grass'):
            effectiveness *= 2
        if (enemytype1 == 'Fighting') or (enemytype2 == 'Fighting'):
            effectiveness *= 2
        if (enemytype1 == 'Bug') or (enemytype2 == 'Bug'):
            effectiveness *= 2
        if (enemytype1 == 'Rock') or (enemytype2 == 'Rock'):
            effectiveness *= 0.5
        if (enemytype1 == 'Steel') or (enemytype2 == 'Steel'):
            effectiveness *= 0.5
    if atktype == 'Psychic':
        if (enemytype1 == 'Fighting') or (enemytype2 == 'Fighting'):
            effectiveness *= 2
        if (enemytype1 == 'Poison') or (enemytype2 == 'Poison'):
            effectiveness *= 2
        if (enemytype1 == 'Psychic') or (enemytype2 == 'Psychic'):
            effectiveness *= 0.5
        if (enemytype1 == 'Dark') or (enemytype2 == 'Dark'):
            effectiveness *= 0
        if (enemytype1 == 'Steel') or (enemytype2 == 'Steel'):
            effectiveness *= 0.5
    if atktype == 'Bug':
        if (enemytype1 == 'Fire') or (enemytype2 == 'Fire'):
            effectiveness *= 0.5
        if (enemytype1 == 'Grass') or (enemytype2 == 'Grass'):
            effectiveness *= 2
        if (enemytype1 == 'Fighting') or (enemytype2 == 'Fighting'):
            effectiveness *= 0.5
        if (enemytype1 == 'Poison') or (enemytype2 == 'Poison'):
            effectiveness *= 0.5
        if (enemytype1 == 'Flying') or (enemytype2 == 'Flying'):
            effectiveness *= 0.5
        if (enemytype1 == 'Psychic') or (enemytype2 == 'Psychic'):
            effectiveness *= 2
        if (enemytype1 == 'Ghost') or (enemytype2 == 'Ghost'):
            effectiveness *= 0.5
        if (enemytype1 == 'Dragon') or (enemytype2 == 'Dragon'):
            effectiveness *= 2
        if (enemytype1 == 'Steel') or (enemytype2 == 'Steel'):
            effectiveness *= 0.5
        if (enemytype1 == 'Fairy') or (enemytype2 == 'Fairy'):
            effectiveness *= 0.5
    if atktype == 'Rock':
        if (enemytype1 == 'Fire') or (enemytype2 == 'Fire'):
            effectiveness *= 2
        if (enemytype1 == 'Ice') or (enemytype2 == 'Ice'):
            effectiveness *= 2
        if (enemytype1 == 'Fighting') or (enemytype2 == 'Fighting'):
            effectiveness *= 0.5
        if (enemytype1 == 'Ground') or (enemytype2 == 'Ground'):
            effectiveness *= 0.5
        if (enemytype1 == 'Flying') or (enemytype2 == 'Flying'):
            effectiveness *= 2
        if (enemytype1 == 'Bug') or (enemytype2 == 'Bug'):
            effectiveness *= 2
        if (enemytype1 == 'Steel') or (enemytype2 == 'Steel'):
            effectiveness *= 0.5
    if atktype == 'Ghost':
        if (enemytype1 == 'Normal') or (enemytype2 == 'Normal'):
            effectiveness *= 0
        if (enemytype1 == 'Psychic') or (enemytype2 == 'Psychic'):
            effectiveness *= 2
        if (enemytype1 == 'Ghost') or (enemytype2 == 'Ghost'):
            effectiveness *= 2
        if (enemytype1 == 'Dark') or (enemytype2 == 'Dark'):
            effectiveness *= 0.5
    if atktype == 'Dragon':
        if (enemytype1 == 'Dragon') or (enemytype2 == 'Dragon'):
            effectiveness *= 2
        if (enemytype1 == 'Steel') or (enemytype2 == 'Steel'):
            effectiveness *= 0.5
        if (enemytype1 == 'Fairy') or (enemytype2 == 'Fairy'):
            effectiveness *= 0
    if atktype == 'Dark':
        if (enemytype1 == 'Fighting') or (enemytype2 == 'Fighting'):
            effectiveness *= 0.5
        if (enemytype1 == 'Psychic') or (enemytype2 == 'Psychic'):
            effectiveness *= 2
        if (enemytype1 == 'Ghost') or (enemytype2 == 'Ghost'):
            effectiveness *= 2
        if (enemytype1 == 'Dark') or (enemytype2 == 'Dark'):
            effectiveness *= 0.5
        if (enemytype1 == 'Fairy') or (enemytype2 == 'Fairy'):
            effectiveness *= 0.5
    if atktype == 'Steel':
        if (enemytype1 == 'Fire') or (enemytype2 == 'Fire'):
            effectiveness *= 0.5
        if (enemytype1 == 'Water') or (enemytype2 == 'Water'):
            effectiveness *= 0.5
        if (enemytype1 == 'Electric') or (enemytype2 == 'Electric'):
            effectiveness *= 0.5
        if (enemytype1 == 'Ice') or (enemytype2 == 'Ice'):
            effectiveness *= 2
        if (enemytype1 == 'Rock') or (enemytype2 == 'Rock'):
            effectiveness *= 2
        if (enemytype1 == 'Steel') or (enemytype2 == 'Steel'):
            effectiveness *= 0.5
        if (enemytype1 == 'Fairy') or (enemytype2 == 'Fairy'):
            effectiveness *= 2
    if atktype == 'Fairy':
        if (enemytype1 == 'Fire') or (enemytype2 == 'Fire'):
            effectiveness *= 0.5
        if (enemytype1 == 'Fighting') or (enemytype2 == 'Fighting'):
            effectiveness *= 2
        if (enemytype1 == 'Poison') or (enemytype2 == 'Poison'):
            effectiveness *= 0.5
        if (enemytype1 == 'Dragon') or (enemytype2 == 'Dragon'):
            effectiveness *= 2
        if (enemytype1 == 'Dark') or (enemytype2 == 'Dark'):
            effectiveness *= 2
        if (enemytype1 == 'Steel') or (enemytype2 == 'Steel'):
            effectiveness *= 0.5
    return effectiveness
