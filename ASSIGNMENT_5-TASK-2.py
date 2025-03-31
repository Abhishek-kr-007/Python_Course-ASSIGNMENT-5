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
print("Original list:",numbers)
print("Extracted list:", extracted_list)
print("Reversed list:", reversed_list)
