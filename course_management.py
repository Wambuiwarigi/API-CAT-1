class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.assignments = {}  
    
    def add_assignment_and_grade(self, assignment_name, grade):
        """Add an assignment and grade to the student's record"""
        if 0 <= grade <= 100:
            self.assignments[assignment_name] = grade
            print(f"Grade {grade} added for {assignment_name} - {self.name}")
        else:
            print(f"Invalid grade {grade}. Grade must be between 0 and 100.")
    
    def display_grades(self):
        """Display all grades for the student"""
        if not self.assignments:
            print(f"{self.name} has no assignments yet.")
        else:
            print(f"\nGrades for {self.name} (ID: {self.student_id}):")
            print("-" * 50)
            for assignment, grade in self.assignments.items():
                print(f"{assignment}: {grade}%")
           
            average = sum(self.assignments.values()) / len(self.assignments)
            print(f"Average Grade: {average:.2f}%")
    
    def __str__(self):
        return f"Student: {self.name} (ID: {self.student_id})"


class Instructor:
    def __init__(self, name, course_name):
        self.name = name
        self.course_name = course_name
        self.students = []  
    
    def add_student(self, student):
        """Add a student to the course"""
        if student not in self.students:
            self.students.append(student)
            print(f"Student {student.name} has been added to {self.course_name}")
        else:
            print(f"Student {student.name} is already enrolled in {self.course_name}")
    
    def assign_grade(self, student_id, assignment_name, grade):
        """Assign a grade to a student"""
        student = self.find_student_by_id(student_id)
        if student:
            student.add_assignment_and_grade(assignment_name, grade)
        else:
            print(f"Student with ID {student_id} not found in {self.course_name}")
    
    def display_all_students_and_grades(self):
        """Display all students and their grades"""
        if not self.students:
            print(f"No students enrolled in {self.course_name}")
        else:
            print(f"\nCourse: {self.course_name}")
            print(f"Instructor: {self.name}")
            print("=" * 60)
            for student in self.students:
                student.display_grades()
                print()
    
    def find_student_by_id(self, student_id):
        """Find a student by their ID"""
        for student in self.students:
            if student.student_id == student_id:
                return student
        return None
    
    def list_students(self):
        """List all students in the course"""
        if not self.students:
            print(f"No students enrolled in {self.course_name}")
        else:
            print(f"\nStudents enrolled in {self.course_name}:")
            print("-" * 40)
            for i, student in enumerate(self.students, 1):
                print(f"{i}. {student}")
    
    def __str__(self):
        return f"Instructor: {self.name} - Course: {self.course_name}"


def display_menu():
    """Display the main menu"""
    print("\n" + "="*60)
    print("ONLINE COURSE MANAGEMENT SYSTEM")
    print("="*60)
    print("1. Display course information")
    print("2. List all students")
    print("3. Add a new student")
    print("4. Assign a grade to a student")
    print("5. Display all students and their grades")
    print("6. Display individual student grades")
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


def get_valid_grade():
    """Get a valid grade from user"""
    while True:
        try:
            grade = float(input("Enter grade (0-100): "))
            if 0 <= grade <= 100:
                return grade
            else:
                print("Grade must be between 0 and 100")
        except ValueError:
            print("Please enter a valid number")


def main():
    """Main interactive function"""
    
    instructor = Instructor("Dr. Sarah Johnson", "Introduction to Computer Science")
    
   
    sample_students = [
        Student("Alice Brown", "S001"),
        Student("Bob Wilson", "S002"),
        Student("Carol Davis", "S003"),
        Student("David Miller", "S004")
    ]
    
    
    for student in sample_students:
        instructor.add_student(student)
    
   
    instructor.assign_grade("S001", "Assignment 1", 85)
    instructor.assign_grade("S001", "Assignment 2", 92)
    instructor.assign_grade("S002", "Assignment 1", 78)
    instructor.assign_grade("S003", "Assignment 1", 95)
    instructor.assign_grade("S003", "Assignment 2", 88)
    instructor.assign_grade("S004", "Assignment 1", 82)
    
    print("Welcome to the Online Course Management System!")
    
    while True:
        display_menu()
        choice = get_valid_choice("Enter your choice (1-7): ", 7)
        
        if choice == 1:
            
            print(f"\nCourse Information:")
            print(f"Instructor: {instructor.name}")
            print(f"Course: {instructor.course_name}")
            print(f"Number of Students: {len(instructor.students)}")
            
        elif choice == 2:
            
            instructor.list_students()
            
        elif choice == 3:
            
            name = input("Enter student name: ")
            student_id = input("Enter student ID: ")
            
            
            if instructor.find_student_by_id(student_id):
                print(f"Student with ID {student_id} already exists!")
            else:
                new_student = Student(name, student_id)
                instructor.add_student(new_student)
                
        elif choice == 4:
            
            instructor.list_students()
            if instructor.students:
                student_choice = get_valid_choice("Enter student number: ", len(instructor.students))
                student = instructor.students[student_choice - 1]
                
                assignment_name = input("Enter assignment name: ")
                grade = get_valid_grade()
                
                instructor.assign_grade(student.student_id, assignment_name, grade)
                
        elif choice == 5:
            
            instructor.display_all_students_and_grades()
            
        elif choice == 6:
           
            instructor.list_students()
            if instructor.students:
                student_choice = get_valid_choice("Enter student number: ", len(instructor.students))
                student = instructor.students[student_choice - 1]
                student.display_grades()
                
        elif choice == 7:
            print("Thank you for using the Online Course Management System!")
            break


if __name__ == "__main__":
    main() 