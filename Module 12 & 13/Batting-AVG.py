def load_players(filename):
    players = {}
    with open(filename, "r") as file:
        for line in file:
            line = line.strip()
            if line:
                name, avg = line.split(",")
                players[name] = float(avg)
    return players


def display_players(players):
    print(f"{'Player':<15}{'Batting Avg':<12}")
    print(f"{'-' * 14:<15}{'-' * 11:<12}")
    for name, avg in players.items():
        print(f"{name:<15}{avg:<12}")


def main():
    players = load_players("players.txt")
    display_players(players)


if __name__ == "__main__":
    main()