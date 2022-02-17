ensoleille = True
neige = True

if ensoleille:
    print("on va à la plage")
elif neige:
    print("on fait un bonhomme de neige")
else:
    print("on reste à la maison")


avec_soleil = True
en_semaine = False

if avec_soleil and not en_semaine:
    print("on va à la plage")
elif avec_soleil and en_semaine:
    print("on va au boulot")
else:
    print("on reste à la maison")


nombre_de_sieges = 30
nombre_invites = 25

if nombre_invites < nombre_de_sieges:
    print("d'autres invités peuvent entrés")
else:
    print("ha désolé il n'y a plus de place")
