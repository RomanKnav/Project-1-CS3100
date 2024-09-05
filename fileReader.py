import csv
from collections import defaultdict

# countries: 'kaggle files/countries-table.csv'
# olympics:  'kaggle files/Olympics 2024.csv'

def read_country_file(countryData):

    # list of items:
    countrylist = []
    # dictionary (key: country name, value: country data list)
    countrydict = {}

    # need to repeat for the olympics ({country: [olympic data]})

    # create countrydict:
    with open(countryData) as file1:
        csvReader = csv.reader(file1, delimiter=',', quotechar='|')

        for row in csvReader:
            country_name = row[0]

            if country_name not in countrydict: 
                countrydict[country_name] = []

            # for col in row:
            for col in row[1:]:
                countrydict[country_name].append(col)

                # add to list:
                countrylist.append(col)

        # for keys, values in countrydict.items():
        #     print(keys)
        #     print(values)

        # return countrylist
        return countrydict

        # landarea = countrydict[2]
        # pop2023 = countrydict[15]

def read_olympic_file(olympicData):
    olympicDict = {}

    with open(olympicData) as file2:
        csvReader2 = csv.reader(file2, delimiter=',', quotechar='|')

""" countries key:    
    1: land area
    5: growth rate
    6: world percentage
    14: population 2023
    15: pop 2030
    16: pop 2050

    olympics key:
""" 
countrydata = read_country_file('kaggle files/data/countries-table.csv')

# should be able to accept BOTH country and olympic queries:
while True:
    print("input country:")
    country = input.lower()

    query = None

    if country in countrydata.keys():

        # we have a valid country:
        print("input query:")
        query = input.lower()

        # we should also print a neat list of interesting facts of the country before query:


        # check if query is a country, medal type, or sport:
        if query in countrydata.keys() or query in 


    else:
        print("Country not found!")
        continue

    if query in countrydata.keys():
        # query is a country
        if country
