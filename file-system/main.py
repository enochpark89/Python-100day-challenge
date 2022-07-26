"""
1. Open and close file with python.
2. Open and close automatically with "with" keyword
3. Open and write on the file.

"""


# Open the file in python
import os.path

file = open("my_file.txt")
contents = file.read()
print(contents)
file.close()

# Open the file

with open("my_file.txt") as file:
    contents = file.read()
    print(contents)

# Write the file

with open("my_file.txt", mode="w") as file:
    file.write("\nNew text.")

with open("my_file.txt") as file:
    contents = file.read()
    print(contents)

# Output:
"""
Hello, my name is Alex.

Hello, my name is Alex.


New text.
"""
path = os.path.abspath("my_file.txt")
with open(path) as file:
    contents = file.read()
    print(contents)
