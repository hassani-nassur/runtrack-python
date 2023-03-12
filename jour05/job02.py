def rectangle(largeur,hauteur):
    
    for i in range(0,hauteur):
        if(i == 0 or i == hauteur - 1):
            print("|"+(largeur-1)*"-"+"|")
        else:
            print("|"+(largeur-1)*" "+"|")

rectangle(10,5)