def Job8(type,saison):

    if type == "fruits" and saison == "hiver":
        return "orange, mandarine et kiwi"
    
    elif type == "fruits" and saison == "ete":
        return "Poire, fraise, cassis"
    
    elif type == "legume" and saison == "hiver":
        return "carotte, topinambour, endive"
    

    elif type == "legume" and saison == "ete":
        return "artichaut, aubergine,navet"
    

print("---------------------")

print(Job8("fruits","hiver"))

print("---------------------")

print(Job8("fruits","ete"))

print("---------------------")

print(Job8("legume","hiver"))

print("---------------------")

print(Job8("legume","ete"))

print("---------------------")