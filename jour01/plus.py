print("Verification de l'existance du caractere : e dans une chaine ")
ma_string = input("\nEntrez une chaine : ")
ma_string.find("e")
if(ma_string.find("e") < 0):
    print("\nle caractere : \"e\" n\'existe pas dans ta chaine. \n")
else:
    print("le caracter \"e\" est conenue dans ta chaine. \n")