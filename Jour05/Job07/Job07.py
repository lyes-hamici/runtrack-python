import random 
l = []

for i in range(10):
    l.append(random.randint(0,100))

def note(l):
    

    l2 = []
    for i in l:
        if  i >= 40 and 100 > i and i%5==0 and i < i+3 :
            l2 += [int(i+2)]

        elif i < 40:
            l2.append("Echec du test")


        elif i >= 40:
            l2.append("Test réussi")


    print("Anciennes liste de notes :",l,"Nouvelles liste de notes",l2)

        


note(l)

        