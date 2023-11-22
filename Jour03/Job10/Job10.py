def pair_impair(nombre):
    if nombre > 0 and nombre == int(nombre):
        
        if nombre % 2 == 0:
            print("Nombre Pair")

        else : 
            print("Nombre impair")
    else:
        print("Nombre négatif ou nombre à virgule, entrer un nombre positif/entier :) .")

    
    
pair_impair(5)

print("---------------------")

pair_impair(2.3)

print("---------------------")

pair_impair(-5)

print("---------------------")

pair_impair(4)