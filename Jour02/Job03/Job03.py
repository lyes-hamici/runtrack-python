print("Boucle For")

for i in range(101):
    if i == 26 or i == 37 or i == 88:
        continue
    else:
        print(i)


print("-------------------------------")

print("Boucle While")


j = 0
while j <= 100:
    if j == 26 or j == 37 or j == 88:
        j += 1
    else:
        print(j)
    j += 1