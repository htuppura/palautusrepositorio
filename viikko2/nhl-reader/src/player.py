class Player:
    def __init__(self, dict):
        self.name = dict['name']
        self.goals = dict['goals']
        self.assists = dict['assists']
        self.team = dict['team']
        self.nationality = dict['nationality']
    
    def __str__(self):
        n = self.name
        t = self.team
        g = self.goals
        a = self.assists
        p = self.goals + self.assists
        return f"{n} team {t} - {g} + {a} = {p}"
