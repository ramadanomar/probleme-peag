import numpy as np
import random

"""
Cele N orașe stat din Grecia antică se luptă între ele pentru dominație, dar în fața unei amenințări
externe hotărăsc să se unească. Pentru a stabili planul de apărare, delegații orașelor urmează să se
întîlnească, fiecare oraș desemnîndu-și un singur reprezentant. Cunoscînd rivalitățile istorice dintre
orașe folosiți un algoritm genetic pentru a găsi o modalitate de așezare a delegaților la masa tratativelor
astfel încît delegații din orașe rivale să nu fie vecini (se presupune că acest lucru este posibil).
Harta orașelor stat între care există animozități este exprimată printr-o matricea pătratică de ordin N,
numită CONFLICT

CONFLICT(i,j) = {esteConflict ? 1 : 0}
"""

# Arangement will look like
# [0,5,3,1,2] - Which represents the first country (at index 0) - sits on the first seat
# second country sits 5th
# etc.


class Arangement:
    def __init__(self, conflict_matrix, arangement=None, seed=42):
        self.conflict_matrix = np.array(conflict_matrix)
        self.n = self.conflict_matrix.shape[0]  # Number of cities
        if arangement is None:
            self.arangement = self.generate_arangement()
        else:
            self.arangement = arangement
        self.nconflicts = self.compute_conflicts()
        np.random.seed(seed)

    def generate_arangement(self):
        return np.random.permutation(self.n)

    def compute_conflicts(self):
        conflicts = 0
        for i in range(self.n):
            # loopback mechanism (similar to circular list)
            next_city = (i + 1) % self.n
            if self.conflict_matrix[self.arangement[i], self.arangement[next_city]] == 1:
                conflicts += 1
        return conflicts

    def swap_multiple_cities(self, n_swaps):
        indices = np.random.choice(self.n, 2 * n_swaps, replace=False)
        for i in range(0, len(indices), 2):
            self.arangement[indices[i]], self.arangement[indices[i+1]
                                                         ] = self.arangement[indices[i+1]], self.arangement[indices[i]]
        self.nconflicts = self.compute_conflicts()  # Recalculate conflicts after swaps

    def optimize(self, population_size=100, generations=1000, n_swaps=2):
        population = [Arangement(self.conflict_matrix)
                      for _ in range(population_size)]
        for _ in range(generations):
            population = sorted(population, key=lambda x: x.nconflicts)
            # Elitism: carry the best 2 solutions to the next generation
            new_population = population[:2]
            while len(new_population) < population_size:
                # Select an individual from the top 50
                individual = random.choice(population[:50])
                new_individual = Arangement(
                    self.conflict_matrix, np.copy(individual.arangement))
                new_individual.swap_multiple_cities(n_swaps)
                new_population.append(new_individual)
            population = new_population
        return sorted(population, key=lambda x: x.nconflicts)[0]


# Example usage
conflict_matrix = [
    [0, 1, 0, 0, 1],
    [1, 0, 1, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 1, 0, 1],
    [1, 0, 0, 1, 0]
]

arrangement = Arangement(conflict_matrix)
optimal_arrangement = arrangement.optimize()
print("Solutions:", optimal_arrangement.arangement)
print("Constraints broken:", optimal_arrangement.nconflicts)

"""
EXPLANATION:
We just swap around positions of the cities until we minimise the number of conflict. We will converge to a local / global minima
due to our elitism selection mechanism.

Advantages:
- It's really simple to implement, we dont have to deal about generating a valid solution, etc.
- Due to the nature of our problem, generating permutations is pretty simple so it will run decently even on larger arrangements
due to the low computational "cost" associateed with generation a solution

Distavantages:
- Esentially this is a "fancy" way to do brute force. If our solution space increased drastically or the generation of a solution
was more "expensive" a.k.a. complex then this would never produce good solutions.

Things we can improve:
Represent the conflict matrix / solution an array of bits. This way we dont need to generate actual arrays for each individual
and can perform operations in constant time without the overhead of python loops
"""
