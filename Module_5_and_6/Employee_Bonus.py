last_name = input("Enter employee last name: ")
salary = float(input("Enter salary: "))
job_level = int(input("Enter job level (1-20): "))

if job_level >= 10:
    bonus_rate = 0.25
elif job_level >= 5:
    bonus_rate = 0.20
else:
    bonus_rate = 0.10

bonus = salary * bonus_rate

print(f"\n{'Last Name:':<20} {last_name:>10}")
print(f"{'Bonus:':<20} {bonus:>10.2f}")