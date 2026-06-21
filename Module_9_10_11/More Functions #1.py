def calc_forecast(month, sales):
    if month == "Jan" or month == "Feb" or month == "Mar" or month == "January" or month == "February" or month == "March":
        percent = 0.10
    elif month == "Apr" or month == "May" or month == "Jun" or month == "April" or month == "May" or month == "June":
        percent = 0.15
    elif month == "Jul" or month == "Aug" or month == "Sep" or month == "July" or month == "August" or month == "September":
        percent = 0.20
    elif month == "Oct" or month == "Nov" or month == "Dec" or month == "October" or month == "November" or month == "December":
        percent = 0.25
    else:
        percent = 0
    next_sales = sales * (1 + percent)
    return next_sales

answer = input("Do you want to enter data? (Yes or No): ")

while answer == "Yes":
    last_name = input("Enter last name: ")
    month = input("Enter month (Jan, Feb, Mar, etc): ")
    sales = float(input("Enter sales: "))
    next_month = calc_forecast(month, sales)
    print("Last Name:", last_name, "Next Month Sales:", next_month)
    answer = input("Do you want to enter data? (Yes or No): ")
