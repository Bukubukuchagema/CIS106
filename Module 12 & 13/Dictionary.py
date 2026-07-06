def display_grades(grades):
    print(f"{'Name':<15}{'Grade':<10}")
    print(f"{'-' * 14:<15}{'-' * 5:<10}")
    for name, grade in grades.items():
        print(f"{name:<15}{grade:<10}")


def class_average(grades):
    total = 0
    count = 0
    for grade in grades.values():
        total += grade
        count += 1
    return total / count


def main():
    grades = {
        "Smith": 88,
        "Johnson": 92,
        "Williams": 76,
        "Brown": 95,
        "Jones": 81,
        "Garcia": 67,
        "Miller": 99,
        "Davis": 73,
        "Rodriguez": 85,
        "Martinez": 90
    }

    display_grades(grades)

    avg = class_average(grades)
    print(f"\nClass average grade: {avg:.2f}")


if __name__ == "__main__":
    main()