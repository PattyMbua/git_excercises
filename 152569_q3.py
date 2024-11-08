class Employee:
    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary

    def display_details(self):
        """Display the details of the employee."""
        print(f"Employee ID: {self.employee_id}")
        print(f"Name: {self.name}")
        print(f"Salary: ${self.salary}")

    def update_salary(self, new_salary):
        """Update the salary of the employee."""
        self.salary = new_salary
        print(f"Salary for {self.name} has been updated to ${self.salary}.")

class Department:
    def __init__(self, department_name):
        self.department_name = department_name
        self.employees = []  # List to hold employees in the department

    def add_employee(self, employee):
        """Add an employee to the department."""
        self.employees.append(employee)
        print(f"{employee.name} has been added to the {self.department_name} department.")

    def calculate_total_salary(self):
        """Calculate and display the total salary expenditure for the department."""
        total_salary = sum(employee.salary for employee in self.employees)
        print(f"Total salary expenditure for the {self.department_name} department: ${total_salary}")

    def display_all_employees(self):
        """Display all employees in the department."""
        if self.employees:
            print(f"Employees in the {self.department_name} department:")
            for employee in self.employees:
                employee.display_details()
        else:
            print(f"No employees in the {self.department_name} department yet.")

# Interactive code to manage employees and department
def main():
    # Create a department
    department_name = input("Enter department name: ")
    department = Department(department_name)

    # Menu for interaction
    while True:
        print("\nEmployee and Department Management System")
        print("1. Add an employee")
        print("2. Update employee salary")
        print("3. Display all employees")
        print("4. Display total salary expenditure")
        print("5. Exit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter employee name: ")
            employee_id = input("Enter employee ID: ")
            salary = float(input("Enter employee salary: "))
            employee = Employee(name, employee_id, salary)
            department.add_employee(employee)

        elif choice == "2":
            if department.employees:
                print("Select an employee to update salary:")
                for idx, employee in enumerate(department.employees, start=1):
                    print(f"{idx}. {employee.name} (ID: {employee.employee_id})")
                
                employee_choice = int(input("Enter employee number: ")) - 1
                if 0 <= employee_choice < len(department.employees):
                    new_salary = float(input("Enter new salary: "))
                    department.employees[employee_choice].update_salary(new_salary)
                else:
                    print("Invalid employee choice. Try again.")
            else:
                print("No employees in the department yet.")

        elif choice == "3":
            department.display_all_employees()

        elif choice == "4":
            department.calculate_total_salary()

        elif choice == "5":
            print("Exiting the Employee and Department Management System.")
            return  # This will return to the caller (back to the main function)

        else:
            print("Invalid choice. Please select again.")

# Run the interactive session
if __name__ == "__main__":
    while True:  # Wrap the entire flow inside another loop
        main()
        continue_program = input("\nDo you want to continue managing employees? (y/n): ").lower()
        if continue_program != "y":
            print("Goodbye!")
            break
