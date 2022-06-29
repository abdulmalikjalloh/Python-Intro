# In order to read the data stored in a text file, you must open it first. 
# Just like a book. You can’t read what is inside if you don’t open it first
"""
There are three modes for opening a file:
r	for only reading files
w	for only writing to files
a	for adding to an existing file
"""

# w flag: write to a file if it exists or create and write to a file if it does not exist 
file1 = open("Part 7 Dict_data_Files/4. ReadWriteToFile/file1.txt","w")
# file1 = open("file1.txt","w")
# f = open("myfile.txt", "x")
file1.write("This is my file") #use the filebane.writemethod to write to a file
file1.close() # to close the file

