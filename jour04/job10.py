def produits(list = [8,24,27,48,2,16,9,102,7,84,91]):
    produit = 1
    for i in list :
        if( i >=25 and i <= 90):
            produit *=i
    
    return produit

print(produits())