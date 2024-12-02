def aliments(type,saison):
    if (type == "fruits" and saison=="hiver") :
        print("orange, mandarine et kiwi")
    elif (type == "fruits" and saison=="été") :
        print("Poire, fraise, cassis")
    elif (type == "légumes" and saison=="hiver") :
        print("carotte, topinambour, endive")
    else :
        print("artichaut, aubergine,navet")
aliments("fruits","hiver")
aliments("fruits","été")
aliments("légumes","hiver")
aliments("légumes","été")