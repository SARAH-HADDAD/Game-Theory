import numpy as np

def trouver_strategies_dominees_joueur1(matrix):
    nombre_de_lignes, _, _ = matrix.shape
    strategies_dominees_joueur1 = []

    for i in range(nombre_de_lignes):
        ligne1 = matrix[i]
        premier_element_ligne1 = ligne1[:, 0]
        est_strategie_dominee = True 

        for j in range(nombre_de_lignes):
            if i != j:
                ligne2 = matrix[j]
                premier_element_ligne2 = ligne2[:, 0]

                if all(premier_element_ligne1 <= premier_element_ligne2):
                    est_strategie_dominee = False

        if est_strategie_dominee:
            strategies_dominees_joueur1.append(ligne1)

    return strategies_dominees_joueur1

def trouver_strategies_dominees_joueur2(matrix):
    _, nombre_de_colonnes, _ = matrix.shape
    strategies_dominees_joueur2 = []

    for i in range(nombre_de_colonnes):
        colonne1 = matrix[:, i]
        premier_element_colonne1 = colonne1[:, 1]
        est_strategie_dominee = True

        for j in range(nombre_de_colonnes):
            if i != j:
                colonne2 = matrix[:, j]
                premier_element_colonne2 = colonne2[:, 1]

                if all(premier_element_colonne1 <= premier_element_colonne2):
                    est_strategie_dominee = False

        if est_strategie_dominee:
            strategies_dominees_joueur2.append(colonne1)

    return strategies_dominees_joueur2

def main():
    matrix = np.array([
        [(0, 0), (75, -25)],
        [(-25, 75), (50, 50)]
    ])
    print("Matrice:")
    for row in matrix:
        print("+-----------+-----------+")
        for payoff in row:
            print(f"| {payoff[0]:>3}, {payoff[1]:>4} ", end="")
        print("|")
    print("+-----------+-----------+")

    choix = input("Choisissez 1 ou 2 : ")

    if choix == "1":
        strategies_dominees_joueur1 = trouver_strategies_dominees_joueur1(matrix)
        if not strategies_dominees_joueur1:
            print("Ce joueur n'a pas de stratégie dominée.")
        else:
            print("Stratégie dominée pour joueur 1 : " + str(strategies_dominees_joueur1))
    elif choix == "2":
        strategies_dominees_joueur2 = trouver_strategies_dominees_joueur2(matrix)
        if not strategies_dominees_joueur2:
            print("Ce joueur n'a pas de stratégie dominée.")
        else:
            print("Stratégie dominée pour joueur 2 : " + str(strategies_dominees_joueur2))
    else:
        print("Choix invalide. Veuillez choisir 1 ou 2.")

if __name__ == "__main__":
    main()
