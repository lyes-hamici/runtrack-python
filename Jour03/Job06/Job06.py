def nombre(nombre):
    if int(nombre) < 0:
        print("negatif")

    if int(nombre) > 0:
        print("positif")
    
    if int(nombre) == 0 :
        print("Chossir un un autres nombres que 0.")


print("---------------------")

nombre("-5")

print("---------------------")

nombre("5")

print("---------------------")

nombre("0")

print("---------------------")

def nombre2(nombre):
    if int(nombre) < 0:
        return "negatif"

    if int(nombre) > 0:
        return "positif"
    
    if int(nombre) == 0 :
        return "Chossir un un autres nombres que 0."


print("---------------------")

print(nombre2("-5"))

print("---------------------")

print(nombre2("5"))

print("---------------------")

print(nombre2("0"))

print("---------------------")