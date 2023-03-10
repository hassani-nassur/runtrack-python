def chainePiramidale(chaine):
    i = 0
    nombreLigne = 1
    # let =''
    # for x in chaine:
    #     let = let +x
    #     i+=1
    #     print(let)
        
    # while i < len(chaine):
    #     print(chaine[:i])
        
    #     if i == len(chaine) - 1:
    #         print(chaine)
    #     i +=1
    
    while i + nombreLigne <= len(chaine):
        print(chaine[i: i+nombreLigne])
        i += nombreLigne
        nombreLigne += 1
            

chaine = "abcdefghijklmnopqrstuvwxyz"*10

chainePiramidale(chaine)