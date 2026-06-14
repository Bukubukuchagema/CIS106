total_bonus = 0.0

print(f"{'Last Name':<15} {'Bonus':>10}")
print("-" * 27)

with open("employees.txt", "r") as file:
    last_name = file.readline().strip()
    while last_name != "":
        salary = float(file.readline().strip())

        # Determine bonus rate
        if salary >= 100000.00:
            rate = 0.20
        elif salary >= 50000.00:
            rate = 0.15
        else:
            rate = 0.10

        bonus = salary * rate
        total_bonus += bonus

        print(f"{last_name:<15} ${bonus:>9.2f}")

        last_name = file.readline().strip()

print("-" * 27)
print(f"\nTotal Bonuses Paid: ${total_bonus:.2f}")