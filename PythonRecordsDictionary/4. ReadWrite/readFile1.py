# In order to read the data stored in a text file, you must open it first. 
# Just like a book. You can’t read what is inside if you don’t open it first
"""
There are three modes for opening a file:
r	for only reading files
w	for only writing to files
a	for adding to an existing file
"""
# r	for only reading files
file1 = open("Part 7 Dict_data_Files/4. ReadWriteToFile/file1.txt","r")
readFile = file1.read() #assign the readfile method to readfile variable 
print(readFile) # print the contents read from the file 
file1.close()