def doublon(L):
    L2 = []
    for i in L:
        if i not in L2:
            L2.append(i)
    return L2
    




print(doublon([10,20,30,20,10,50,60,40,80,50,40]))
