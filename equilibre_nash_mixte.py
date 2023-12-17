import numpy as np

matrix = np.array([
    [[2, 1], [0, 0]],
    [[0, 0], [1, 2]]
])

def calculate_mixed_strategy(player, opponent):
    num_strategies = matrix.shape[2]
    probabilities = np.zeros(num_strategies)

    for i in range(num_strategies):
        numerator = max(matrix[player, :, opponent])
        denominator = sum([max(matrix[k, :, opponent]) for k in range(num_strategies)])

        if denominator != 0:
            probabilities[i] = numerator / denominator

    return probabilities

equilibria = []

for i in range(len(matrix)):
    for j in range(matrix.shape[2]):
        mixed_strategy_player_1 = calculate_mixed_strategy(i, j)
        mixed_strategy_player_2 = calculate_mixed_strategy(j, i)

        value = matrix[i, j]

        equilibria.append((i, j, mixed_strategy_player_1, mixed_strategy_player_2, value))

print("equilibres de Nash mixtes :")
for equilibrium in equilibria:
    player1_strategy = equilibrium[0]
    player2_strategy = equilibrium[1]
    
    print(f"equilibre de Nash mixte : Joueur 1 choisit la strategie {player1_strategy}, Probabilites : {np.round(equilibrium[2], 3)}, Joueur 2 choisit la strategie {player2_strategy}, Probabilites : {np.round(equilibrium[3], 3)}, Valeur : {equilibrium[4]}")
