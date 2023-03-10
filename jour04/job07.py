def comptMultileTrois(L=[8,24,48,2,16]):
    compt =0
    for i in L:
        if(i%3 == 0 ):
            compt +=1
    
    txt = "cette list à {} mulitple de 3"
    return txt.format(compt)

print(comptMultileTrois())