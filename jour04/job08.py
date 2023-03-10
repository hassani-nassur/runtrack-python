def calculeSommeNombrePaire(list = [8,24,27,48,2,16,8,7,84,91]):
    s = 0
    i = 0
    while i < len(list):
        if(list[i] % 2 == 0):
            s += list[i]
        i += 1
    return s

print(calculeSommeNombrePaire([3,2,12,5]))