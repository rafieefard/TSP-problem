import math
import time
import os
from itertools import permutations
def tsp1(city_distance):
    try_no = 0
    num_of_city = len(city_distance)
    min_path = []
    min_length = 0
    next_city = 0
    for counter in range(num_of_city):
        try_no += 1
        target = next_city
        min_path.append(next_city)
        shortest = max(city_distance[next_city]) + 1
        for city in range(num_of_city):
            try_no += 1
            if city_distance[next_city][city] < shortest and city != next_city and city not in min_path:
                shortest = city_distance[next_city][city]
                target = city
        next_city = target
        if len(min_path) < num_of_city:
            min_length += shortest
    min_path.append(0)
    min_length += city_distance[next_city][0]
    min_path = [i + 1 for i in min_path]
    try_no += len(min_path)
    answer = {'length': min_length, 'path': min_path, 'try': try_no}
    return answer
def tsp2(city_distance):
    try_no = 0
    num_of_city = len(city_distance)
    all_path = list(permutations(range(num_of_city)))
    for path_no in range(len(all_path)):
        try_no += 1
        all_path[path_no] += (all_path[path_no][0],)
    all_path_length = []
    for path_no in range(len(all_path)):
        try_no += 1
        path_length = 0
        for city in range(len(all_path[path_no]) - 1):
            try_no += 1
            path_length += city_distance[all_path[path_no][city]][all_path[path_no][city + 1]]
        all_path_length.append(path_length)
    path_min_no = all_path_length.index(min(all_path_length))
    min_path = [i + 1 for i in all_path[path_min_no]]
    try_no += len(all_path)
    min_length = min(all_path_length)
    answer = {'length': min_length, 'path': min_path, 'try': try_no}
    return answer
os.system('cls')
file = open('data.txt', 'r')
x, y = [], []
location = []
next(file)
for l in file:
    point = []
    row = l.split()
    x.append(int(row[0]))
    y.append(int(row[1]))
    location.append([int(row[0]), int(row[1])])
num_of_city = len(location)
city_distance = []
for first_city in range(num_of_city):
    row = []
    for second_city in range(num_of_city):
        dist_row = math.dist([x[first_city], y[first_city]], [x[second_city], y[second_city]])
        row.append(dist_row)
    city_distance.append(row)
print(row[i] for i in range(num_of_city))
print(city_distance)
print('Number of cities:', num_of_city)
print('location of cities:', location)
print('----------------------------------------------------------')
print('nearest- neighbor heuristic algorithm:')
print('This algorithm is fast but not guaranteed to find an optimal tour')
start = time.time()
answer = tsp1(city_distance)
end = time.time()
print('Shortest path:', answer['path'])
print('Shortest path length:', answer['length'])
print('number of try:', answer['try'])
print('Runtime of the program:', end - start, 'seconds')
print('----------------------------------------------------------')
print('2. very slow algorithm:')
print('This algorithm tries all permutations and guaranteed optimal solution but is very slow')
start = time.time()
answer = tsp2(city_distance)
end = time.time()
print('Shortest path:', answer['path'])
print('Shortest path length:', answer['length'])
print('number of try:', answer['try'])
print('Runtime of the program:', end - start, 'seconds')
