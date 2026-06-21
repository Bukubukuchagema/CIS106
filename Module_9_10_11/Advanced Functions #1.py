def calc_discount(qty, price, discount_rate):
    total = qty * price
    discount_amount = total * (discount_rate / 100)
    discounted_price = total - discount_amount
    return discount_amount, discounted_price

qty = int(input("Enter quantity (-1 to stop): "))

while qty != -1:
    price = float(input("Enter price: "))
    discount_rate = float(input("Enter discount rate (ex: 10 for 10%): "))
    discount_amount, discounted_price = calc_discount(qty, price, discount_rate)
    print("Quantity:", qty, "Price:", price)
    print("Discount Amount:", discount_amount, "Discounted Price:", discounted_price)
    qty = int(input("Enter quantity (-1 to stop): "))