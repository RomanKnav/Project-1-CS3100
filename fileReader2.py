import csv
import math

# countries: 'kaggle files/data/countries-table.csv'
# olympics:  'kaggle files/data/Olympics 2024.csv'

# "Gold", "Silver", "Bronze"
medals = ["gold medals", "silver medals", "bronze medals"]

# this works:
# returns a list of a given country's stats:
def countryStats(country):
        stats = []

        with open('kaggle files/data/countries-table.csv') as file1:
            csvReader = csv.reader(file1, delimiter=',', quotechar='|')
        
            # loop through rows and check item 1:
            for row in csvReader:

                if country == row[0]:

                    for col in row:
                        stats.append(col)

                    return stats

            print("not a valid country!")

# this works:
def allCountries():
    with open('kaggle files/data/countries-table.csv') as file1:
        csvReader = csv.reader(file1, delimiter=',', quotechar='|')

        countries = []
        for row in csvReader:
            # add country names to countries
            countries.append(row[0])
        
        return countries
    
def getMedals(country, medal):
    # by this point, medal is fully formatted.

    with open('kaggle files/data/countries-table.csv') as file1:
        csvReader = csv.reader(file1, delimiter=',', quotechar='|')

        """
        Gold medal: 3
        Silver medal: 4 
        Bronze medal: 5
        """

        medalIndex = None

        # medal of any type:
        xMedals = 0

        match medal:
            case "Gold":
                medalIndex = 3
            case "Silver":
                medalIndex = 4
            case "Bronze":
                medalIndex = 5

        for row in csvReader:
            if (row[2] == country):
                xMedals += row[medalIndex]

        return xMedals


""" country keys:   
    0: country name
    1: world ranking by pop
    2: land area
    7: growth rate
    8: world percentage
    16: population 2023
    17: pop 2030
    18: pop 2050

    olympics key:
""" 

""""Queries:
    medals, athletics
"""

def loop():
    while True:
        print("input country:")
        country = input()

        query = None

        if country in allCountries():
            country1 = countryStats(country)
            country1Size = country1[3]
            country1Pop = country1[16]

            string = """
            Key Insights on %s:\n
            land area: %skm (%s miles)\n
            growth rate: %s percent a year\n
            Liklihood of being born in %s: %s percent\n
            population 2023: %s\n
            """  % (# country name
                    country,  
                    # size in km                      
                    country1Size, 
                    # size in miles     
                    format(float(country1Size) / 1.609344, ".2f"),
                    # annual growth rate
                    format(float(country1[7]) * 100, ".2f"), 
                    country,
                    # world population percentage
                    format(float(country1[8]) * 100, ".2f"),
                    #population in 2023
                    country1Pop)
            
            print(string)

            # we have a valid country:
            print("input query:")
            query = input()

            ##################SECOND INPUT#####################

            # we have a country (if statement works):
            if query in allCountries() and query != country1:
                country2 = countryStats(query)

                country2Size = country2[3]

                # these are LISTS:
                biggerCountry = None
                smallerCountry = None

                # these should ALSO be lists:
                biggerCountryPop = None
                smallerCountryPop = None
                biggerCountryPopName = None
                smallerCountryPopName = None

                if (country1Size > country2Size):
                    biggerCountry = country1
                    smallerCountry = country2
                else:
                    biggerCountry = country2
                    smallerCountry = country1

                # TODO: get NAME of bigger population country

                if (int(biggerCountry[16]) > int(smallerCountry[16])):
                    biggerCountryPopName = biggerCountry[0]
                    smallerCountryPopName = smallerCountry[0]
                    biggerCountryPop = int(biggerCountry[16])
                    smallerCountryPop = int(smallerCountry[16])
                    print(biggerCountryPopName, "has a bigger population than", smallerCountryPopName)
                else:
                    # THIS keeps running:
                    biggerCountryPopName = smallerCountry[0]
                    smallerCountryPopName = biggerCountry[0]
                    biggerCountryPop = int(smallerCountry[16])
                    smallerCountryPop = int(biggerCountry[16])

                size_quotient = math.floor(int(biggerCountry[3]) / 
                                           int(smallerCountry[3])
                                          )
                
                pop_quotient = math.floor(biggerCountryPop / 
                                          smallerCountryPop
                                        )

                if (size_quotient == 1):
                    print("\nYou can fit %s %s in %s" % (size_quotient, smallerCountry[0], biggerCountry[0]))
                else:
                    print("\nYou can fit %s %ss in %s" % (size_quotient, smallerCountry[0], biggerCountry[0]))

                print("\nthere are %s people in %s for every person in %s\n" % (pop_quotient, biggerCountryPopName, smallerCountryPopName))

            # compare sizes, populations, growth rates. 
            elif (query in medals):
                keyWord = (query.split(maxsplit=1)[0]).capitalize()
                # print(keyWord)
                print("this country possess", getMedals(country, keyWord), keyWord, "medals")


        else:
            # for first country:
            print("country not found in our advanced extensive database!")

loop()