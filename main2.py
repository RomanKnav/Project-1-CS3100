import csv

def load_data(filename)
    myList = []
    with open(filename) as data:
        countries_data = csv.reader(data, delimiter=',')


# TODO: store the entries in a list