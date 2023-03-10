def elimineDoublon(list=[10,20,30,20,10,50,60,40,80,50,40]):
    copy = list
    taille = 0
    for i in list:
        taille += 1
        
    for i in range(1,taille):
        
        value = list[i]
        j = i - 1
        while(j>=0 and value == list[j]):
            if(copy[i]):
                copy.pop(i)
            j -=1
        copy.pop(j+1)   
        # for i in list:
        #     taille += 1
    
    return copy

print(elimineDoublon())             