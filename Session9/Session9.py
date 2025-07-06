# file management
# 1. How to make the python interpretor to read in human format?
# ASCII - UTF-8
# 2. How to identify the location of the file?
# relative path - ~/Desktop, ablsolute path - /Users/santhoshsolomon/Desktop
# 3. How to deal with cross platform file locations?
# OS commands and path management library from Python helps

import os

# hard coding
absolute_path = "\Users\panka\OneDrive\Documents\GitHub\PD_Python\test-file.txt"

# # dynamic handling
# current_directory = os.getcwd()
# target_file = os.path.join(current_directory, "test-file.txt")


# 1. Read the file content

file_obj = open(absolute_path, mode="r")
data_read = file_obj.read()
file_obj.close()

file_obj = open(absolute_path, mode="r")
data_readline = file_obj.readline()
file_obj.close()

file_obj = open(absolute_path, mode="r")
data_readlines = file_obj.readlines()
file_obj.close()

print(data_read)
print(type(data_read))

print(data_readline)
print(type(data_readline))

print(data_readlines)
print(type(data_readlines))

# garbage collector - gc

# 2. Write operations
absolute_write_path = "/Users/santhoshsolomon/Desktop/test-file-cp.txt"
write_file_obj = open(absolute_write_path, "w")
sample_text_string = "Pankaj\nDeshpande\n"
write_file_obj.write(sample_text_string)
write_file_obj.close()

write_file_obj = open(absolute_write_path, "w")
sample_text_list = ["pankaj\n", "deshpande\n"]
write_file_obj.writelines(sample_text_list)
write_file_obj.close()

# 3. append operations
write_file_obj = open(absolute_write_path, "a")
sample_text_list = ["santhosh\n", "solomon\n"]
write_file_obj.writelines(sample_text_list)
write_file_obj.close()
