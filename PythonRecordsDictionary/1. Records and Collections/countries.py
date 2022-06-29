countries = []  # create an empty list to add different countries
addCountries = True  # declare a flag variable of type Boolean which is true
# print(addCountry)
# This condition is true and will be executed because addCountry is set to true
while addCountries:
    # ask for user input respectively
    country = input("Enter country: ")
    countryCity = input("Enter city: ")
    size = int(input("Enter country size: "))
    countryPop = int(input("Enter country population: "))

    # add data captured and stored in the variables(country,countryCity..e.tc) from the user input to to their keys
    # the values stored/held in variables becomes the values in the dictionary
    aCountry = {
        "country": country,
        "city": countryCity,
        "countrySize": size,
        "population": countryPop,
    }
    # add data captured to the empty list players[]
    countries.append(aCountry)

    # check to add more data or not
    addACountry = input("Would you like to add another country? Y/N").upper()
    if (
        addACountry == "N"
    ):  # check if the user answer no, then no more data will me added
        addCountries = (
            False  # reset addCountry variable to a boolean datatype which is false
        )
print(countries)

# print record for a specific country
"index/number         0 ,       1 ,         2 ,         3     "

aCountryRecord = int(input("Enter the number of the record you want to display: "))
# accessing at record level

countryData = countries[aCountryRecord]
print(countryData)

# access data at the the key pair level
"""
country: key=country, value = countrName
"""
countryAttribute = input(f"What attribute from {countryData} you want to print: ")
print(countryData[countryAttribute])
