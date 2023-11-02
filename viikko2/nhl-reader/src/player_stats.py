class PlayerStats:
    def __init__(self, reader):
        self.players=reader.get_players()
        
    def top_scorers_by_nationality(self, nat):
        return sorted(
                filter(lambda i: i.nationality==nat, self.players), 
                key=lambda h: -h.goals-h.assists)

