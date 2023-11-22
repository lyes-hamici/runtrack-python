def pair_impair(nombre):
    if int(nombre) > 0:
        if int(nombre) % 2 == 0:
            print("Nombre Pair")

        else : 
            print("Nombre impair")
    else:
        print("Nombre négatif , entrer un nombre positif :) .")
    
    
pair_impair(5)



pair_impair(-5)


pair_impair(4)