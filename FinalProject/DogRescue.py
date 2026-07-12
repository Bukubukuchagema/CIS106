try:
    from prettytable import PrettyTable
    HAS_PRETTYTABLE = True
except ImportError:
    HAS_PRETTYTABLE = False

dogCount = 0

def main():
    dogTable = []
    menu(dogTable)

def menu(dogTable):
    while True:
        print("\n - Dog Rescue - ")
        print("-----------------\n")
        print("\t1. Add a Dog")
        print("\t2. View All Dogs")
        print("\t3. Find a Dog")
        print("\t4. Exit\n")

        choice = input("Select an option (1-4): ")

        if choice == "1":
            addDog(dogTable)
        elif choice == "2":
            viewDogs(dogTable)
        elif choice == "3":
            findDog(dogTable)
        elif choice == "4":
            print("\nThank you, goodbye!")
            break
        else:
            print("\nInvalid choice, please select 1-4.")

def addDog(dogTable):
    global dogCount

    print()
    name = input("Dog Name: ")
    breed = input("Dog Breed: ")
    age = input("Age: ")
    weight = input("Weight: ")

    dogTable.append([name, breed, age, weight])
    dogCount += 1

def viewDogs(dogTable):
    print()
    if not dogTable:
        print("No dogs have been added yet.")
        return

    print("Rescued Dogs: ")
    print("-" * 60)

    if HAS_PRETTYTABLE:
        table = PrettyTable()
        table.field_names = ["Dog", "Breed", "Age", "Weight"]
        for dog in dogTable:
            table.add_row(dog)
        print(table)
    else:
        print(f"{'Dog':<15}{'Breed':<25}{'Age':<8}{'Weight':<8}")
        print("-" * 60)
        for dog in dogTable:
            name, breed, age, weight = dog
            print(f"{name:<15}{breed:<25}{age:<8}{weight:<8}")

    print(f"\n*There is a total of {dogCount} dogs*")

def findDog(dogTable):
    print()
    searchName = input("Enter the name of the dog you want to find: ")

    for dog in dogTable:
        if dog[0].lower() == searchName.lower():
            print(f"Found  {dog[0]} - (Check 'View All Dogs' For More Information)")
            return

    print(f"Sorry, unable to find  {searchName}")

if __name__ == "__main__":
    main()