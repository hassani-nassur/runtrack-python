def fruitSeson(type,saison):
    type = type.lower()
    saison = saison.lower()
    if(type =="fruits" and saison == "hiver"):
        print("Orange, Mandarine et Kiwi")
    elif type =="fruit" and saison == "ete":
        print("Poire, fraise, Cassis")
    elif type == "legume" and saison == "hiver" :
        print("Carotte, Topinambour,endive")
    elif type == "legume" and saison == "ete":
        print("Artichaut, Aubergine, Navet")
    else:
        print("J\'ai rien à vous proposez")

fruitSeson("Fruits","hiver")
fruitSeson("fruit","ete")
fruitSeson("legume","ete")
fruitSeson("legume","hiver")