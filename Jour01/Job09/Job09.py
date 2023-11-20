nom = "Crocs Cars"
prix_unitaire = 103 #Prix en € du produit

quantité_en_stock = 0 #Nombres d'exemplaire du produit

demande = input("Nombre de produit à commander :") #Nombre de produit demander à l'achat

print("----------------------------")

print("Article :",nom)

print("----------------------------")

print("Prix :",prix_unitaire,"€")

print("----------------------------")

print("Quantité en stock :",quantité_en_stock)

print("----------------------------")



quantité_en_stock += 15 #mise à jour du stock

print("Ajout de stock :",quantité_en_stock)

print("----------------------------")

print("Nombre de produit à commander :",demande)

print("----------------------------")

print("Stock :",int(quantité_en_stock) - int(demande)) #mise à jour du stock

print("----------------------------")

quantité_en_stock -= int(demande)

prix_unitaire += 10/100 #Ajout de 10% à la valeur

print("Dommage, l'inflation est passée par là, le nouveau prix est de :",prix_unitaire,"€")

print("----------------------------")

print("Article :",nom)

print("----------------------------")

print("Prix :",prix_unitaire,"€")

print("----------------------------")

print("Quantité en stock après commande :",quantité_en_stock)

print("----------------------------")

print("Prix total de la commande :",float(prix_unitaire) * float(demande),"€")

print("----------------------------")


