def additionner(a, b):
    return a + b


print(additionner(1, 2))


def calculer_somme(nombres):
    resultat = 0
    for nombre in nombres:
        resultat += nombre
    return resultat


liste_de_nombres = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(calculer_somme(liste_de_nombres))
