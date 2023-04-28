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
