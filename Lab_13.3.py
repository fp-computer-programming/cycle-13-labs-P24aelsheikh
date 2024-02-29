"""
1. Create a Python file named lab_13-3.py
2. Create a variable, weekdays and set it equal to a tuple that
contains the days Monday – Friday as strings.
3. Create a variable weekends and set it equal to a tuple that contains
Saturday and Sunday as strings.
4. Create a variable called days_of_the_week and set it equal to the
concatenation of the two previous variables.
5. Printing days_of_the_week should display a tuple containing all
the days of the week in order.
"""
# Author: ALsir Elsheikh

# This creates a variable, weekdays and set it equal to a tuple that contains the days Monday – Friday as strings.
weekdays = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday')

# This creates a variable weekends and set it equal to a tuple that contains Saturday and Sunday as strings.
weekends = ('Saturday', 'Sunday')

# This will create a variable called days_of_the_week and set it equal to the concatenation of the two previous variables.
days_of_the_week = weekdays + weekends

# Printing days_of_the_week should display a tuple containing all the days of the week in order.
print(days_of_the_week)
