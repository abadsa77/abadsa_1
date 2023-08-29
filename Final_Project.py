class Course:
    course_id = 1

    def __init__(self, course_name, course_level):
        self.course_id = Course.course_id
        Course.course_id += 1
        self.course_name = course_name
        self.course_level = course_level
    def course_info(self):
        #print("-" * 30)
        print(f"course name      :{self.course_name.capitalize()}       /"
              f"course id    :{self.course_id} /"
              f"course level : {self.course_level.capitalize()} ")
        print("-"*75)

class Student:
    student_id = 1

    def __init__(self, student_name, studnet_level):
        self.student_id = Student.student_id
        Student.student_id += 1
        self.student_name = student_name
        self.studnet_level = studnet_level
        self.student_courses = []

    # Define a method to add a new course to the student's courses
    def add_course(self, course):
        # Check if the course is an instance of the Course class
        if isinstance(course, Course):
            # Check if the student's level is the same as the course's level
            if self.studnet_level == course.course_level:
                # Check if the course is already in the student's courses
                if course not in self.student_courses:
                    # Add the course to the student's courses
                    self.student_courses.append(course)
                    print(f"Course {course.course_name.capitalize()} added successfully.")
                else:
                    print(f"Course {course.course_name.capitalize()} already exists.")
            else:
                print(f"Course {course.course_name} is not suitable for your level.")
        else:
            print(f"Invalid course.")

    def display_student_details(self):
        print(f"student name    : {self.student_name.capitalize()}\n"
              f"student id      : {self.student_id}\n"
              f"student level   : {self.studnet_level.capitalize()}\n"
              f"student courses : {', '.join(course.course_name for course in self.student_courses)}")
        print("_"*30)
        for course in self.student_courses:
            course.course_info()
        print("*" * 30)




course1 = Course("Python Basics   ", "A")
course2 = Course("Python Intermed.", "B")
course3 = Course("Python Advanced ", "C")
courses_list = [course1,course2,course3]


# Create an empty list to store the students
students = []

# Define a function to add a new student to the list
def add_student():
    # Ask the user to enter the student name
    while True:
        name = input("Enter student name          : ")

        if name.isalpha():
            break  # ينهي الحلقة إذا كان الإدخال صحيحًا
        else:
            print("Please enter a valid name consisting of alphabetical characters only.")
    # Ask the user to select the student level
    level = input("Select student level (A-B-C): ")
    # Validate the level input
    while level not in ["A", "B", "C","a","b","c"]:
        print("Invalid level. Please select A, B or C.")
        level = input("Select student level (A-B-C): ")
    # Create a new student object with the name and level
    student = Student(name.capitalize(), level.upper())
    # Add the student object to the list
    students.append(student)
    print(f"Student {name.capitalize()} saved successfully.")
    print("*" * 30)

# Define a function to remove a student from the list
def remove_student():
    # Ask the user to enter the student id
    id = int(input("Enter student id            : "))
    # Loop through the list to find the student with the matching id
    for student in students:
        if student.student_id == id:
            # Remove the student from the list
            students.remove(student)
            print(f"Student {student.student_name} deleted successfully.")
            print("*" * 30)
            # Return from the function to avoid further looping
            return
    # If no matching student is found, print a message
    print(f"Student with id {id} does not exist.")
    print("^" * 30)


# Define a function to edit a student's name and level
def edit_student():
    # Ask the user to enter the student id
    id = int(input("Enter student id          : "))
    # Loop through the list to find the student with the matching id
    for student in students:
        if student.student_id == id:
            # Ask the user to enter the new name
            name = input("Enter new name           : ")
            # Ask the user to select the new level
            level = input("Select new level (A-B-C): ")
            # Validate the level input
            while level not in ["A", "B", "C","a","b","c"]:
                print("Invalid level. Please select A, B or C.")
                print("^" * 30)
                level = input("Select new level (A-B-C): ")
            # Update the student's name and level
            student.student_name = name
            student.studnet_level = level
            print(f"Student {name.capitalize()} updated successfully.")
            print("*" * 30)
            # Return from the function to avoid further looping
            return
    # If no matching student is found, print a message
    print(f"Student with id {id} does not exist.")
    print("^" * 30)



# Define a function to display all students in the list
def display_students():
    # Check if the list is empty or not
    if students:
        # Loop through the list and display each student's details
        for student in students:
            student.display_student_details()
    else:
        print("No students found.")
        print("^" * 30)


def display_courses():
    print("*" * 30)
    # Loop through the list and display each courses details
    for course in courses_list:
        course.course_info()






# Define a function to create a new course object and return it
def create_course():
    # Ask the user to enter the course name
    name = input("Enter course name           : ")
    # Ask the user to select the course level
    level = input("Select course level (A-B-C): ")
    # Validate the level input
    while level not in ["A", "B", "C","a","b","c"]:
        print("Invalid level. Please select A, B or C.")
        print("^" * 30)
        level = input("Select course level (A-B-C): ")
    # Create a new course object with the name and level
    course = Course(name.capitalize(), level.upper())
    print(f"Course {name.capitalize()}, level : {level.upper()} created successfully.")
    print("*" * 30)
    # Return the course object
    return courses_list.append(course)

# Define a function to add a course to a student's courses
def add_course_to_student(courses_list):
    # Ask the user to enter the student id
    id = int(input("Enter student id          : "))
    # Loop through the list to find the student with the matching id
    for student in students:
        if student.student_id == id:
            # Ask the user to enter the course id
            cid = input("Enter course id      : ")
            if cid.isdigit():
                cid = int(cid)
                for course in courses_list:
                    if course.course_id == cid:
                        student.add_course(course)
                        return
                print(f"Course with id {cid} does not exist.")
                print("^" * 30)
            else:
                print("Invalid course id.")
                print("^" * 30)
            return
            # If no matching student is found, print a message
    print(f"Student with id {id} does not exist.")
    print("^" * 30)

def main_menu():
    print("-" * 40)
    print("| Welcome to Student Management System |")
    print("| Selct Choice Please:                 |")
    print("| 1. Add New Student                   |")
    print("| 2. Remove Student                    |")
    print("| 3. Edit Student                      |")
    print("| 4. Display All Students              |")
    print("| 5. Create New Course                 |")
    print("| 6. Add Course to Students            |")
    print("| 7. Display All Courses               |")
    print("| 0. Exit                              |")
    print("-"*40)

def main():
    # students = []
   #courses = [course1, course2, course3]

    while True:
        main_menu()
        choice = input("Enter your choice         : ")

        if choice == "1":
            add_student()
        elif choice == "2":
            remove_student()
        elif choice == "3":
            edit_student()
        elif choice == "4":
            display_students()
        elif choice == "5":
            create_course()
        elif choice == "6":
            add_course_to_student(courses_list)
        elif choice == "7":
            display_courses()
        elif choice == "0":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
