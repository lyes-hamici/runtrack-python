def max(l):
    max = l[0]
    longueur=len(l)
    for i in range(longueur):
        if l[i] >= max:
            max = l[i]
    return max

def min(l):
    min = l[0]
    longueur=len(l)
    for i in range(longueur):
        if l[i] <= min:
            min = l[i]
    return min


print("Valeur minimale :",min([8, 24, 27, 48, 2,16, 9, 102, 7, 84, 91]))
print("Valeur maximale :",max([8, 24, 27, 48, 2,16, 9, 102, 7, 84, 91]))