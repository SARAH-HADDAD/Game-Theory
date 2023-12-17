import numpy as np

def pareto(matrix):
    num_points, num_criteria = matrix.shape[:2]
    is_dominated = np.zeros(num_points, dtype=bool)

    for i in range(num_points):
        for j in range(num_points):
            if i != j and np.all(matrix[i] < matrix[j] ):
                is_dominated[i] = True
                break

    pareto_result = matrix[~is_dominated]
    return pareto_result

matrix = np.array([[[1, -1], [-1, 1]], 
                   [[-1, 1], [1, -1]]])



print("Matrice:")
for row in matrix:
    print("+-----------+-----------+")
    for payoff in row:
        print(f"| {payoff[0]:>3}, {payoff[1]:>4} ", end="")
    print("|")
print("+-----------+-----------+")

pareto_result = pareto(matrix.reshape(-1, matrix.shape[-1]))

print("Pareto:")
print(pareto_result)
