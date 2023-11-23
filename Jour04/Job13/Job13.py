def Trouve_taille(l):
    j = 0
    for i in l:
        j+=1
    return j

def doublon(L):
    L2 = []
    for i in range(Trouve_taille(L)):
        if i not in L2:
            L2 += L[i]
    return L2
    
    x = L2 + L




print(doublon([10,20,30,20,10,50,60,40,80,50,40]))
