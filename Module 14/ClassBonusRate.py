class Employee:
    def __init__(self, first_name, last_name, salary):
        self.salary = salary
        self.last_name = last_name
        self.first_name = first_name

    def full_name(self):
            return f"{self.first_name} {self.last_name}"

    def emp_bonus(self, bonus_rate):
            return bonus_rate * self.salary

def main():
    first = input("Enter the employee's first name: ")
    last = input("Enter the employee's last name: ")
    salary = float(input("Enter the employee's salary: "))

    emp = Employee(first, last, salary)
    print(f"\nEmployee: {emp.full_name()}, Salary: ${emp.salary:,.2f}")
    rate = float(input("Enter bonus rate (Ex. 0.10 for 10%): "))
    bonus = emp.emp_bonus(rate)
    print(f"\n{emp.full_name()}'s bonus rate is at a rate of {rate:.2%} or: ${bonus:,.2f}")

if __name__ == "__main__":
    main()