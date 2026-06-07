quantity = int(input("Enter quantity: "))

if quantity >= 1000:
    unit_price = 3.00
else:
    unit_price = 5.00

extended_price = quantity * unit_price
tax = extended_price * 0.07
total = extended_price + tax

print(f"\n{'Quantity:':<20} {quantity:>10}")
print(f"{'Unit Price:':<20} {unit_price:>10.2f}")
print(f"{'Extended Price:':<20} {extended_price:>10.2f}")
print(f"{'Tax (7%):':<20} {tax:>10.2f}")
print(f"{'Total:':<20} {total:>10.2f}")