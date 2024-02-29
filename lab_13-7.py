#Author: Alsir ELsheikh
# Step 1: Create a Python file named lab_13-7.py

# Step 2: Assuming alma_mater.txt is in the same directory as lab_13-7.py

# Step 3: Using the reading files all at once method, read the alma_mater.txt file and print the lines to the console in reverse order, with a blank line between each line.

file_path = "alma_mater.txt.txt"  # Assuming alma_mater.txt is in the same directory as lab_13-7.py

try:
    with open(file_path, 'r') as file:
        lines = file.readlines()  # Read all lines at once

        for line in reversed(lines):
            print(line.strip())  # Print each line in reverse order
            print()  # Print a blank line after each line
except FileNotFoundError:
    print("File not found.")
