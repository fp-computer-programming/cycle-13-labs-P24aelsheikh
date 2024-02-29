"""
1. Create a Python file named lab_13-2.py
2. Create a dictionary named grades, that contains keys for each assignment
this quarter and the grade you received on it as the key. Make sure the
grades are out of 100.
3. Using a one-line statement, print a list of just all the grades you received.
4. Using a loop, print the name of each assignment in the dictionary on a
separate line.
5. Using another loop, print the name and grade you received on each
assignment that you scored an 70 or above on.
6. Using another loop, print the name and grade you received on each
assignment that you scored an 50 or below on.
"""
#Author: Alsir Elsheikh

# Step 2: Create a dictionary named grades
grades = {
    "Assignment1": 85,
    "Assignment2": 70,
    "Assignment3": 90,
    "Assignment4": 55,
    "Assignment5": 40
}

# Step 3: Print a list of just all the grades you received
print("All Grades Received:", list(grades.values()))

# Step 4: Print the name of each assignment in the dictionary on a separate line
print("\nNames of Assignments:")
for assignment in grades:
    print(assignment)

# Step 5: Print the name and grade you received on each assignment that you scored 70 or above on
print("\nAssignments with Scores 70 or Above:")
for assignment, grade in grades.items():
    if grade >= 70:
        print(f"{assignment}: {grade}")

# Step 6: Print the name and grade you received on each assignment that you scored 50 or below on
print("\nAssignments with Scores 50 or Below:")
for assignment, grade in grades.items():
    if grade <= 50:
        print(f"{assignment}: {grade}")
