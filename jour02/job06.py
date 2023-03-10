def afficheSigneNombre(nombre):
    if(nombre > 0):
        print(nombre," Est positif")
    elif(nombre < 0):
        print(nombre," Est negatif")
    else:
        print("Votre nombre vos zero")
        
afficheSigneNombre(20)
afficheSigneNombre(-12)
afficheSigneNombre(0)