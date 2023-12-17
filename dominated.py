import numpy as np

def find_dominated_strategies_player1(matrix):
    num_rows, _, _ = matrix.shape
    dominated_strategies_player1 = []

    for i in range(num_rows):
        row1 = matrix[i]
        first_element_row1 = row1[:, 0]
        is_dominated_strategy = any(
            all(first_element_row1 <= row2[:, 0]) for j, row2 in enumerate(matrix) if i != j
        )

        if is_dominated_strategy:
            dominated_strategies_player1.append(row1)

    return dominated_strategies_player1

def find_dominated_strategies_player2(matrix):
    _, num_columns, _ = matrix.shape
    dominated_strategies_player2 = []

    for i in range(num_columns):
        col1 = matrix[:, i]
        first_element_col1 = col1[:, 1]
        is_dominated_strategy = any(
            all(first_element_col1 <= col2[:, 1]) for j, col2 in enumerate(matrix.T) if i != j
        )

        if is_dominated_strategy:
            dominated_strategies_player2.append(col1)

    return dominated_strategies_player2

def main():
    matrix = np.array([
        [(0, 0), (75, -25)],
        [(-25, 75), (50, 50)]
    ])

    print("Matrix:")
    for row in matrix:
        print("+-----------+-----------+")
        for payoff in row:
            print(f"| {payoff[0]:>3}, {payoff[1]:>4} ", end="")
        print("|")
    print("+-----------+-----------+")

    choice = input("Choose 1 or 2: ")

    if choice == "1":
        dominated_strategies_player1 = find_dominated_strategies_player1(matrix)
        print(
            "Dominated strategies for player 1: "
            + str(dominated_strategies_player1) if dominated_strategies_player1 else "This player has no dominated strategy."
        )
    elif choice == "2":
        dominated_strategies_player2 = find_dominated_strategies_player2(matrix)
        print(
            "Dominated strategies for player 2: "
            + str(dominated_strategies_player2) if dominated_strategies_player2 else "This player has no dominated strategy."
        )
    else:
        print("Invalid choice. Please choose 1 or 2.")

if __name__ == "__main__":
    main()
