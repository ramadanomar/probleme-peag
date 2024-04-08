import numpy as np


def f(x1, x2, x3):
    return 1 + np.sin(2*x1-x3)+np.cos(x2)


def genereaza_populatie(dim):
    pop = []
    for _ in range(dim):
        x1 = np.random.uniform(-1, 1)
        x2 = np.random.uniform(0, 1)
        x3 = np.random.uniform(-2, 1)

        pop.append(np.array([x1, x2, x3, f(x1, x2, x3)]).T)
    return pop


def crossover(pop_input, pc):
    populatie = pop_input.copy()
    populatie_crossover = []

    # Iteram prin perechi
    for i in range(0, len(populatie), 2):
        parinte1 = populatie[i]
        try:
            parinte2 = populatie[i+1]
        except IndexError:
            # Pt nr impar de indivizi, copiem primul parinte
            populatie_crossover.append(parinte1)
            break
        if np.random.rand() < pc:
            copil = (parinte1[:3] + parinte2[:3])/2
            copil = np.append(copil, f(copil[0], copil[1], copil[2]))
            populatie_crossover.append(copil)
        else:
            # Reproducere asexuala
            copil = parinte1 if np.random.rand() < 0.5 else parinte2
            populatie_crossover.append(copil)

    return populatie_crossover


dim = 6
pc = 0.6
popi = genereaza_populatie(dim)
popf = crossover(popi, pc)

print(popi)
print("\n")
print(popf)
