import csv
import math

# countries: 'kaggle files/data/countries-table.csv'
# olympics:  'kaggle files/data/Olympics 2024.csv'

medals = ["Gold", "Silver", "Bronze"]

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

            # check if query is a country, medal type, or sport:
            # looks like I'll have to make lists for medals and sports

            ##################SECOND INPUT#####################

            # we have a country (if statement works):
            if query in allCountries() and query != country1:
                country2 = countryStats(query)

                country2Size = country2[3]
                country2Pop = country2[16]

                # these are LISTS:
                biggerCountry = None
                smallerCountry = None

                biggerCountryPop = None
                smallerCountryPop = None

                if (country1Size > country2Size):
                    biggerCountry = country1
                    smallerCountry = country2
                else:
                    biggerCountry = country2
                    smallerCountry = country1

                if (biggerCountry[16] > smallerCountry[16]):
                    print(biggerCountry[0], "population:", biggerCountry[16])
                    print(smallerCountry[0], "population:", smallerCountry[16])
                    biggerCountryPop = biggerCountry[16]
                    smallerCountryPop = smallerCountry[16]
                else:
                    print(smallerCountry, "has the bigger population")
                    biggerCountryPop = smallerCountry[16]
                    smallerCountryPop = biggerCountry[16]

                size_quotient = math.floor(int(biggerCountry[3]) / 
                                           int(smallerCountry[3])
                                          )
                
                pop_quotient = math.floor(int(biggerCountryPop) / 
                                          int(smallerCountryPop
                                        ))

                if (size_quotient == 1):
                    print("You can fit %s %s in %s" % (size_quotient, smallerCountry[0], biggerCountry[0]))
                else:
                    print("You can fit %s %ss in %s" % (size_quotient, smallerCountry[0], biggerCountry[0]))

                print("\nthere are %s people in %s for every person in %s" % (pop_quotient, biggerCountry[0], smallerCountry[0]))


                # compare sizes, populations, growth rates. 

        else:
            # for first country:
            print("country not found in our advanced extensive database!")

loop()