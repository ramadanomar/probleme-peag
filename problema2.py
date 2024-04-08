import numpy as np


def f(x, y):
    """Functia obiectiv"""
    return y * (np.sin(x-2))**2


def generare_populatie(dim):
    pop = []
    for _ in range(dim):
        x = np.random.randint(1, 1501)
        y = np.random.randint(-1, 2501)

        x_bin = np.binary_repr(x)
        y_bin = np.binary_repr(y)

        individ = [x_bin, y_bin, f(x, y)]

        pop.append(individ)
    return pop


dim = 10
pc = 0.7


def recombinare(pop_input, pc, dim):
    pop = pop_input.copy()
    np.random.shuffle(pop)

    # Noua populatie
    popc = []

    # Iteram in perechea de cromozoni (indivizi)
    for i in range(0, len(pop), 2):
        parinte1 = pop[i]
        try:
            parinte2 = pop[i+1]
        except IndexError:
            # Daca este un nr impar de elem, ultimul va fi copiat
            popc.append(parinte1)
            break

        # Mutatie
        if np.random.rand() < pc:
            # Aplicam incrucisarea

            # Alegem 3 puncte aleatorii
            puncte = sorted(np.random.choice(
                range(1, max(len(parinte1[0]), len(parinte1[1]))), 3, replace=False))

            copil1, copil2 = '', ''

            # Formare cromozoni copii
            for j in range(len(puncte)+1):
                # ne asiguram sa n avem index negativ
                start = puncte[j-1] if j > 0 else 0
                end = puncte[j] if j < len(puncte) else max(
                    len(parinte1[0]), len(parinte1[1]))

                if j % 2 == 0:
                    copil1 += parinte1[0][start:end]
                    copil2 += parinte2[0][start:end]
                else:
                    copil1 += parinte2[0][start:end]
                    copil2 += parinte1[0][start:end]

            # Calculcam calitatea copiilor
            x1, y1 = int(copil1, 2), int(parinte1[1], 2)
            x2, y2 = int(copil2, 2), int(parinte2[1], 2)
            popc.append([copil1, parinte1[1], f(x1, y1)])
            popc.append([copil2, parinte2[1], f(x2, y2)])
        else:
            # Reproducere asexuala
            popc.append(parinte1)
            if len(popc) < dim:
                popc.append(parinte2)

    return popc


populatie = generare_populatie(dim)
populatie_recombinata = recombinare(populatie, pc, dim)
print(populatie)
print(populatie_recombinata)
