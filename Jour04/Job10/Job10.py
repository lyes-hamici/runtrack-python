def produit(L):
    x = 1
    for i in range(len(L)):
        if 25 <= L[i] <= 90:
            x *= L[i]
    return x

print(produit([8, 24, 27, 48, 2,16, 9, 102, 7, 84, 91]))
