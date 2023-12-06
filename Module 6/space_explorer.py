from random import seed, sample, choice
from os import linesep
from string import punctuation
from math import sqrt
from itertools import product
from operator import itemgetter

SEED_NUMBER = 1024
seed(SEED_NUMBER)
MAP_SIZE = 100
all_possible_symbols = frozenset(punctuation+'GSFT ')


def define_possible_objects(choices=punctuation):
    chars = choices
    chars += 'G'
    chars += 'T'*3
    chars += 'F'*3
    return chars


def generate_object(itera, available_coordinates, occupied_coordinates):
    symbol = sample(itera, 1)
    coordinates = choice(available_coordinates)
    available_coordinates.remove(coordinates)
    occupied_coordinates.append(coordinates)
    return symbol, coordinates


def set_up():
    symbols1 = define_possible_objects(punctuation)
    symbols2 = define_possible_objects('^&*'*5)
    return symbols1, symbols2


def generate_available_coordinates(map_size):
    available_coordinates = list(product(range(0, map_size), range(0, map_size)))
    return available_coordinates
    pass


def generate_empty_map(available_coordinates):
    galaxy_map = {}
    for coordinate in available_coordinates:
        if coordinate == (0,0):
            galaxy_map.update({coordinate: 'S'})
        else:
            galaxy_map.update({coordinate: ' '})
    return galaxy_map
    pass


def get_unique_objects(galaxy_map):
    unique_objects = []
    for value in galaxy_map.values():
        unique_objects.append(value)
    unique_objects = frozenset(unique_objects)
    return unique_objects
    pass


def symbols_not_used_in_galaxy(symbols_in_galaxy):
    not_used = set()
    for symbol in all_possible_symbols:
        if symbol not in symbols_in_galaxy:
            not_used.add(symbol)
    return frozenset(not_used)
    pass


def common_objects_encountered(galaxy_1_objects, galaxy_2_objects):
    result = galaxy_1_objects.intersection(galaxy_2_objects)
    return result
    pass


def objects_encountered_in_galaxy1_not_galaxy2(galaxy_1_objects, galaxy_2_objects):
    result = galaxy_1_objects.difference(galaxy_2_objects)
    return result
    pass


def objects_encountered_in_galaxy2_not_galaxy1(galaxy_1_objects, galaxy_2_objects):
    result = galaxy_2_objects.difference(galaxy_1_objects)
    return result
    pass


def objects_encountered_in_both_galaxys(galaxy1_objects, galaxy2_objects):
    result = galaxy1_objects.union(galaxy2_objects)
    return result
    pass


def calculate_path_to_goal(sorted_object_list):
    objects_of_interest = []
    for item in sorted_object_list:
        if item[2] != ['G']:
            if item[2] == ['F'] or item[2] == ['T']:
                objects_of_interest.append(item)
            else:
                continue
        else:
            objects_of_interest.append(item)
            break
    return objects_of_interest
    pass


def display_galaxy(galaxy_map):
    counter = 0
    concatenated_objects_str = ""
    for value in galaxy_map.values():
        concatenated_objects_str += str(value)
        counter += 1
        if (counter/MAP_SIZE) >= 1 and (counter % MAP_SIZE) == 0:
            concatenated_objects_str += "\n"
    return concatenated_objects_str
    pass


def calculate_euclidean_distance(coordinates):
    x, y = coordinates
    euclidean_distance = sqrt((x**2) + (y**2))
    return int(euclidean_distance)
    pass


def populate_galaxy_map(available_symbols, available_coordinates, occupied_coordinates, galaxy_map):
    objects_encountered_list = list()
    while True:
        symbol, coordinates = generate_object(available_symbols, available_coordinates, occupied_coordinates)
        distance = calculate_euclidean_distance(coordinates)
        # insert your code here
        objects_encountered_list.append((distance, coordinates, symbol))
        galaxy_map.update({coordinates: symbol[0]})
        if symbol == ["G"]:
            break
            
    # insert your code here
    objects_encountered_list = sorted(objects_encountered_list)
    return objects_encountered_list
    pass


def run_exploration():
    available_symbols1, available_symbols2 = set_up()

    available_coordinates1 = generate_available_coordinates(MAP_SIZE)
    available_coordinates2 = generate_available_coordinates(MAP_SIZE)
    occupied_coordinates1 = list()
    occupied_coordinates2 = list()

    galaxy_map_1 = generate_empty_map(available_coordinates1)
    galaxy_map_2 = generate_empty_map(available_coordinates2)

    explorer1_list = populate_galaxy_map(available_symbols1, available_coordinates1, occupied_coordinates1, galaxy_map_1)
    explorer2_list = populate_galaxy_map(available_symbols2, available_coordinates2, occupied_coordinates2, galaxy_map_2)

    print(explorer1_list)
    print(explorer2_list)

    path_list1 = calculate_path_to_goal(explorer1_list)
    print(path_list1)

    path_list2 = calculate_path_to_goal(explorer2_list)
    print(path_list2)

    display_galaxy(galaxy_map_1)
    display_galaxy(galaxy_map_2)
    galaxy2_symbols = get_unique_objects(galaxy_map_2)
    galaxy1_symbols = get_unique_objects(galaxy_map_1)
    print(galaxy1_symbols)
    print(galaxy2_symbols)


if __name__ == '__main__':
    run_exploration()

if __name__ == '__main__':
    run_exploration()
