investissement_initia = 0

taux = 0

print("----------------------")


print("rendement annuel :",taux/100*investissement_initia,"€") # Rendement annuel

print("----------------------")

investissement_initia += 5000

taux += 2


print("rendement annuel :",taux/100*investissement_initia,"€") # Nouveau rendement annuel

print("----------------------")


investissement_initia -= investissement_initia *10/100 # 10% en moins sur l'investissement_initia

taux -= 1 # 1% en moins sur le rendement


print("rendement annuel :",taux/100*investissement_initia,"€") # Nouveau rendement annuel 

print("----------------------")