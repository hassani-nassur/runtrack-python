def insertFruit(fruit,list = ["pomme",'cerise',"orange","melon"]):
    
    list.insert(2,fruit)
    
    return list

print(insertFruit("mangue"))