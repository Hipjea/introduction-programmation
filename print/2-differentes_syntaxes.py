salutation = "Bonjour"
nom = "utilisateur"

# 1. séparation des paramètres avec des virgules :
print(salutation, ",", nom)

# 2. concaténation des paramètres par l'opérateur + :
print(salutation + ", " + nom)

# 3. utilisation d'un placeholder en fonction du type de données :
print("%s%s %s" % (salutation, ",", nom))

# 4. utilisation d'un placeholder anonyme :
print("{}{} {}".format(salutation, ",", nom))

# 5. utilisation d'un placeholder nommé :
print("{salut}{virgule} {nom}".format(salut=salutation, virgule=",", nom=nom))
