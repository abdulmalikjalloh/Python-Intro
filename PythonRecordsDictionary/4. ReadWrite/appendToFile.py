# In order to read the data stored in a text file, you must open it first. 
# Just like a book. You can’t read what is inside if you don’t open it first
"""
There are three modes for opening a file:
r	for only reading files
w	for only writing to files
a	for adding to an existing file
"""
# a	for adding to an existing file
# variablename = file2

file2 = open("Part 7 Dict_data_Files/4. ReadWriteToFile/file2.txt", "a")
addFile = file2.write("This file was created using the a flag")
file2.close()
