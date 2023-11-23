L = []
L.append(1)
L.append(2)
L.append(3)
L.append(4)
L.append(5)

print("Liste :",L)


print("Deuxième valeurs de la liste :",L[1])

def somme_liste():
    L[3] = L[2] + L[4]
    return L

print("Nouvelle liste :",somme_liste())



print("Dernière élément de la liste :",L[-1])