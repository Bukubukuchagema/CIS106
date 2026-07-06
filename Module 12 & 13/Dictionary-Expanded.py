def student_average(grade_list):
    total = 0
    for grade in grade_list:
        total += grade
    return total / len(grade_list)


def build_average_list(grades):
    averages = []
    for name, grade_list in grades.items():
        averages.append([name, student_average(grade_list)])
    return averages


def display_averages(averages):
    print(f"{'Name':<15}{'Average':<10}")
    print(f"{'-' * 14:<15}{'-' * 7:<10}")
    for name, avg in averages:
        print(f"{name:<15}{avg:<10.2f}")


def class_averages_per_grade(grades):
    total1 = 0
    total2 = 0
    total3 = 0
    count = 0
    for grade_list in grades.values():
        total1 += grade_list[0]
        total2 += grade_list[1]
        total3 += grade_list[2]
        count += 1
    return total1 / count, total2 / count, total3 / count


def main():
    grades = {
        "Smith": [88, 90, 85],
        "Johnson": [92, 89, 94],
        "Williams": [76, 80, 72],
        "Brown": [95, 91, 97],
        "Jones": [81, 78, 83],
        "Garcia": [67, 70, 65],
        "Miller": [99, 96, 98],
        "Davis": [73, 75, 71],
        "Rodriguez": [85, 88, 82],
        "Martinez": [90, 87, 92]
    }

    averages = build_average_list(grades)
    display_averages(averages)

    avg1, avg2, avg3 = class_averages_per_grade(grades)
    print("\nClass averages by grade:")
    print(f"  Grade 1 average: {avg1:.2f}")
    print(f"  Grade 2 average: {avg2:.2f}")
    print(f"  Grade 3 average: {avg3:.2f}")


if __name__ == "__main__":
    main()