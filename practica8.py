import numpy as np
import random


def read_distance_matrix(filename):
    with open(filename, 'r') as file:
        matrix = np.array([list(map(int, line.split(',')))
                          for line in file.read().splitlines()])
    return matrix


def initialize_population(pop_size, num_islands, n):
    return [random.sample(range(1, num_islands), n) for _ in range(pop_size)]


def calculate_fitness(route, distance_matrix, max_distance):
    total_distance = distance_matrix[0, route[0]]
    for i in range(len(route) - 1):
        total_distance += distance_matrix[route[i], route[i+1]]
    total_distance += distance_matrix[route[-1], 0]
    if total_distance > max_distance:
        return 0
    return 1 / total_distance


def select_parent(population, fitness):
    total_fitness = sum(fitness)
    pick = random.uniform(0, total_fitness)
    current = 0
    for i, f in enumerate(fitness):
        current += f
        if current > pick:
            return population[i]


def crossover(parent1, parent2):
    size = len(parent1)
    co_point = random.randint(0, size - 1)
    child = parent1[:co_point] + \
        [x for x in parent2 if x not in parent1[:co_point]]
    return child


def mutate(route, mutation_rate, num_islands):
    if random.random() < mutation_rate:
        i, j = random.sample(range(len(route)), 2)
        route[i], route[j] = route[j], route[i]
    return route


def genetic_algorithm(filename, pop_size, num_islands, n, max_distance, generations, mutation_rate):
    distance_matrix = read_distance_matrix(filename)
    population = initialize_population(pop_size, num_islands, n)
    for _ in range(generations):
        fitness = [calculate_fitness(
            route, distance_matrix, max_distance) for route in population]
        new_population = []
        for _ in range(pop_size):
            parent1 = select_parent(population, fitness)
            parent2 = select_parent(population, fitness)
            child = crossover(parent1, parent2)
            child = mutate(child, mutation_rate, num_islands)
            new_population.append(child)
        population = new_population
    best_route_index = np.argmax(fitness)
    return population[best_route_index]


filename = 'input_practica8.txt'
pop_size = 50
num_islands = 5
n = 3
max_distance = 100
generations = 100
mutation_rate = 0.01

best_route = genetic_algorithm(
    filename, pop_size, num_islands, n, max_distance, generations, mutation_rate)
print("Best route:", best_route)
