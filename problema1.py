import numpy as np


def f(p):
    """Calculează funcția obiectiv pentru o permutare p."""
    count = 0
    for idx, elem in enumerate(p):
        if (p[idx] == p[elem]):
            count += 1
    return count


def generare_populatie(dim, n):
    """Generează o populație aleatoare de dimensiunea dim cu permutări de n elemente."""
    pop = []
    for _ in range(dim):
        p = np.random.permutation(n)
        pop.append(np.append(p, f(p)))
    return pop


def mutate_population(pop_input, pm):
    """Aplică mutația prin inserare la populație cu probabilitatea pm."""
    pop = pop_input.copy()
    for i in range(len(pop)):
        # Sansa pentru mutatie
        if np.random.rand() < pm:
            p = pop[i][:-1]  # Excludem ultimul element
            idx_from, idx_to = np.random.choice(len(p), 2, replace=False)
            # Se elimina un element si se foloseste cromozonul din idx_to
            p = np.insert(np.delete(p, idx_from), idx_to, p[idx_from])
            pop[i] = np.append(p, f(p))
    return pop


# print(f([0, 1, 3, 2]))
dim = 5  # Dimensiunea populației
n = 5    # Numărul de elemente în permutări
pop = generare_populatie(dim, n)
print(f"populatie initiala: {pop}")

pm = 0.3  # Probabilitatea de mutație

popm = mutate_population(pop.copy(), pm)

print(f"populatie finala: {popm}")
