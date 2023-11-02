import requests
from player import Player

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2022-23/players"
    response = requests.get(url).json()

    players = []
    for player_dict in response:
        player = Player(player_dict)
        players.append(player)



    print("Players from FIN\n\n")
    
    for p in sorted(players, key=lambda h: -h.goals-h.assists):
        if p.nationality=="FIN":
            print(p)

if __name__ == "__main__":
    main()
