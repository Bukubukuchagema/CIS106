quantity = int(input("Enter quantity of widgets: "))

if quantity > 10000:
    unit_price = 10.00
elif quantity >= 5000:
    unit_price = 20.00
else:
    unit_price = 30.00

extended_price = quantity * unit_price
tax = extended_price * 0.07
total = extended_price + tax

print(f"\n{'Extended Price:':<20} {extended_price:>10.2f}")
print(f"{'Tax (7%):':<20} {tax:>10.2f}")
print(f"{'Total:':<20} {total:>10.2f}")