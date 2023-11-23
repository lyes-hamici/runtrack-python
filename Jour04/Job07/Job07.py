def multiple_de_tois(L):
    for i in range(len(L)):
        if L[i] % 3 == 0:
            print("index dans la liste :",i,", élement dans la liste",L[i])

multiple_de_tois([8,24,48,2,16])