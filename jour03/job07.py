def recopieInverse(chaine):
    
    i = len(chaine) - 1
    
    copy =""
    
    # for i in range(i,-1,-1):
    
    while i >= 0:
        copy = copy+chaine[i]
        i -= 1
    
    return copy

nom = recopieInverse("abdoulhamid")

print(nom)
    