import csv
import math

######################## global variables ################################

nameIndex = 2
popIndex = 5
sizeIndex = 13
growthIndex = 15
percentIndex = 16

# "Gold", "Silver", "Bronze"
medals = ["gold medals", "silver medals", "bronze medals"]

################################################################################

def genPurposeReader(path):
    with open(path) as file:
        readCSV = csv.reader(file, delimiter=',', quotechar='"')
        return list(readCSV)  # a list of lists

countriesData = genPurposeReader('kaggle files/data/world_population.csv')
olympicsData = genPurposeReader('kaggle files/data/Olympics 2024.csv')

# returns a list of a given country's stats:
def countryStats(country):
    stats = []
    
    # loop through rows and check item 1:
    for row in countriesData:

        # check every single row for the given country name
        if country == row[nameIndex]:
            for col in row:
                stats.append(col)

            return stats

    return "not a valid country!"

# returns list of all country names:
def allCountries():
        countries = []
        for row in countriesData:
            countries.append(row[nameIndex])
        
        return countries

def getMedalIndex(medal):
    medalIndex = None

    match medal:
        case "Gold":
            medalIndex = 3
        case "Silver":
            medalIndex = 4
        case "Bronze":
            medalIndex = 5

    return medalIndex

# now time for work on olympics file:
def getMedals(country, medal):

    medalIndex = getMedalIndex(medal)

    """
    sport: 0
    Gold medal: 3
    Silver medal: 4 
    Bronze medal: 5
    total: 6
    """

    # determines index to search for specified medal
    # medalIndex = None

    # # medal of any type:
    xMedals = 0

    # match medal:
    #     case "Gold":
    #         medalIndex = 3
    #     case "Silver":
    #         medalIndex = 4
    #     case "Bronze":
    #         medalIndex = 5

    # every time country name appears, add the number of medals to xMedals:
    for row in olympicsData:
        if (row[2] == "\xa0" + country):
            medalsToAdd = row[medalIndex]
            xMedals += int(medalsToAdd)

    return xMedals

def medalSummary(country, medal):
    sportAndMedals = []

    medalIndex = None
    match medal:
        case "Gold":
            medalIndex = 3
        case "Silver":
            medalIndex = 4
        case "Bronze":
            medalIndex = 5

    # medal count of a certain type:
    medalCount = getMedals(country, medal)
    for row in olympicsData:
        sportName = row[0]

        if (row[2] == "\xa0" + country):
            sportAndMedals.append(sportName)
            sportAndMedals.append


# MAIN LOOP:
def loop():
    while True:
        print("input country:")
        country = input()

        query = None

        if country in allCountries():
            country1 = countryStats(country)
            country1Size = country1[sizeIndex]
            country1Pop = country1[popIndex]

            string = """
            Key Insights on %s:\n
            land area: %skm (%s miles)\n
            growth rate: %s percent a year\n
            Liklihood of being born in %s: %s percent\n
            population: %s\n
            """  % (# country name
                    country,  
                    # size in km                      
                    country1Size, 
                    # size in miles     
                    format(float(country1Size) / 1.609344, ".2f"),
                    # annual growth rate
                    float(country1[growthIndex]), 
                    country,
                    # world population percentage
                    format(float(country1[percentIndex]), ".2f"),
                    #population in 2023
                    country1Pop)
            
            print(string)

            # we have a valid country:
            print("input query:\n")
            query = input()

            ##################SECOND INPUT#####################

            # we have a country:
            if query in allCountries() and query != country1:
                country2 = countryStats(query)

                country2Size = country2[sizeIndex]

                # these become LISTS:
                biggerCountry = None
                smallerCountry = None

                # these become INTS:
                biggerCountryPop = None
                smallerCountryPop = None

                # strings:
                biggerCountryPopName = None
                smallerCountryPopName = None

                print(country1[nameIndex], country1[sizeIndex])
                print(country2[nameIndex], country2[sizeIndex])

                if (int(country1Size) > int(country2Size)):
                    biggerCountry = country1
                    smallerCountry = country2
                else:
                    biggerCountry = country2
                    smallerCountry = country1

                if (int(biggerCountry[popIndex]) > int(smallerCountry[popIndex])):
                    biggerCountryPopName = biggerCountry[nameIndex]
                    smallerCountryPopName = smallerCountry[nameIndex]
                    biggerCountryPop = int(biggerCountry[popIndex])
                    smallerCountryPop = int(smallerCountry[popIndex])
                    print(biggerCountryPopName, "has a bigger population than", smallerCountryPopName)
                else:
                    # this keeps running for India and Austria
                    biggerCountryPopName = smallerCountry[nameIndex]
                    smallerCountryPopName = biggerCountry[nameIndex]
                    biggerCountryPop = int(smallerCountry[popIndex])
                    smallerCountryPop = int(biggerCountry[popIndex])

                # big country size divided by small country size:
                size_quotient = math.floor(int(biggerCountry[sizeIndex]) / 
                                           int(smallerCountry[sizeIndex])
                                          )
                
                # big country population divided by small country population:
                pop_quotient = math.floor(biggerCountryPop / 
                                          smallerCountryPop
                                        )

                if (size_quotient == 1):
                    print("\nYou can fit %s %s in %s" % (size_quotient, smallerCountry[nameIndex], biggerCountry[nameIndex]))
                else:
                    print("\nYou can fit %s %ss in %s" % (size_quotient, smallerCountry[nameIndex], biggerCountry[nameIndex]))

                print("\nthere are %s people in %s for every person in %s\n" % (pop_quotient, biggerCountryPopName, smallerCountryPopName))

            # compare sizes, populations, growth rates. 
            elif (query in medals):
                # should be one of the three medal types:
                keyWord = (query.split(maxsplit=1)[0]).capitalize()

                medalsCount = getMedals(country, keyWord)

                pluralOrNot = "medal" if getMedals(country, keyWord) == 1 else "medals"

                # country is the original input:
                # print("\nthis country possess", str(getMedals(country, keyWord)), keyWord, "medals\n")
                print("\n" + country, "possesses", str(getMedals(country, keyWord)), keyWord, pluralOrNot)

                # getMedals(country, keyWord)


        else:
            # for first country:
            print("country not found in our advanced extensive database!")

loop()