start = int(input("Enter start value: "))
stop = int(input("Enter stop value: "))
increment = int(input("Enter increment value: "))

print(f"\nNumbers from {start} to {stop} by {increment}:")
current = start
while current <= stop:
    print(current)
    current += increment