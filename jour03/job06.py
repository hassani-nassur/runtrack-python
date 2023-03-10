def piramide(chaine,ligne):
    
    i = 0
    
    for x in range(ligne):
        stock =""
        for y in range(i, i+x):
            while i >= len(chaine):
                i -= len(chaine)
            stock +=chaine[y]
            i +=1
        print(stock)
               


piramide("abcdefghijklmnopqrstuvwxyz",14)
            