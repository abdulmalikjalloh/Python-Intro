userData = open("Part 7 Dict_data_Files/4. ReadWriteToFile/userDetails.txt", "a")

fName = input("Enter firstname: ")
lName = input("Enter lastname: ")
age = int(input("Enter age: "))

"method 1"
# userData.write("\n" +fName+" "+ lName + " " + str(age))


# "method 2"
user = "\n"+ fName+" "+ lName + " " + str(age)
userData.write(user)


# "method 3"
userDataList =[]
userDataList.append(fName)
userDataList.append(lName)
userDataList.append(age)

strData = str(userDataList) # convert list to string
userData.write("\n" + strData)
userData.close()

