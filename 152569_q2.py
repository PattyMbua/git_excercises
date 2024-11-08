class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.assignments = {}  # Dictionary to hold assignments and grades

    def add_assignment(self, assignment_name, grade):
        """Add or update an assignment with a grade."""
        self.assignments[assignment_name] = grade

    def display_grades(self):
        """Display all assignments and grades for the student."""
        if self.assignments:
            print(f"Grades for {self.name} (Student ID: {self.student_id}):")
            for assignment, grade in self.assignments.items():
                print(f"  {assignment}: {grade}")
        else:
            print(f"{self.name} has no assignments yet.")

class Instructor:
    def __init__(self, name, course_name):
        self.name = name
        self.course_name = course_name
        self.students = []  # List to store students enrolled in the course

    def add_student(self, student):
        """Add a student to the course."""
        self.students.append(student)
        print(f"Student {student.name} has been added to the course.")

    def assign_grade(self, student, assignment_name, grade):
        """Assign a grade to a student for a particular assignment."""
        student.add_assignment(assignment_name, grade)
        print(f"Grade for {assignment_name} has been assigned to {student.name}.")

    def display_all_grades(self):
        """Display all students and their grades."""
        if self.students:
            print(f"Course: {self.course_name} - Grades for all students:")
            for student in self.students:
                student.display_grades()
        else:
            print("No students enrolled in the course yet.")

# Interactive code to allow an instructor to add students and assign grades
def main():
    # Create an instructor
    instructor = Instructor("Dr. Smith", "Application Programming for the Internet")
    
    # Menu for interaction
    while True:
        print("\nOnline Course Management System")
        print("1. Add a student")
        print("2. Assign a grade to a student")
        print("3. Display all students and their grades")
        print("4. Exit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter student's name: ")
            student_id = input("Enter student ID: ")
            student = Student(name, student_id)
            instructor.add_student(student)

        elif choice == "2":
            if instructor.students:
                print("Select a student to assign a grade:")
                for idx, student in enumerate(instructor.students, start=1):
                    print(f"{idx}. {student.name} (ID: {student.student_id})")
                
                student_choice = int(input("Enter student number: ")) - 1
                if 0 <= student_choice < len(instructor.students):
                    student = instructor.students[student_choice]
                    assignment_name = input("Enter assignment name: ")
                    grade = input("Enter grade: ")
                    instructor.assign_grade(student, assignment_name, grade)
                else:
                    print("Invalid student choice. Try again.")
            else:
                print("No students enrolled yet.")

        elif choice == "3":
            instructor.display_all_grades()

        elif choice == "4":
            print("Exiting the Online Course Management System.")
            break

        else:
            print("Invalid choice. Please select again.")

# Run the interactive session
if __name__ == "__main__":
    main()
