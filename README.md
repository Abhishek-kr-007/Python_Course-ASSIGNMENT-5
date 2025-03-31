# Python_Course-ASSIGNMENT-5

# TASK-1 Create a Dictionary of Student Marks

# Student Marks Lookup

This Python script allows users to create a dictionary containing student names and their corresponding marks. Users can then input a student's name to retrieve and display their marks.

## Features

- **Create Student Dictionary**: Initializes a dictionary with predefined student names and their marks.
- **Retrieve Student Marks**: Prompts the user to enter a student's name and retrieves their marks from the dictionary.

## Usage

1. Ensure you have Python installed on your machine.
2. Run the script in your terminal or command prompt.
3. Follow the prompt to enter a student's name to retrieve their marks.

### Example

When you run the script, it will prompt you for a student's name:

```plaintext
Enter the student's name: Alice
Alice's marks: 85
If the student is not found, it will display:

plaintext
Run
Copy code
Student not found.
Code
Here is the code for the student marks lookup:

python
Run
Copy code
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
Error Handling
If the user inputs a name that is not in the dictionary, the script will output a message indicating that the student was not found.
License
This project is licensed under the MIT License - see the LICENSE file for details


# TASK-2 Demonstrate List Slicing 


# Number List Manipulation

This Python script demonstrates basic list operations, including creating a list of numbers, extracting a subset of that list, and reversing the extracted elements.

## Features

- **Create Number List**: Generates a list of numbers from 1 to 10.
- **Extract First Five Elements**: Retrieves the first five elements from the list.
- **Reverse Extracted Elements**: Reverses the order of the extracted elements.

## Usage

1. Ensure you have Python installed on your machine.
2. Run the script in your terminal or command prompt.
3. The script will display the original list, the extracted list, and the reversed list.

### Example Output

When you run the script, you will see output similar to the following:

```plaintext
Original list: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Extracted list: [1, 2, 3, 4, 5]
Reversed list: [5, 4, 3, 2, 1]
Code
Here is the code for the number list manipulation:

python
Run
Copy code
# Function to create a list of numbers from 1 to 10
def create_number_list():
    return list(range(1, 11))

# Function to extract the first five elements
def extract_first_five(num_list):
    return num_list[:5]

# Function to reverse the extracted elements
def reverse_list(sub_list):
    return sub_list[::-1]

# Main program
numbers = create_number_list()
extracted_list = extract_first_five(numbers)
reversed_list = reverse_list(extracted_list)

# Print results
print("Original list:", numbers)
print("Extracted list:", extracted_list)
print("Reversed list:", reversed_list)
Error Handling
This script does not include specific error handling, as it operates on a fixed range of numbers. However, it assumes that the list will always contain at least five elements.

License
This project is licensed under the MIT License - see the LICENSE file for details.
