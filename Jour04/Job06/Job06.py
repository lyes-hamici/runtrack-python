L = []
L.append(1)
L.append(2)
L.append(3)
L.append(4)
L.append(5)

print("Liste :",L)


def échange():
    a = L[0]
    b = L[-1]
    L[-1] = a
    L[0] = b
    return L

print("Nouvelle liste :",échange())