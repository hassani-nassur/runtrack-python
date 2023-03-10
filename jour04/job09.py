def min_maxElement(list =[8,24,27,48,2,16,9,102,7,84,91]):
    
    list.sort()
    min_max = [list[0],list[-1]]
    return min_max

min_max = min_maxElement()
print(min_max)
print("le minimum du tableau est : ",min_max[0])
print("le maximum du tableau est : ",min_max[1])