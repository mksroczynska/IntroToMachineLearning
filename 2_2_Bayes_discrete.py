import csv


# read file with data and return the data as dictionary
def read_csv(filename):
    data = []
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)
    return data


# return P(key == value)
def probability(key, value, data):
    N = len(data)
    occurences = 0
    for row in data:
        if row[key] == value:
            occurences += 1
    return occurences / N


# return set of different values of a key found in data
def possible_values(key, data):
    vals = set()
    for row in data:
        vals.add(row[key])
    return vals


# return P(key_checked == value_checked | key_condition == value_condition)
def conditional_probability(key_checked, value_checked, key_condition, value_condition, data):
    occurences_of_condition_value = 0
    occurences_of_checked_and_condition_value = 0
    for row in data:
        if row[key_condition] == value_condition:
            occurences_of_condition_value += 1
            if row[key_checked] == value_checked:
                occurences_of_checked_and_condition_value += 1
    return occurences_of_checked_and_condition_value / occurences_of_condition_value


# Probability that the object decribed by a vector of attributes can be classified as class c_j
# P(x|c_j) = Product_i P(x_i | c_j)
def vector_probability(vector, key_class, value_class, data):
    prob = 1
    for k, v in vector.items():
        prob *= conditional_probability(k, v, key_class, value_class, data)
    return prob


# check if an object described by a vector of attributes is already in a data
def is_in_data(vector, data):
    for row in data:
        this_row_is_identical = 1
        for k, v in vector.items():
            if row[k] != v:
                this_row_is_identical *= 0
        if this_row_is_identical:
            return True, row
    return False


# Finds the class c_j for which P(c_j) * \Product_i P(x_i | c_j) is the largest, returns its name
# If the object is already in data, returns the name of its class
def most_probable_class(vector, data):
    if is_in_data(vector, data)[0]:
        print("The given object is already in the data!")
        return is_in_data(vector, data)[1]['class']
    else:
        possible_classes = possible_values('class', data)
        most_prob_class = [0, '']
        for cj in possible_classes:
            prob_cj = vector_probability(vector, 'class', cj, data) * probability('class', cj, data)
            if prob_cj > most_prob_class[0]:
                most_prob_class = [prob_cj, cj]
        return most_prob_class[1]


data = read_csv('pies.csv')
x = {'shape': 'triangle',
     'crust-size': 'thick',
     'crust-shade': 'dark',
     'filling-size': 'thick',
     'filling-shade': 'gray'}
print("Possible classes of objects in given data: ", possible_values('class', data))
print("The most probable class for a given example: ", most_probable_class(x, data))
