# def calcule(num1,operateur,num2):
#     if(operateur == "+"):
#         return num1+num2
#     elif(operateur == "-"):
#         return num1-num2
#     elif(operateur == "%"):
#         return num1 % num2
#     elif(operateur == "/"):
#         return num1/num2
#     else:
#         return"votre operateur m'ai inconue"
    
# print("12 % 12 = ",calcule(12,"%",12))

# print("12 + 12 = ",calcule(12,"+",12))

# print("12 - 12 = ",calcule(12,"-",12))

# print("12 / 12 = ",calcule(12,"/",12))


def calcule(num1,operateur,num2):
    
    if( operateur in "-*+/%"):
        return eval(str(num1)+ operateur+str(num2))
    else:
        return "Votre operateur m'ai inconnue"

print(calcule(12,"+",3))