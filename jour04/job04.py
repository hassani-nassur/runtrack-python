# je donnée une liste en argument par defaut pour faciliter les testes
def insertFruit(fruit,list = ["pomme",'cerise',"orange","melon"]):
    
    list.insert(2,fruit)
    
    return list

print(insertFruit("mangue"))