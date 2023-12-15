import numpy as np

def is_pareto_optimal(matrix, strategy_profile):
    # Check if there is no other strategy profile that makes at least one player better off
    for other_profile in np.ndindex(matrix.shape[:-1]):
        if all(matrix[strategy_profile] >= matrix[other_profile]) and any(matrix[strategy_profile] > matrix[other_profile]):
            return False
    return True

def find_pareto_optimal_strategies(matrix):
    pareto_optimal_strategies = []

    # Iterate through all possible strategy profiles
    for profile in np.ndindex(matrix.shape[:-1]):
        if is_pareto_optimal(matrix, profile):
            pareto_optimal_strategies.append(profile)

    return pareto_optimal_strategies

# Example with a 2x2x2 matrix for two players
matrix_2_players = np.array([[[2, 1], [0, 0]], 
                             [[0, 0], [1, 2]]])

pareto_optimal_strategies = find_pareto_optimal_strategies(matrix_2_players)

# Print Pareto optimal strategies
for profile in pareto_optimal_strategies:
    print(f"Pareto Optimal Strategy: {profile}, Values: {matrix_2_players[profile]}")
