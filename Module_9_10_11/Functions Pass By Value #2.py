# Problem 2 - Batting Average
# Functions module

def calc_batting_avg(hits, at_bats):
    avg = hits / at_bats
    return avg

count = 0

last_name = input("Enter player last name (Done to stop): ")

while last_name != "done":
    hits = int(input("Enter hits: "))
    at_bats = int(input("Enter at bats: "))
    avg = calc_batting_avg(hits, at_bats)
    count = count + 1
    print("Last Name:", last_name, "Batting Average:", round(avg, 3))
    last_name = input("Enter player last name (done to stop): ")

print("Number of players entered:", count)