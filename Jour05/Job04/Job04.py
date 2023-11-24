def diago(n):
    debut = "|"
    fin = "|"
    contain ="#"
    l = []
    l.append(debut)
    for i in range(n):
        l.append(contain)
    l.append(fin)

    for j in range(1,n+1):
        a = l[j]
        l[j]=" "
        print(' '.join(l))
        l[j]= a
        
    

diago(6)