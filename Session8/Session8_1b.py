# File operations in Python

# Writing to a file
with open('example.txt', 'w') as file:
    file.write('Hello, this is a test file.\n')
    file.write('This is the second line.\n')

# Reading from a file
with open('example.txt', 'r') as file:
    content = file.read()
    print('File Content:')
    print(content)

# Appending to a file
with open('example.txt', 'a') as file:
    file.write('This is an appended line.\n')

# Reading line by line
with open('example.txt', 'r') as file:
    print('Reading line by line:')
    for line in file:
        print(line.strip())