L = [1,2,3,4,5,6]

print(L[1])
# je donnée une liste en argument par defaut pour faciliter les testes

def replace(L=L):
    if(len(L)<5):
        return"la liste est courte"
    else:
        L[3]=L[2]+L[4]
        return L

print(replace())
print(L[-1])