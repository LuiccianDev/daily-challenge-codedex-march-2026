def upset_probability(matchups):

    results = []

    for match in matchups:
        seedA = match[1]
        seedB = match[3]

        higher_seed = seedB
        lower_seed = seedA

        probability = lower_seed / (higher_seed + lower_seed)

        results.append(round(probability, 2))

    return results