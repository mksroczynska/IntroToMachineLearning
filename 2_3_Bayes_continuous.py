import csv
from math import exp, sqrt, pi
import matplotlib.pyplot as plt
import numpy as np


def read_csv(filename):
    data = []
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)
    return data


# return set of different values of a key found in data
def possible_values(key, data):
    vals = set()
    for row in data:
        vals.add(row[key])
    return vals

# count how many examples in data are classified asgiven class
def examples_in_the_class(data, class_value, class_name="class"):
    N = 0
    for row in data:
        if row[class_name] == class_value:
            N += 1
    return N


#
# # gaussian distribution
# def gauss(x, mean, variance):
#     return exp(-(x - mean) ** 2 / (2 * variance)) / sqrt(2 * pi * variance)
#
#
# # returns mean for the values of a given attribute in the class
# def mean(data, attribute_name, class_value, class_name="class"):
#     m = 0
#     N = len(data)
#     for row in data:
#         if row[class_name] == class_value:
#             m += row[attribute_name]
#     return m / N
#
#
# # returns mean for the values of a given attribute in all classes
# def variance(data, attribute_name, class_value, class_name='class'):
#     v = 0
#     m = mean(data, attribute_name, class_value, class_name)
#     N = len(data)
#     for row in data:
#         if row[class_name] == class_value:
#             v += (row[attribute_name] - m) ** 2
#     return v / (N - 1)


#p_{ci}(x)
def p(x, data, attribute_name, class_value,  variance=1):
    total_p = 0
    m = 0
    for row in data:
        if row['class'] == class_value:
            m += 1
            mu = float(row[attribute_name])
            total_p += exp(-(x - mu) ** 2 / (2 * variance))
    k = 1 / (sqrt(2 * pi * variance) ** m)
    return k * total_p


# return P(key == value)
def P(key, value, data):
    N = len(data)
    occurences = 0
    for row in data:
        if row[key] == value:
            occurences += 1
    return occurences / N


def p_vector(vector, data, class_value):
    pp = 1
    for k,v in vector.items():
        pp *= p(float(v), data, k, class_value)
    return pp


# the result: classify the given example
def most_probable_class(vector, data):
    possible_classes = possible_values('class', data)
    most_prob_class = [0, '']
    for cj in possible_classes:
        prob_cj = p_vector(vector, data, cj) * P('class', cj, data)
        if prob_cj > most_prob_class[0]:
            most_prob_class = [prob_cj, cj]
    return most_prob_class[1]


data = read_csv('example1.csv')
print("Possible classes: ", possible_values('class', data))

v = {'at1': 9, 'at2': 3.6, 'at3': 3.3}
print("The most probable class for a given example is: ", most_probable_class(v, data))

# x = np.arange(0, 10, 0.1)
# y = []
# for val in x:
#     y.append(p(val, data, 'at1', 'pos'))
# plt.plot(x, y)
# plt.show()
