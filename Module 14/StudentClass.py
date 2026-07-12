IN_DISTRICT_RATE = 250.00
OUT_OF_DISTRICT_RATE = 500.00

class Student:
    def __init__(self, first_name, last_name, district_code, enrolled_credits):
        self.first_name = first_name
        self.last_name = last_name
        self.district_code = district_code
        self.enrolled_credits = enrolled_credits

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def tuition(self):
        if self.district_code == "I":
            tuition = self.enrolled_credits * IN_DISTRICT_RATE
        else:
            tuition = self.enrolled_credits * OUT_OF_DISTRICT_RATE

        return tuition

def main():
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    district_code = input("Enter your district code (I = In District, O = Out Of District): ")
    enrolled_credits = float(input("Enter your enrolled credits: "))

    student = Student(first_name, last_name, district_code, enrolled_credits)
    tuition = student.tuition()

    print(f"\nStudent: {student.full_name()}")
    print(f"District Code: {student.district_code}")
    print(f"Enrolled Credits: {student.enrolled_credits}")
    print(f"Tuition Owed: ${tuition:,.2f}")

if __name__ == "__main__":
    main()