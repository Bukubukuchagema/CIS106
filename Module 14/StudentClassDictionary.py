DISTRICT_RATES = {
    "I": 250.00,
    "O": 500.00,
    "X": 800.00,
    "G": 250.00
}
class Student:
    def __init__(self, first_name, last_name, district_code, enrolled_credits):
        self.first_name = first_name
        self.last_name = last_name
        self.district_code = district_code
        self.enrolled_credits = enrolled_credits

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def tuition(self):
        rate = DISTRICT_RATES.get(self.district_code)

        if rate is None:
            raise ValueError(f"Unknown district code: {self.district_code}")

        tuition = self.enrolled_credits * rate
        return tuition

def get_student_input(label):
    first = input(f"Enter {label} student's first name: ")
    last = input(f"Enter {label} student's last name: ")
    district_code = input(
        f"Confirm {label} student's district code (I, O, X, or G): "
    )
    credits = float(input(f"Enter {label} student enrolled credit hours: "))
    return Student(first, last, district_code, credits)

def display_student(student):
    tuition = student.tuition()
    print(f"\nStudent: {student.full_name()}")
    print(f"District Code: {student.district_code}")
    print(f"Enrolled Credits: {student.enrolled_credits}")
    print(f"Tuition Owed: ${tuition:,.2f}")

def main():
    # Instantiate at least one student of each district code: I, O, X, G
    print("   - In District Student -")
    in_district_student = get_student_input("(I)")
    display_student(in_district_student)

    print("\n   - Out of District Student -")
    out_of_district_student = get_student_input("(O)")
    display_student(out_of_district_student)

    print("\n   - International Student -")
    international_student = get_student_input("(X)")
    display_student(international_student)

    print("\n   - Reciprocity Student -")
    reciprocity_student = get_student_input("(G)")
    display_student(reciprocity_student)

if __name__ == "__main__":
    main()