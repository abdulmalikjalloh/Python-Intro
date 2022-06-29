
# r	for only reading files
searchFile = input("Enter search keyword: ")
# Use the with keyword followed by open method (filepath/filename) as variable name
with open("Part 7 Dict_data_Files/4. ReadWriteToFile/userDetails.txt","r") as file1:
    readFile = file1.read() #assign the readfile method to readfile variable 
    # print(readFile) # print the contents read from the file

if searchFile in readFile:
    print(f"found {searchFile}")
else:
    print(f"{searchFile} Not Found!")

 
