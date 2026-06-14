student_count = 0
response = input("Do you want to enter student data? (Yes to continue): ")

while response.lower() == "yes":
    last_name = input("Enter student last name: ")
    score1 = float(input("Enter first exam score: "))
    score2 = float(input("Enter second exam score: "))

    average = (score1 + score2) / 2
    student_count += 1

    print(f"  Last Name: {last_name}")
    print(f"  Average Score: {average:.2f}\n")

    response = input("Do you want to enter another student? (Yes to continue): ")

print("-" * 35)
print(f"Total number of students entered: {student_count}")