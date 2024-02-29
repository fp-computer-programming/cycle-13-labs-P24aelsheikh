"""
1. Create a Python file named lab_13-4.py
2. Create a list called day_date that contains the number day for the
next 5 days, starting with, "2", for today.
3. Using a tuple, assign the 5 letters from the list to a variable that
represents each day using a single statement. The variables can be
something like, thu, fri, mon, tue, wed. Look at the last slide of
notes for help.
4. Print each of the variables (thu, fri, mon, tue, wed) to see what
they equal.
"""
# Author: Alsir Elsheikh

# This creates a list called day_date that contains the number day for the next 5 days, starting with "2" for today.
day_date = [2, 3, 4, 5, 6]  # Assuming today is the 2nd day of the month

# Using a tuple, this assigns the 5 letters from the list to a variable that represents each day using a single statement.
thu, fri, mon, tue, wed = tuple(day_date)  # Assigning each value from day_date to respective variables

# This just prints each of the variables (thu, fri, mon, tue, wed) to see what they equal.
print("Thursday:", thu)
print("Friday:", fri)
print("Monday:", mon)
print("Tuesday:", tue)
print("Wednesday:", wed)
