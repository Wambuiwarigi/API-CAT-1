class Employee:
    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary
    
    def display_details(self):
        """Display employee details"""
        print(f"\nEmployee Details:")
        print(f"Name: {self.name}")
        print(f"Employee ID: {self.employee_id}")
        print(f"Salary: ${self.salary:,.2f}")
    
    def update_salary(self, new_salary):
        """Update employee salary"""
        if new_salary >= 0:
            old_salary = self.salary
            self.salary = new_salary
            print(f"Salary updated for {self.name}: ${old_salary:,.2f} → ${new_salary:,.2f}")
        else:
            print("Invalid salary amount. Salary must be non-negative.")
    
    def __str__(self):
        return f"Employee: {self.name} (ID: {self.employee_id}) - ${self.salary:,.2f}"


class Department:
    def __init__(self, department_name):
        self.department_name = department_name
        self.employees = [] 
    
    def add_employee(self, employee):
        """Add an employee to the department"""
        if employee not in self.employees:
            self.employees.append(employee)
            print(f"Employee {employee.name} has been added to {self.department_name}")
        else:
            print(f"Employee {employee.name} is already in {self.department_name}")
    
    def calculate_total_salary_expenditure(self):
        """Calculate and return the total salary expenditure for the department"""
        total = sum(employee.salary for employee in self.employees)
        return total
    
    def display_total_salary_expenditure(self):
        """Display the total salary expenditure for the department"""
        total = self.calculate_total_salary_expenditure()
        print(f"\nTotal Salary Expenditure for {self.department_name}:")
        print(f"${total:,.2f}")
        print(f"Number of Employees: {len(self.employees)}")
        if self.employees:
            average_salary = total / len(self.employees)
            print(f"Average Salary: ${average_salary:,.2f}")
    
    def display_all_employees(self):
        """Display all employees in the department"""
        if not self.employees:
            print(f"No employees in {self.department_name}")
        else:
            print(f"\nEmployees in {self.department_name}:")
            print("-" * 60)
            for i, employee in enumerate(self.employees, 1):
                print(f"{i}. {employee}")
    
    def find_employee_by_id(self, employee_id):
        """Find an employee by their ID"""
        for employee in self.employees:
            if employee.employee_id == employee_id:
                return employee
        return None
    
    def __str__(self):
        return f"Department: {self.department_name} ({len(self.employees)} employees)"


def display_menu():
    """Display the main menu"""
    print("\n" + "="*60)
    print("EMPLOYEE AND DEPARTMENT MANAGEMENT SYSTEM")
    print("="*60)
    print("1. Display department information")
    print("2. Display all employees")
    print("3. Add a new employee")
    print("4. Update employee salary")
    print("5. Display total salary expenditure")
    print("6. Display individual employee details")
    print("7. Exit")
    print("="*60)


def get_valid_choice(prompt, max_value):
    """Get valid user choice"""
    while True:
        try:
            choice = int(input(prompt))
            if 1 <= choice <= max_value:
                return choice
            else:
                print(f"Please enter a number between 1 and {max_value}")
        except ValueError:
            print("Please enter a valid number")


def get_valid_salary():
    """Get a valid salary from user"""
    while True:
        try:
            salary = float(input("Enter salary amount: $"))
            if salary >= 0:
                return salary
            else:
                print("Salary must be non-negative")
        except ValueError:
            print("Please enter a valid number")


def main():
    """Main interactive function"""
    
    department = Department("Information Technology")
    
    
    sample_employees = [
        Employee("John Smith", "E001", 65000.00),
        Employee("Sarah Johnson", "E002", 72000.00),
        Employee("Michael Brown", "E003", 58000.00),
        Employee("Emily Davis", "E004", 68000.00),
        Employee("David Wilson", "E005", 75000.00)
    ]
    
    
    for employee in sample_employees:
        department.add_employee(employee)
    
    print("Welcome to the Employee and Department Management System!")
    
    while True:
        display_menu()
        choice = get_valid_choice("Enter your choice (1-7): ", 7)
        
        if choice == 1:
            
            print(f"\nDepartment Information:")
            print(f"Department: {department.department_name}")
            print(f"Number of Employees: {len(department.employees)}")
            if department.employees:
                total_salary = department.calculate_total_salary_expenditure()
                print(f"Total Salary Budget: ${total_salary:,.2f}")
                average_salary = total_salary / len(department.employees)
                print(f"Average Salary: ${average_salary:,.2f}")
            
        elif choice == 2:
            
            department.display_all_employees()
            
        elif choice == 3:
           
            name = input("Enter employee name: ")
            employee_id = input("Enter employee ID: ")
            
            
            if department.find_employee_by_id(employee_id):
                print(f"Employee with ID {employee_id} already exists!")
            else:
                salary = get_valid_salary()
                new_employee = Employee(name, employee_id, salary)
                department.add_employee(new_employee)
                
        elif choice == 4:
           
            department.display_all_employees()
            if department.employees:
                employee_choice = get_valid_choice("Enter employee number: ", len(department.employees))
                employee = department.employees[employee_choice - 1]
                
                print(f"Current salary for {employee.name}: ${employee.salary:,.2f}")
                new_salary = get_valid_salary()
                employee.update_salary(new_salary)
                
        elif choice == 5:
           
            department.display_total_salary_expenditure()
            
        elif choice == 6:
            
            department.display_all_employees()
            if department.employees:
                employee_choice = get_valid_choice("Enter employee number: ", len(department.employees))
                employee = department.employees[employee_choice - 1]
                employee.display_details()
                
        elif choice == 7:
            print("Thank you for using the Employee and Department Management System!")
            break


if __name__ == "__main__":
    main() 