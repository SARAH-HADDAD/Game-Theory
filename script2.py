import numpy as np

def trouver_optimum_pareto(matrix):
    _, num_strategies, _ = matrix.shape
    pareto_optimal_strategies = []

    for i in range(num_strategies):
        for j in range(num_strategies):
            # Vérifier si (i, j) est un optimum de Pareto
            if (matrix[:, i, :] <= matrix[:, j, :]).all():
                continue  # Continue to the next iteration if Pareto Optimal
        else:
            pareto_optimal_strategies.append(tuple(matrix[:, i, :]))

    return pareto_optimal_strategies

# Exemple d'utilisation
matrix = np.array([
    [(0, 0), (75, -25)],
    [(-25, 75), (50, 50)]
])

optimum_pareto = trouver_optimum_pareto(matrix)

if not optimum_pareto:
    print("Aucun optimum de Pareto trouvé.")
else:
    print(f"Points d'optimum de Pareto : {optimum_pareto}")
