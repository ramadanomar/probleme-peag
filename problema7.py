import numpy as np


def f(p):
    """Functia fitness"""
    count = 0
    for idx, val in enumerate(p):
        if p[idx] == p[val]:
            count += 1
    return count


def generare_populatie(dim, n):
    pop = []
    for _ in range(dim):
        perm = np.random.permutation(n)
        individ = [perm, f(perm)]
        pop.append(individ)
    return pop


def mutatie_populatie(pop_input, pm, n):
    """Aplica mutatia prin amestec pe populatie cu probabilitatea pm"""
    pop = pop_input.copy()
    popm = []
    for individ in pop:
        if np.random.rand() < pm:  # Verifica daca aplicam mutatia
            # Selecteaza doua pozitii aleatoare pentru a le interschimba
            idx1, idx2 = np.random.choice(n, 2, replace=False)
            # Copie a cromozomului pentru a nu modifica originalul
            perm_mutat = np.copy(individ[0])
            # Interschimbare valori
            perm_mutat[idx1], perm_mutat[idx2] = perm_mutat[idx2], perm_mutat[idx1]
            # Adauga individul mutat in noua populatie
            popm.append([perm_mutat, f(perm_mutat)])
        else:
            # Daca nu se aplica mutatia, adauga individul fara modificari
            popm.append(individ)
    return popm


dim = 10
n = 100
pm = 0.6
pop = generare_populatie(dim, n)
popm = mutatie_populatie(pop, pm, n)

print(pop)
print("\n")
print(popm)
