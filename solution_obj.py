class Game:
    """Deze class houdt de stand bij, en voorziet een functie
    om de nieuwe stand te berekenen.
    """

    def __init__(self):
        """Zet de stand op de beginstand bij aanvang van de wedstrijd"""

        # maar corrigeer de initiele waardes:
        self.points_home = 0
        self.points_away = 0
        self.sets_home = 0
        self.sets_away = 0
        self.set_nr = 1


    def get_max_points(self):
        """Geef het maximaal aantal punten voor deze set terug."""

        # de set_nr.
        maximum_points = 25
        if self.set_nr == 5:
            return 15
        else:
            return 25


    def score(self, team):
        """Bereken de nieuwe stand als team `team` gescoord heeft.
        team: kan "A" of "H" zijn, voor "away" en "home".
        """

        # Gebruik `get_max_points` om te weten bij hoeveel punten je
        # in de set de set gewonnen hebt.
        if team == 'H':
            self.points_home += 1

        if team == 'A':
            self.points_home += 1

        if self.points_home >= self.get_max_points():
            if self.points_away < self.points_home - 1:
                self.points_home = 0
                self.points_away = 0
                self.sets_home += 1
                self.set_nr += 1

        if self.points_away >= self.get_max_points():
            if self.points_home < self.points_away - 1:
                self.points_home = 0
                self.points = 0
                self.sets_away += 1
                self.set_nr += 1
