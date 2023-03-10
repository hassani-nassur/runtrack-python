def AfficheNombrePremier():
    i=1
    while i < 1000:
        compte = 0
        for j in range(i,0,-1):
            if( i%j == 0):
                compte += 1
            
        if compte == 2 :
            print(i)
        i +=1
        
AfficheNombrePremier()   