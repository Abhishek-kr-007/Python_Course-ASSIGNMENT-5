# Function to create a dictionary with student names and marks
def create_student_dict():
    return {
        "Alice": 85,
        "Bob": 90,
        "Charlie": 78,
        "David": 92,
        "Eve": 88
    }


# Function to retrieve and display student marks
def get_student_marks(student_dict):
    student_name = input("Enter the student's name: ")
    marks = student_dict.get(student_name)

    if marks is not None:
        print(f"{student_name}'s marks: {marks}")
    else:
        print("Student not found.")


# Main program
students = create_student_dict()
get_student_marks(students)
