def pair_ou_impair(n):
    # Fonction qui retourne la chaîne "pair" ou "impair"
    # selon la valeur de la variable n
    if n % 2 == 0:
        return "pair"
    else:
        return "impair"


# Appel de la fonction pair_ou_impair() avec la valeur 1 comme paramètre
valeur1 = pair_ou_impair(1)
print(1, valeur1)

# Appel de la fonction pair_ou_impair() avec la valeur 2 comme paramètre
valeur2 = pair_ou_impair(2)
print(2, valeur2)


"""
Pour aller plus loin :

On peut optimiser la fonction en s'affranchissant de la clause "else" qui n'est pas nécessaire dans ce cas.
L'instruction "return" met fin à l'exécution de la fonction, on peut donc partir du principe que lorsqu'on
atteint return "pair", on sort de la fonction. Ce qui nous permet d'optimiser la fonction comme ceci :
"""


def pair_ou_impair(n):
    if n % 2 == 0:
        return "pair"
    return "impair"


"""
Le second return "impair" est implicitement la condition "else". On ne l'atteint que lorsque "n" est impair.
"""
