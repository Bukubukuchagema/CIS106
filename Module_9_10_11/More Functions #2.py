def calc_out_the_door(msrp, make, model, ev):
    if ev == "Y":
        discount = msrp * 0.30
    elif make == "Honda" and model == "Accord":
        discount = msrp * 0.10
    elif make == "Toyota" and model == "Rav4":
        discount = msrp * 0.15
    else:
        discount = msrp * 0.05
    new_msrp = msrp - discount
    tax = new_msrp * 0.07
    total = new_msrp + tax
    return total

total_msrp = 0
total_sales = 0

answer = input("Do you want to enter a vehicle? (Yes or No): ")

while answer == "Yes":
    make = input("Enter make: ")
    model = input("Enter model: ")
    ev = input("Electric vehicle? (Y or N): ")
    msrp = float(input("Enter MSRP: "))
    total = calc_out_the_door(msrp, make, model, ev)
    total_msrp = total_msrp + msrp
    total_sales = total_sales + total
    print("Out the door price:", total)
    answer = input("Do you want to enter a vehicle? (Yes or No): ")

print("Total MSRP:", total_msrp)
print("Total Sales Price:", total_sales)