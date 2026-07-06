def load_data(filename):
    names = []
    scores = []
    with open(filename, "r") as file:
        for line in file:
            line = line.strip()
            if line:
                name, score = line.split(",")
                names.append(name)
                scores.append(int(score))
    return names, scores


def display_names_scores(names, scores):
    for i in range(len(names)):
        print(f"{names[i]}: {scores[i]}")


def display_highest(names, scores):
    high_var = 0
    high_index = 0
    for i in range(len(scores)):
        if scores[i] > high_var:
            high_var = scores[i]
            high_index = i
    print(f"Highest score - {names[high_index]}: {high_var}")


def display_lowest(names, scores):
    low_var = 999
    low_index = 0
    for i in range(len(scores)):
        if scores[i] < low_var:
            low_var = scores[i]
            low_index = i
    print(f"Lowest score - {names[low_index]}: {low_var}")


def main():
    names, scores = load_data("LastnameScores.txt")

    print("Student scores:")
    display_names_scores(names, scores)

    print()
    display_highest(names, scores)
    display_lowest(names, scores)


if __name__ == "__main__":
    main()