import numpy as np

def is_dominated(a, b):
    """Check if vector 'a' is dominated by vector 'b'."""
    return (a[0] < b[1] and a[1] <= b[1]) or (a[0] <= b[0] and a[1] < b[1])

def find_pareto_optimal(matrix):
    """Find Pareto optimal points in a given matrix."""
    flatmat = matrix.reshape(-1, matrix.shape[-1])
    length = flatmat.shape[0]
    is_dominated_by_others = np.full(length, True)

    for i in range(length):
        for j in range(length):
            if i != j and is_dominated(flatmat[i], flatmat[j]):
                is_dominated_by_others[i] = False
                break

    pareto_optimal_points = flatmat[is_dominated_by_others]
    return pareto_optimal_points


matrix = np.array([[[2, 1], [0, 0]], 
                [[0, 0], [1, 2]]])

pareto_optimal_points = find_pareto_optimal(matrix)
print(pareto_optimal_points)
