# Hill climbing algorithm

import numpy as np


def are_equal(state_1, state_2):
    return np.array_equal(state_1, state_2)


def find_index_of_element(state, element):
    x, y = np.where(state == element)
    return (x[0], y[0])


def d(current_state, final_state):
    total_distance = 0
    for value in np.nditer(final_state):
        if (value > 0):
            x_final, y_final = find_index_of_element(final_state, value)
            x_current, y_current = find_index_of_element(current_state, value)
            total_distance += abs(x_final - x_current) + abs(y_final - y_current)
    return total_distance


def swap_elements(state, index_1, index_2):
    if 0 <= index_2[0] < state.shape[0] and 0 <= index_2[1] < state.shape[1]:
        new_state = np.copy(state)
        new_state[index_1], new_state[index_2] = new_state[index_2], new_state[index_1]
        return new_state
    else:
        return state


def remove_given_elements_from_list(list_to_change, elements_to_remove):
    if len(elements_to_remove) == 0:
        return list_to_change
    else:
        modified_list = []
        for element_to_remove in elements_to_remove:
            for element in list_to_change:
                if not are_equal(element, element_to_remove):
                    modified_list.append(element)
        return modified_list


def is_in_the_list(element, list):
    for list_elem in list:
        if are_equal(list_elem, element):
            return True
    return False


def possible_transformations(state):
    x_0, y_0 = find_index_of_element(state, 0)
    neighbour_indices = [
        (x_0 + 1, y_0),
        (x_0 - 1, y_0),
        (x_0, y_0 + 1),
        (x_0, y_0 - 1)
    ]
    transformations = []
    for neighbour_index in neighbour_indices:
        transformed_state = swap_elements(state, (x_0, y_0), neighbour_index)
        if not are_equal(state, transformed_state):
            transformations.append(transformed_state)
    return transformations


def best_transformation(state, final_state):
    transformations = possible_transformations(state)
    best = transformations[0]
    for transformation in transformations:
        if d(transformation, final_state) < d(best, final_state):
            best = transformation
    return d(best, final_state), best


def hill_climbing(initial_state, final_state):
    L = [(d(initial_state, final_state), initial_state)]
    L_seen = []
    i = 0
    while len(L) > 0:
        n = L[0]
        i += 1
        if n[0] == 0:
            print("Final state reached in ", i, " iterations")
            return True
        else:
            best = best_transformation(n[1], final_state)
            if not is_in_the_list(best[1], L_seen):
                L.append(best)
            L.pop(0)
            L_seen.append(n[1])
            L = sorted(L, key=lambda tup: tup[0])
    print("Could not reach final state in ", i, " iterations")
    return False


def main():
    initial_state = np.random.choice(4, (2, 2), replace=False)
    final_state = np.array([[1, 2], [3, 0]])
    hill_climbing(initial_state, final_state)


main()
