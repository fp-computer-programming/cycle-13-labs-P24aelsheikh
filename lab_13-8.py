"""
1. Create a Python file named lab_13-8.py
2. Create a handle to open a file for writing called my_file.txt
3. Use the handle and the write method to add 3 lines to the file:
1. The first line should have your initials and today's date
2. The second line should have "Hello World!"
3. The final line should have what you have been doing for fun
4. Be sure to close the file. You can do this using the with statement
or using the close method.
5. Run the Python file and confirm that a file called my_file.txt
appears in the same folder as the Python file.
"""
# Author: Alsir Elsheikh

# Step 1: Create a Python file named lab_13-8.py

# Step 2-5: Open file, write lines, and close file
with open("my_file.txt", "w") as my_file:
    # Step 3: Write 3 lines to the file
    my_file.write("Initials: AE\nDate: 2024-02-29\n")
    my_file.write("Hello World!\n")
    my_file.write("For fun, I've been playing videogames.\n")
