def len(list):
    compt=0
    for i in list:
        compt +=1
    return compt
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


list=[10,20,30,20,10,50,60,40,80,50,40]

def elimineDoublons(list):
    i =0
    trie(list)
    n = len(list)
    if n >= 2:
        while i < n:
            if(list[i] == list[i-1]):
                list = list[0:i] + list[i+1:len(list)]
                n -=1
            else:
                i+=1
    return list

print(elimineDoublons(list))
        