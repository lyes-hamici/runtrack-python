def my_long_world(longeur, phrase):
    i = 0
    longeur = 0
    index = 0
    list = []
    new_phrase = ""
    for letter in phrase:
        longeur += 1
    while i < longeur:
        if phrase[i] == " ":
            list += [phrase[index:i]]
            index = i+1
        i +=1
    for mot in list:
        longeur = 0
        for letter in mot:
            longeur += 1 
        if longeur > 3 :
            new_phrase += mot + " "
    print(new_phrase)
    

phrase = "La peur est le chemin vers le côté obscur, la peur mène à la colère, la colère mène à la haine, la haine mène à la souffrance "

print("-------------------------------------------------")

my_long_world(3,phrase)

print("-------------------------------------------------")







