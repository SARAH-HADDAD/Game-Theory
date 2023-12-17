import numpy as np

def support(strategies, probabilities):


    #  le support de l’ensemble des probabilités 
    #  représente l’ensemble des stratégies du joueur i ayant une probabilité non nulle.

    supports = {}
    supports_zero = {}

    for player, probabilities in probabilities.items():
        supports[player] = [i for i, prob in enumerate(probabilities) if prob > 0]
        supports_zero[player] = [i for i, prob in enumerate(probabilities) if prob == 0]
        print(f"Probabilités du joueur {player} :", probabilities)
        print(f"Support du joueur {player} :", supports[player], "\n")

    return supports, supports_zero

def paiement_strategies(strategies, probabilities):
    # représente le gain qu’aura le joueur i s’il jouera une de ses stratégie selon ce que jouera l’autre joueurs 
    #  (ou les autres joueurs si nous avons plus de 2 joueurs).
    strategy_payoffs_dic = {}

    for player, player_strategies in strategies.items():
        opponent_probabilities = probabilities[3 - player]  

        strategy_payoffs = [sum(p1 * p2 for p1, p2 in zip(strategy, opponent_probabilities)) for strategy in player_strategies]

        strategy_payoffs_dic[player] = strategy_payoffs

        print(f"Paiements des stratégies du joueur {player} :", strategy_payoffs)

    return strategy_payoffs_dic

def paiement_joueur(probabilities, strategy_payoffs_dic):
    # Appelée paiement joueur également, elle représente le gain d’un joueur 
    # en fonction des ensembles des probabilités et la matrice des gains. 
    result = {}

    for player, probabilities in probabilities.items():
        result[player] = sum(p * strategy_payoffs_dic[player][i] for i, p in enumerate(probabilities))

    print("")
    print("Paiement du joueur 1 :", result[1])
    print("Paiement du joueur 2 :", result[2])

    return result

def IndifferenceSupport(supports, supports_zero, dic_strategy_payoffs, fct_utility):
    for player, strategies in dic_strategy_payoffs.items():
        support_values = [strategies[i] for i in supports[player]]
        zero_support_values = [strategies[i] for i in supports_zero[player]]

        if not all(value == support_values[0] for value in support_values) or strategies[1] != fct_utility[player]:
            print(f"Les paiements des stratégies du joueur {player} ne sont pas égaux.")
            return False

        if not all(value == zero_support_values[0] for value in zero_support_values) or strategies[1] > fct_utility[player]:
            print(f"Les paiements des stratégies du joueur {player} pour le non-support ne sont pas égaux.")
            return False

    print("\nCe jeu admet un équilibre de Nash mixte.")
    return True

def enumerate_support(num_strategies):
    supports = []

    for prob_player1 in range(num_strategies[0] + 1):
        prob_player2 = 1 - prob_player1
        supports.append({
            1: [1 if i == prob_player1 else 0 for i in range(num_strategies[0])],
            2: [1 if i == prob_player2 else 0 for i in range(num_strategies[1])]
        })

    return supports

def print_matrix(strategies):
    for player, matrix in strategies.items():
        print(f"Matrice des gains du joueur {player}:")
        for row in matrix:
            print(row)
        print("\n")



# La matrice des gains correspondant à ce joueur est la suivantes :
strategies = {
    1: np.array([[4, 5, 6], [2, 8, 3], [3, 9, 2]]),
    2: np.array([[3, 1, 0], [1, 4, 6], [2, 6, 5]]),
}

probabilities = {
    1: np.array([1/3, 1/3, 1/3]),
    2: np.array([0, 1/2, 1/2]),
}

print("\n\n\n")
print_matrix(strategies)
supports, supports_zero = support(strategies, probabilities)
dic_strategy_payoffs = paiement_strategies(strategies, probabilities)
fct_utiliter = paiement_joueur(probabilities, dic_strategy_payoffs)
val = IndifferenceSupport(supports, supports_zero, dic_strategy_payoffs, fct_utiliter)
