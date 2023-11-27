def my_sort(t):
    a=0
    b=0
    for i in range(1,len(t)):
        a +=1
        x = t[i] # mémoriser T[i] dans x
        j = i
        while j > 0 and t[j - 1] > x :
            t[j] = t[j-1] 
            j = j - 1 
            b+=1
        t[j] = x # placer x dans le "trou" laissé par le décalage


    print("Liste trié :",t,"Nombre de coup total :",a+b)


print("---------------------------------------------------------------")

my_sort([7, 11, 42, 39, 2])

print("---------------------------------------------------------------")

my_sort([7, 11, 42, 39, 2,15,40,32,85,4,1])