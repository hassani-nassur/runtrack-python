def longeur(list):
    compt =0    
    for i in list:
        compt += 1
    return compt

def decoupage(chaine):
    txt=''
    table=[]
    for i in chaine:
        if i == ' ':
            table += [txt]
            txt =''
        else :
            txt +=i
    table += [txt]
    return table 
        
# pour tester rapidement je donnée un chaine par defaut à ma methode 
def my_long_word(nombre = 2, chaine = "je suis nassur hassani"):
    chaienList= decoupage(chaine)
    list = []
    txt =""
    for i in chaienList:
        compt = longeur(i)
        if( compt > nombre ):
            list +=[i]
    for i in list:
        txt += i + " "
    return txt
    
print(my_long_word())
# print(decoupage("je suis nassur hassani"))