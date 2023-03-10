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

def arrondi(list = [22.4, 4.0, 16.22, 9.10, 11.60, 12.22, 14.20, 5.20, 17.50]):
    for index,value in enumerate(list):
        txt =""
        chiffreConvertie = str(value)
        apresVirgule = ""
        indice = 0
        
        for key,val in enumerate(chiffreConvertie):
            # print(val)
            if val =='.':
                indice = key
                continue
            
            if indice == 0:
                if(apresVirgule !=""):
                    continue
                txt +=str(val)
            
            if indice + 1 == key:
                apresVirgule = ""
                apresVirgule += val
                # print(val)
            indice=0
        if(int(apresVirgule) >= 5 ):
            txt = int(txt)
            list[index] = txt + 1
        else:
            txt = int(txt)
            list[index] = txt
    
    return trie(list)

print(arrondi())