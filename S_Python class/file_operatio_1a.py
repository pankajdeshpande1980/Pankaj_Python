# file management
# 1. How to make the python interpretor to read in human format?
# ASCII - UTF-8
# 2. How to identify the location of the file?
# relative path - ~/Desktop, ablsolute path - /Users/santhoshsolomon/Desktop
# 3. How to deal with cross platform file locations?
# OS commands and path management library from Python helps

import os

# hard coding
# absolute_path = "\Users\panka\OneDrive\Documents\GitHub\PD_Python\test-file.txt"
absolute_path = r"C:\Users\panka\OneDrive\Documents\GitHub\PD_Python\test-file.txt.txt"

file_obj = open(absolute_path, mode="r")
data_read = file_obj.read()
file_obj.close()
print(data_read)
print(type(data_read))

file_obj = open(absolute_path, mode="r")
