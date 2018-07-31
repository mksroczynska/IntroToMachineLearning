import csv


def read_csv(filename):
    data = []
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)
    return data


def count_occurences(key, value, data):
    occurences = 0
    for row in data:
        if row[key] == value:
            occurences += 1
    return occurences
