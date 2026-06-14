IN_DISTRICT_RATE = 250.00
OUT_OF_DISTRICT_RATE = 500.00

total_tuition = 0.0
student_count = 0

print(f"{'Last Name':<12} {'Credits':>7} {'Tuition':>10}")
print("-" * 32)

with open("Students.txt", "r") as file:
    lines = file.readlines()

for i in range(0, len(lines), 3):
    last_name = lines[i].strip()
    district_code = lines[i + 1].strip().upper()
    num_credits = int(lines[i + 2].strip())

    if district_code == "I":
        rate = IN_DISTRICT_RATE
    else:
        rate = OUT_OF_DISTRICT_RATE

    tuition = num_credits * rate
    total_tuition += tuition
    student_count += 1

    print(f"{last_name:<12} {num_credits:>7} ${tuition:>9.2f}")

print("-" * 32)
print(f"\nTotal Tuition Owed: ${total_tuition:.2f}")
print(f"Number of Students: {student_count}")