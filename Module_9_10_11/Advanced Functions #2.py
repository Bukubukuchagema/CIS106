def calc_scores(score1, score2, score3):
    total = score1 + score2 + score3
    average = total / 3
    return total, average

last_name = input("Enter student last name (done to stop): ")

while last_name != "done":
    score1 = float(input("Enter score 1: "))
    score2 = float(input("Enter score 2: "))
    score3 = float(input("Enter score 3: "))
    total, average = calc_scores(score1, score2, score3)
    print("Last Name:", last_name, "Total Points:", total, "Average:", average)
    last_name = input("Enter student last name (done to stop): ")