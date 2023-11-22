def moyenne():
    note_final = 0
    a = input("Entrée vôtre première note :")
    b = input("Entrée vôtre deuxième note :")
    c = input("Entrée vôtre troisième note :")

    note_final = int(a) + int(b) + int(c)
    print("Note total :",note_final)

    moyenne_final = note_final / 3

    print("Moyenne :",moyenne_final)


moyenne()

    