def display_names(names):
    for name in names:
        print(name)


def display_names_reverse(names):
    # Walk backwards through the array manually - no reversed()/[::-1]/.reverse()
    index = len(names) - 1
    while index >= 0:
        print(names[index])
        index -= 1


def main():
    last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones",
                  "Garcia", "Miller", "Davis", "Rodriguez", "Martinez"]

    print("Names in original order:")
    display_names(last_names)

    print("\nNames in reverse order:")
    display_names_reverse(last_names)


if __name__ == "__main__":
    main()