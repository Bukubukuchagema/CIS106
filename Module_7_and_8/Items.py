total_extended = 0.0

print(f"{'Item':<12} {'Qty':>5} {'Price':>8} {'Extended':>10}")
print("-" * 38)

with open("Items.txt", "r") as file:
    lines = file.readlines()

order_count = 0
for i in range(0, len(lines), 3):
    item = lines[i].strip()
    quantity = int(lines[i + 1].strip())
    price = float(lines[i + 2].strip())

    extended_price = quantity * price
    total_extended += extended_price
    order_count += 1

    print(f"{item:<12} {quantity:>5} ${price:>7.2f} ${extended_price:>9.2f}")

print("-" * 38)
average_order = total_extended / order_count if order_count > 0 else 0

print(f"\nTotal Extended Price: ${total_extended:.2f}")
print(f"Number of Orders:     {order_count}")
print(f"Average Order Value:  ${average_order:.2f}")
