print("Boucle For :")

print("-----------------------------------------")


for i in range(101):

    if i%5 == 0 and i%3 == 0:
        print("FizzBuzz")


    elif i%3 == 0:
        print("Fizz")

    elif i%5 == 0:
        print("Buzz")


    else:
        print(i)



print("-----------------------------------------")




print("Boucle While :")

j = 0
while j <=100:

    if j%5 == 0 and j%3 == 0:
        print("FizzBuzz")
        j+=1


    elif j%3 == 0:
        print("Fizz")
        j+=1

    elif j%5 == 0:
        print("Buzz")
        j+=1


    else:
        print(j)
        j+=1

print("-----------------------------------------")