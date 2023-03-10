def natureTriangle(a,b,c):
    a = float(a)
    b = float(b)
    c = float(c)
    
    if (a > 0 and b > 0 and c > 0):
        if(a == b and b == c):
            print("le tringle de cote a =",a,"; b=",b,"; c=",c," est un triangle equilaterale")
        elif ((a*a == b*b + c*c) or(b*b == a*a +c*c) or( c*c == a*a + b*b)):
            if a == b or a == c or b == c:
                print("le tringle de cote a =",a,"; b=",b,"; c=",c," est un triangle isorectangle")
            else:
                print("le tringle de cote a =",a,"; b=",b,"; c=",c," est un triangle rectangle")
        elif a == b or a == c or b == c:
            print("le tringle de cote a =",a,"; b=",b,"; c=",c," est un triangle isocel") 
        else:
            print("le tringle de cote a =",a,"; b=",b,"; c=",c," est un triangle quelconque")
    else:
        print("les cote a =",a,"; b=",b,"; c=",c," ne peuvent pas faire un triangle")


natureTriangle(5,3,4)
natureTriangle(2,2,2)
natureTriangle(6,7,7)
natureTriangle(0,1,2)
natureTriangle(-12,2,9)