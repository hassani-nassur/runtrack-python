def changeValeur(list =["nassur","hassani","mouigni"]):
    if(len(list)==1):
        txt = "Ta liste ne contient qu'une valeur : "+list[0]
        return txt
    elif(len(list)==0):
        return "il ya rien n'a inverser la list est vide"
    else:
        a = list[0]
        list[0] = list[-1]
        list[-1] = a
        return list
    
print(changeValeur())
print(changeValeur([]))
print(changeValeur(["said"]))