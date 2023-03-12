def chiffrage(mot = " je suis nassur"):
    
    ref = "abcdefghijklmnopqrstuvwxyz"
    mot = mot.lower()
    longeurMot = len(mot)
    longeurRef = len(ref)
    
    for i in range(0,longeurMot):
        c = False
        for j in range(0,longeurRef):
            if( mot[i] == ref[j]):
                c = j
                while( c + 3 >= longeurRef):
                    c = j - longeurRef
            
        if (c != False):    
            mot = list(mot)
            mot[i] = ref[c+3]
            mot = "".join(mot)
       
    return mot
print(chiffrage())
