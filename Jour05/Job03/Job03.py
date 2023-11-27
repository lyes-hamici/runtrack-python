n=int(input("saisir l'hauteur du triangle:"))

def triangle(n):
    for i in range(n):
        vide = ' ' * (n - i - 1)
        if i == 0:
            print(vide + '/\\')

        elif i == (n-1):
            print(vide + '/' + '_' * (2 * i) + '\\')

        else:
            print(vide + '/' + ' ' * (2 * i) + '\\')
    







triangle(n)

    
    