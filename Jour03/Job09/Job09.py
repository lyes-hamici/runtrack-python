a = input("Entrée vôtre première note :")
b = input("Entrée vôtre deuxième note :")
c = input("Entrée vôtre troisième note :")

def moyenne(a,b,c):
    moyenne = float(a) + float(b) + float(c)
    moyenne = moyenne / 3
    print("Moyenne :",moyenne)
    return moyenne



moyenne(a,b,c)


moyenne_etudiant = moyenne(a,b,c)

if 15 <= moyenne_etudiant <= 20:
    print("Très bon élève")

elif 11 <= moyenne_etudiant < 15:
    print("Bonne éléve")


elif 8 <= moyenne_etudiant < 11:
    print("Élève moyen")


elif 0 < moyenne_etudiant <= 7:
    print("Élève devant faire des efforts")





    