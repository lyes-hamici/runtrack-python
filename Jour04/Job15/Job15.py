def Trouve_taille(l):
    j = 0
    for i in l:
        j+=1
    return j


def tri_à_bulles(liste):
    for i in range (Trouve_taille(liste)-1,1,-1):
        
        for j in range(i):
            if liste[j+1] < liste[j]:
                (liste[j+1], liste[j]) = (liste[j], liste[j+1])
    return liste




def arrondi(l):
    l2 = []
    for i in l:
        l2 += [int(i)]
    return tri_à_bulles(l2)

print(arrondi([22.4, 4.0, 16.22, 9.10, 11.00,12.22, 14.20, 5.20, 17.50]))        






