valeur_maximale = 20

for number in range(0, valeur_maximale):
    if number % 2 == 0:
        print(number, "% 2 =", number % 2, ": pair")
    else:
        print(number, "% 2 =", number % 2, ": impair")
