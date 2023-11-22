def moyenne():
    note_final = 0
    a = input("Entrée vôtre première note :")
    b = input("Entrée vôtre deuxième note :")
    c = input("Entrée vôtre troisième note :")

    note_final = int(a) + int(b) + int(c)
    print("Note total :",note_final)

    moyenne_final = note_final / 3

    print("Moyenne :",moyenne_final)


    if 15 < moyenne_final <= 20:
        print("Très bon élève")

    elif 11 < moyenne_final <= 14:
        print("Bonne éléve")


    elif 8 < moyenne_final <= 10:
        print("Élève moyen")


    elif 0 < moyenne_final <= 7:
        print("Élève devant faire des efforts")

moyenne()

    