"""
1. Create a Python file named lab_13-1.py
2. Create a dictionary called row.
3. Add key:value pairs to the dictionary for each person in the row,
where the key is the computer they are sitting at and the value is
their first name.
4. Print the dictionary and notice the order the key:value pairs are
listed in.
5. Imagine you were out for a day and someone else sat at your
computer. How would you update the dictionary to reflect this
change? Add this line after your print statement.
"""
#Author: Alsir Elsheikh

# Step 2: Create a dictionary called row
row = {}

# Step 3: Add key:value pairs to the dictionary for each person in the row
# Assume 'C1', 'C2', 'C3' represent computer IDs and 'Alice', 'Bob', 'Charlie' represent names
row['C1'] = 'Alice'
row['C2'] = 'Bob'
row['C3'] = 'Charlie'

# Step 4: Print the dictionary and notice the order of key:value pairs
print("Original Dictionary:")
print(row)

# Step 5: Update the dictionary to reflect the change if someone else sits at your computer
# Let's say someone else sits at 'C2' (your computer) and their name is 'Dave'
row['C2'] = 'Dave'
print("\nUpdated Dictionary:")
print(row)
