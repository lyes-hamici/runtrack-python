def cal_somme_pair(L):
    x = 0
    for i in range(len(L)):
        if L[i] % 2 == 0:
            x += L[i]
    print(x)

cal_somme_pair([8, 24, 27, 48, 2,16, 9, 7, 84, 91])