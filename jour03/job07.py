def recopieInverse(chaine):
    
    i = len(chaine) - 1
    
    copyInvers =""
    
    while i >= 0:
        copy = copy+chaine[i]
        i -= 1
    
    return copyInvers

nom = recopieInverse("abdoulhamid")

print(nom)
    