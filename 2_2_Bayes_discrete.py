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


def joint_probability(key1, value1, key_condition, value_condition, data):  # TODO change names of args
    N = len(data)
    occurences = 0
    for row in data:
        if row[key1] == value1 and row[key_condition] == value_condition:
            occurences += 1
    return occurences / N


data = read_csv('pies.csv')
print(len(data))
number_of_circles = count_occurences('shape', 'circle', data)
prob_circ_pos = joint_probability('shape', 'circle','class', 'pos', data)
print(prob_circ_pos)
