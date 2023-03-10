def trie(list = [2,5,12,1,7]):
    taille = 0
    for i in list:
        taille +=1
    for i in range(1,taille):
        
        valeur = list[i]
        j = i-1
        while j >= 0 and valeur < list[j] :
            list[j+1] = list[j] 
            j -=1
        list[j+1] = valeur
    return list   

print(trie())
             