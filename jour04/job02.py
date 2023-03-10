def AfficheFruits(index):
    list =["pomme","cerise","orange"]
    
    if(index >= len(list) or index < 0):
        text = "l'element d'index {} n'existe pas dans la liste"
        return text.format(index)
    else: 
        return list[index]
    
print(AfficheFruits(-1))