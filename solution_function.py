def update_score(oldscore, team):
    """Deze functie berekent de nieuwe stand, vertrekkend van
    de oude stand "oldscore" als "team" net gescoord heeft.
    De nieuwe stand wordt als resultaat teruggegeven.

    oldscore: een tuple van 4 nummers, set thuis, set away, punten thuis,
    punten away
    team: de ploeg die net scoorde, "H" voor thuis, "A" voor away
    """
    sets_home = oldscore[0]
    sets_away = oldscore[1]
    points_home = oldscore[2]
    points_away = oldscore[3]

    # schrijf hier de nodige code om de testen te doen slagen
    set_score = 25

    if team == 'H':
        points_home = points_home +1

    if team == 'A':
        points_away = points_away +1

    if sets_home + sets_away == 4:
        set_score = 15

    if points_home >= set_score and points_home >= points_away + 2:
        points_home = 0
        points_away = 0
        sets_home = sets_home +1

    if points_away >= set_score and points_away >= points_home + 2:
        points_home = 0
        points_away = 0
        sets_away = sets_away + 1


    return sets_home, sets_away, points_home, points_away
