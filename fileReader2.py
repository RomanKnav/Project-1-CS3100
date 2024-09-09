import csv
import math

########## global variables and genPurposeReader function/objects ###############

nameIndex = 2
popIndex = 5
sizeIndex = 13
growthIndex = 15
percentIndex = 16

# "Gold", "Silver", "Bronze", "Total" -these are valid medal strings to input for query:
medals = ["gold medals", "silver medals", "bronze medals", "total medals"]

# reads a given csv file and returns it as a list of lists (1 row = 1 sublist):
def genPurposeReader(path):
    with open(path) as file:
        readCSV = csv.reader(file, delimiter=',', quotechar='"')
        return list(readCSV)  # a list of lists

countriesData = genPurposeReader('kaggle files/data/world_population.csv')
olympicsData = genPurposeReader('kaggle files/data/Olympics 2024.csv')

########################## functions ######################################################

# returns a list of a given country's stats:
def countryStats(country):
    stats = []
    
    # loop through rows and check item at nameIndex:
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

# returns index of given medal type (3, 4, 5, or 6)
def getMedalIndex(medal):
    medalIndex = None

    match medal:
        case "Gold":
            medalIndex = 3
        case "Silver":
            medalIndex = 4
        case "Bronze":
            medalIndex = 5
        case "Total":
            medalIndex = 6

    return medalIndex

# now time for work on olympics file:
# returns medal count of X type
def getMedals(country, medal):

    medalIndex = getMedalIndex(medal)

    """
    sport: 0
    Gold medal: 3
    Silver medal: 4 
    Bronze medal: 5
    total: 6
    """

    # # medal of any type:
    xMedals = 0

    # every time country name appears, add the number of medals to xMedals:
    for row in olympicsData:
        if (row[2] == "\xa0" + country):
            medalsToAdd = row[medalIndex]
            xMedals += int(medalsToAdd)

    return xMedals

# this is a summary for a SINGLE medal type:
def medalSummary(country, medal):

    # only strings:
    sportAndMedals = []

    medalIndex = getMedalIndex(medal)

    # medal count of a certain type:
    medalCount = getMedals(country, medal)

    summary = """"""

    if (medalCount > 0): 
        for row in olympicsData:
            sportName = row[0]

            if (row[2] == "\xa0" + country):
                rowMedalCount = row[medalIndex]

                if (int(rowMedalCount) > 0):
                    sportAndMedals.append(sportName)
                    sportAndMedals.append(rowMedalCount)



        for i in range(1, len(sportAndMedals), 2):
            summary += "\t\t%s, %s \n\n" % (sportAndMedals[i - 1], sportAndMedals[i])
            
    # return sportAndMedals
    return summary

# print(medalSummary("Canada", "Gold"))

# MAIN LOOP:
def loop():
    while True:
        print("\ninput country:")
        country = input()

        # for second input, assigned on 168:
        query = None

        if country in allCountries():
            country1 = countryStats(country)
            country1Size = country1[sizeIndex]
            country1Pop = country1[popIndex]

            # how "{:,}".format() works: 
            # {} is where formatting stuff goes into
            # "," ensures that the thousands (every 3 numbers) are seperated by commas. 
            string = """
            Key Insights on %s:\n
            land area: %skm (%s miles)\n
            growth rate: %s percent a year\n
            Liklihood of being born in %s: %s percent\n
            population: %s\n
            """  % (# country name
                    country,  
                    # size in km                      
                    "{:,}".format(int(country1Size)), 
                    # size in miles     
                    "{:,}".format(float(format(float(country1Size) / 1.609344, ".2f"))),
                    # annual growth rate
                    float(country1[growthIndex]), 
                    country,
                    # world population percentage
                    format(float(country1[percentIndex]), ".2f"),
                    #population in 2023
                    "{:,}".format(int(country1Pop)))
            
            print(string)

            # we have a valid country:
            print("input query:")
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

                # if first country's size (km) is bigger than small country's size:
                if (int(country1Size) > int(country2Size)):
                    biggerCountry = country1
                    smallerCountry = country2
                else:
                    biggerCountry = country2
                    smallerCountry = country1

                # if the bigger country has a larger POPULATION:
                if (int(biggerCountry[popIndex]) > int(smallerCountry[popIndex])):
                    biggerCountryPopName = biggerCountry[nameIndex]
                    smallerCountryPopName = smallerCountry[nameIndex]
                    biggerCountryPop = int(biggerCountry[popIndex])
                    smallerCountryPop = int(smallerCountry[popIndex])
                else:
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

                medalsPluralOrNot = "medal:" if getMedals(country, keyWord) == 1 else "medals:"

                medalsToPeople = None

                # if medalsCount equals 0, set medalsToPeople to regular population:
                try:
                    medalsToPeople = math.floor(int(country1Pop) / medalsCount)
                except ZeroDivisionError:
                    medalsToPeople = country1Pop

                # we don't want to say "for every Total medal":
                totalOrNot = '' if keyWord == "Total" else keyWord

                # country is the original input:
                print("\n*************2024 Olympics:*************")

                if getMedals(country, keyWord) > 0: 
                    print("\n" + country, "possesses", str(getMedals(country, keyWord)), keyWord, medalsPluralOrNot)

                    print("\n" + medalSummary(country, keyWord))

                    print("For every %s medal, there are %s people living in %s" % (totalOrNot, "{:,}".format(medalsToPeople), country))
                else:
                    print("%s has no %s medals" % (country, keyWord))
        else:
            # for first country:
            print("\ncountry not found in our advanced extensive database!")

loop()