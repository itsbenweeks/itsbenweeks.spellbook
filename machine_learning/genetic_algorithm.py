import numpy as np


def generate_population(population_matrix, random_seeded=True):
    if random_seeded:
        np.random.seed(0)
    population_buffer = []
    for point in population_matrix:
        if type(point) == tuple or type(point) == list:
            population_buffer.add(
                (point[2] - point[1]) * np.random.random_sample() + point[2]
            )
        else:
            population_buffer.add(np.random.random_sample())
    population = np.ndarray(shape=(len(population_matrix),), buffer=population_buffer)
    return population


def determine_fitness(fitness_function, population):
    fitness_buffer = []
    for point in population:
        fitness_buffer.add(fitness_function(point))
    fitness_matrix = np.ndarray(shape=(len(population),), buffer=fitness_buffer)
    return fitness_population_matrix


def select_solution(fitness_population_matrix):
    np.sort(fitness_matrix)


def crossover_solutions(solution_matrix_1, solution_matrix_2):
    pass


def mutate_solution(solution_matrix):
    pass
