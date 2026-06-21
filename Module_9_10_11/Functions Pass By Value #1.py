def calc_ext_price(qty, price):
    total = qty * price
    if total > 10000:
        total = total * 0.90
    return total

total_ext = 0

qty = int(input("Enter quantity (-1 to stop): "))

while qty != -1:
    price = float(input("Enter unit price: "))
    ext = calc_ext_price(qty, price)
    total_ext = total_ext + ext
    print("Qty:", qty, "Price:", price, "Extended Price:", ext)
    qty = int(input("Enter quantity (-1 to stop): "))

print("Total Extended Price:", total_ext)