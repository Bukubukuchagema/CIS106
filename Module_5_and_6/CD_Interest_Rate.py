principle = float(input("Enter principle amount: "))
years = int(input("Enter years to maturity: "))

if principle > 100000:
    interest_rate = 0.06
elif principle >= 50000 and years == 10:
    interest_rate = 0.05
elif principle >= 50000 and years == 5:
    interest_rate = 0.04
else:
    interest_rate = 0.02

first_year_interest = principle * interest_rate

print(f"\n{'Principle:':<25} {principle:>10.2f}")
print(f"{'Interest Rate:':<25} {interest_rate * 100:>9.0f}%")
print(f"{'First Year Interest:':<25} {first_year_interest:>10.2f}")