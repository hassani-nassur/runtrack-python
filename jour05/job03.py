def dieze(n):
    j = 1
    for i in range(0,n+2):
        if( i == 0 or i == n+1):
            print("+"+n*"-"+"+")
            # print()
        else:
            txt = "|"+n*"#"+"|"
            txt = list(txt)
            long = len(txt)
            txt[long - j] = " "
            txt = ''.join(txt)
            print(txt)
            # print()
        j += 1
            
dieze(10)


