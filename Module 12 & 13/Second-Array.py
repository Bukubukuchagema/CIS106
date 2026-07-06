def display_names(names):
    for name in names:
        print(name)


def display_names_reverse(names):
    index = len(names) - 1
    while index >= 0:
        print(names[index])
        index -= 1


def display_names_scores(names, scores):
    for i in range(len(names)):
        print(f"{names[i]}: {scores[i]}")


def display_names_scores_reverse(names, scores):
    index = len(names) - 1
    while index >= 0:
        print(f"{names[index]}: {scores[index]}")
        index -= 1


def main():
    last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones",
                  "Garcia", "Miller", "Davis", "Rodriguez", "Martinez"]
    exam_scores = [88, 92, 76, 95, 81, 67, 99, 73, 85, 90]

    print("Names in original order:")
    display_names(last_names)

    print("\nNames in reverse order:")
    display_names_reverse(last_names)

    print("\nNames and scores in original order:")
    display_names_scores(last_names, exam_scores)

    print("\nNames and scores in reverse order:")
    display_names_scores_reverse(last_names, exam_scores)


if __name__ == "__main__":
    main()