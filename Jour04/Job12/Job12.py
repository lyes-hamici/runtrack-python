




def tri_selection(t):
    n = len(t)
    for i in range(0,n-1):
        min = i
        for j in range(i+1,n):
            if t[j] < t[min]:
                min = j
            if min != i :
                t[i] , t[min] = t[min], t[i]
    return t

print(tri_selection([7, 11, 42, 39, 2]))

#Si la fonction "len" était utilisable l'on aurai pu faire :

'''
    def tri_insertion(t):
    for i in range(1,len(t)):
        x = t[i]
        j = i
        while j > 0 and t[j - 1] > x :
            t[j] = t[j-1]
            j = j - 1
        t[j] = x
    
    return t'''


'''def tri_à_bulles(liste):
    for i in range (len(liste)-1,1,-1):
        
        for j in range(i):
            if liste[j+1] < liste[j]:
                (liste[j+1], liste[j]) = (liste[j], liste[j+1])
    return liste'''