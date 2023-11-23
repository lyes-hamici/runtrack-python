def my_long_word(a,L):
    nouvelle_liste = ""
    for x in range(Trouve_taille(L)):
        if L[x] >= a:
            nouvelle_liste += str(L[x])

    return nouvelle_liste



def Trouve_taille(l):
    j = 0
    for i in l:
        j+=1
    return j

print("len de la liste :",Trouve_taille('La peur est le chemin vers le côté obscur, la peur mène à la colère, la colère mène à la haine, la haine mène à la souffrance'))


print(my_long_word(3,'La peur est le chemin vers le côté obscur, la peur mène à la colère, la colère mène à la haine, la haine mène à la souffrance'))