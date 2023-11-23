L = [7, 11, 42, 39, 2]

def list_plus_un(L):
    L2 = []
    for i in range(len(L)):
        L[i] = L[i] + 1
        L2.append(L[i])

    return L2


print(list_plus_un(L))