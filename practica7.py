import numpy as np

# Problem data
COMBINATIONS = np.array([
    [0.30, 0.25, 0.25, 0.20],
    [0.75, 0.00, 0.25, 0.00],
    [0.25, 0.25, 0.25, 0.25],
    [0.00, 0.00, 1.00, 0.00],
    [1.00, 0.00, 0.00, 0.00]
])

# Convert kg to number of packets
FRUIT_QUANTITIES = np.array([100, 80, 120, 50]) * 1000 / 200
PROFIT_PER_PACKET = np.array([20, 10, 15, 12, 5])
MAX_ITERATIONS = 1000
STEPSIZE = 10


def calculate_profit(production):
    profit = np.sum(PROFIT_PER_PACKET * production)
    fruit_usage = np.dot(production, COMBINATIONS)
    penalty = np.sum(np.maximum(fruit_usage - FRUIT_QUANTITIES, 0) * 1000)
    return profit - penalty


def get_neighbor(current_solution):
    neighbor = current_solution.copy()
    index = np.random.randint(0, len(neighbor))
    change = np.random.choice([-STEPSIZE, STEPSIZE])
    # Ensure non-negative production
    neighbor[index] = max(0, neighbor[index] + change)
    return neighbor


def hill_climbing():
    current_solution = np.random.randint(0, 100, size=len(PROFIT_PER_PACKET))
    current_profit = calculate_profit(current_solution)

    for _ in range(MAX_ITERATIONS):
        neighbor = get_neighbor(current_solution)
        neighbor_profit = calculate_profit(neighbor)

        if neighbor_profit > current_profit:
            current_solution, current_profit = neighbor, neighbor_profit

    return current_solution, current_profit


best_solution, best_profit = hill_climbing()

print("Best Solution:", best_solution)
print("Best Profit:", best_profit)
