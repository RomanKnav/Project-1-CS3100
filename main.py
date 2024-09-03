import csv
from collections import defaultdict

columns = defaultdict(list)

# my filepath is: 'kaggle files/kazakhstan.csv'
def read_csv_file(filepath):
    megalist = []

    megadict = {}

    # CREATE MEGADICT:
    with open(filepath) as myFile:
        csvReader = csv.reader(myFile, delimiter=',', quotechar='|')
        for row in csvReader:
            country_name = row[0]
            # print(country_name)       # prints each country

            if country_name not in megadict: 
                megadict[country_name] = []

            # for col in row:
            for col in row[1:]:
                megadict[country_name].append(col)

        for keys, values in megadict.items():
            print(keys)
            print(values)


read_csv_file('kaggle files/archive/countries-table.csv')


# TODO: store the entries in a list