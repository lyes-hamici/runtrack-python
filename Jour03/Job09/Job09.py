a = input("Entrée vôtre première note :")
b = input("Entrée vôtre deuxième note :")
c = input("Entrée vôtre troisième note :")

def moyenne(a,b,c):
    moyenne_etudiant = int(a) + int(b) + int(c)

    moyenne_etudiant = moyenne_etudiant / 3

    print("Moyenne :",moyenne_etudiant)


    if 15 <= moyenne_etudiant <= 20:
        print("Très bon élève")

    elif 11 <= moyenne_etudiant <= 14:
        print("Bonne éléve")


    elif 8 <= moyenne_etudiant <= 10:
        print("Élève moyen")


    elif 0 < moyenne_etudiant <= 7:
        print("Élève devant faire des efforts")

moyenne(a,b,c)



    