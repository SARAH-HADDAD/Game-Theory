import numpy as np



matrix = np.array([
    [[2, 1], [0, 0]],
    [[0,0], [1, 2]]
])

indice1 = []
for i in range(len(matrix)):

    indice = np.argmax(matrix[i][:, 0])
    indice1.append([i, indice])



indices2 = []

for j in range(matrix.shape[2]):

    indice2 = np.argmax(matrix[:, :, 1][:, j])
    indices2.append([indice2, j])


print("Matrice:")
for row in matrix:
    print("+-----------+-----------+")
    for payoff in row:
        print(f"| {payoff[0]:>3}, {payoff[1]:>4} ", end="")
    print("|")
print("+-----------+-----------+")

nash_equilibre = [index for index in indice1 if index in indices2]
print("\n\n\n")
print("Équilibres de Nash pur :", nash_equilibre)
print("\n\n\n")

for equilibrium in nash_equilibre:
    player1_strategy = equilibrium[0]
    player2_strategy = equilibrium[1]
    value = matrix[player1_strategy][player2_strategy]
    print(f"Équilibre de Nash pur : Joueur 1 choisit la stratégie {player1_strategy}, Joueur 2 choisit la stratégie {player2_strategy}, Valeur : {value}")