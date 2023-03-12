def arrondisementNote(list = [12,62,45,60,67,52,91,73,60]):
    
    for i in range(0,len(list)):
        if (list[i] >= 40 and list[i] < 100):
            for J in range(1,3):
                if( (list[i] + J) % 5 == 0):
                    list[i] = list[i]+J
    
    return list

print(arrondisementNote())
# arrondisementNote()