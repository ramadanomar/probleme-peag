import numpy as np


def f(x1, x2, x3, x4):
    """Functia fitness/obiectiv"""
    return 1 + np.sin(2*x1-x3)+(x2*x4)**(1/3)


def generare_populatie(dim):
    # Generarea aleatoare a populației
    pop = []

    for _ in range(dim):
        x1 = np.random.uniform(-1, 1, dim)
        x2 = np.random.uniform(0, 0.2, dim)
        x3 = np.random.uniform(0, 1, dim)
        x4 = np.random.uniform(0, 5, dim)

        pop.append(np.array([x1, x2, x3, x4]).T)

    return pop


def mutatie(populatie_input, pm):
    t = 0.6
    sigma = t / 3
    # Deep copy to avoid modifying the input directly
    populatie = [ind.copy() for ind in populatie_input]
    for ind in populatie:
        for j in range(ind.shape[1]):
            if np.random.rand() < pm:
                ind[:, j] += np.random.normal(0, sigma, ind.shape[0])
                # Ne asiguram ca raman in domeniu de definitie
                if j == 0:
                    ind[:, j] = np.clip(ind[:, j], -1, 1)
                elif j == 1:
                    ind[:, j] = np.clip(ind[:, j], 0, 0.2)
                elif j == 2:
                    ind[:, j] = np.clip(ind[:, j], 0, 1)
                elif j == 3:
                    ind[:, j] = np.clip(ind[:, j], 0, 5)
    return populatie


dim = 2
pm = 0.7
pop_initial = generare_populatie(dim)
pop_mutat = mutatie(pop_initial, pm)

print(pop_initial)
print("\n")
print(pop_mutat)
