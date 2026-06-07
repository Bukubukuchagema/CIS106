quantity = int(input("Enter number of concert tickets: "))

if quantity >= 25:
    price_per_ticket = 50.00
elif quantity >= 10:
    price_per_ticket = 60.00
elif quantity >= 5:
    price_per_ticket = 70.00
else:
    price_per_ticket = 75.00

total_cost = quantity * price_per_ticket

print(f"\n{'Number of Tickets:':<25} {quantity:>10}")
print(f"{'Price Per Ticket:':<25} {price_per_ticket:>10.2f}")
print(f"{'Total Cost:':<25} {total_cost:>10.2f}")