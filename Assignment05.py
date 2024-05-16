# ------------------------------------------------------------------------------------------ #
# Title: Assignment05
# Desc: This assignment demonstrates using dictionaries, files, and exception handling
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Script
#   Vugee Preap,05/15/2024, Created Script
# ------------------------------------------------------------------------------------------ #
import json

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
# Define the Data Constants
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables and constants
student_first_name: str = ''  # Holds the first name of a student entered by the user.
student_last_name: str = ''  # Holds the last name of a student entered by the user.
course_name: str = ''  # Holds the name of a course entered by the user.
student_data: list = []  # one row of student data
students: list = []  # a table of student data
csv_data: str = ''  # Holds combined string data separated by a comma.
file = None  # Holds a reference to an opened file.
menu_choice: str  # Hold the choice made by the user.

# When the program starts, read the file data into a list of lists (table)
# Extract the data from the file
file = open(FILE_NAME, "r")
for row in file.readlines():
    # Transform the data from the file
    student_data = row.split(',')
    student_data = [student_data[0], student_data[1], student_data[2].strip()]
    # Load it into our collection (list of lists)
    students.append(student_data)
file.close()

# Present and Process the data
while (True):

    # Present the menu of choices
    print(MENU)
    menu_choice = input("What would you like to do: ")

    # Input user data
    if menu_choice == "1":  # This will not work if it is an integer!
        student_first_name = input("Enter the student's first name: ")
        student_last_name = input("Enter the student's last name: ")
        course_name = input("Please enter the name of the course: ")
        student_data = [student_first_name,student_last_name,course_name]
        students.append(student_data)
        print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
        continue

    # Present the current data
    elif menu_choice == "2":

        # Process the data to create and display a custom message
        print("-"*50)
        for student in students:
            print(f"Student {student[0]} {student[1]} is enrolled in {student[2]}")
        print("-"*50)
        continue

    # Save the data to a file
    elif menu_choice == "3":
        file = open(FILE_NAME, "w")
        for student in students:
            csv_data = f"{student[0]},{student[1]},{student[2]}\n"
            file.write(csv_data)
        file.close()
        print("The following data was saved to file!")
        for student in students:
            print(f"Student {student[0]} {student[1]} is enrolled in {student[2]}")
        continue

    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop
    else:
        print("Please only choose option 1, 2, or 3")

print("Program Ended")

# ------------------------------------------------------------------------------------------ #
# Define the Data Constants
MENU = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course
    2. Show current data  
    3. Save data to a file
    4. Exit the program
----------------------------------------- 
'''
FILE_NAME = "Enrollments.json"

# Define the Data Variables
student_first_name = ""
student_last_name = ""
course_name = ""
json_data = ""
file = None
menu_choice = ""
student_data = {}
students = []

# When the program starts, read the file data into a list of lists (table)
# Extract the data from the file
file = open(FILE_NAME, "r")
for row in file.readlines():
    student_data = row.split(',')
    student_data = [student_data[0], student_data[1], student_data[2].strip()]
    students.append(student_data)
file.close()

try:
    with open(FILE_NAME, 'r') as file:
        students = json.load(file)
except FileNotFoundError:
    print(f"{FILE_NAME} not found, starting with an empty list.")
except json.JSONDecodeError:
    print(f"Error decoding JSON from {FILE_NAME}, starting with an empty list.")
except Exception as e:
    print(f"An error occurred: {e}, starting with an empty list.")

# Present and Process the data
def register_student():
    global student_first_name, student_last_name, course_name
    try:
        student_first_name = input("Enter student's first name: ").strip()
        if not student_first_name:
            raise ValueError("First name cannot be empty.")
    except ValueError as ve:
        print(ve)
        return

    try:
        student_last_name = input("Enter student's last name: ").strip()
        if not student_last_name:
            raise ValueError("Last name cannot be empty.")
    except ValueError as ve:
        print(ve)
        return

    try:
        course_name = input("Enter course name: ").strip()
        if not course_name:
            raise ValueError("Course name cannot be empty.")
    except ValueError as ve:
        print(ve)
        return

    student_data = {
        "first_name": student_first_name,
        "last_name": student_last_name,
        "course_name": course_name
    }
    students.append(student_data)
    print("Student registered successfully.")

    def show_current_data():
    if not students:
        print("No data available.")
        return

    for student in students:
        print(f"First Name: {student['first_name']}, Last Name: {student['last_name']}, Course Name: {student['course_name']}")

def save_data_to_file():
    try:
        with open(FILE_NAME, 'w') as file:
            json.dump(students, file)
        print(f"Data saved to {FILE_NAME}.")
    except IOError as e:
        print(f"An error occurred while writing to the file: {e}")

 # Stop the loop
while True:
    print(MENU)
    menu_choice = input("Enter your choice (1-4): ").strip()

    if menu_choice == '1':
        register_student()
    elif menu_choice == '2':
        show_current_data()
    elif menu_choice == '3':
        save_data_to_file()
    elif menu_choice == '4':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")

