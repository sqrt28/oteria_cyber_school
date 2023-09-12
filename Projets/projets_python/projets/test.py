def correcteur(l): #correcteur hamming
    b1 = l[0][0]
    b2 = l[0][1]
    b3 = l[0][2]
    b4 = l[0][3]
    p1 = l[0][4]
    p2 = l[0][5]
    p3 = l[0][6]
    b5 = l[0][7]
    b6 = l[0][8]
    b7 = l[0][9]
    b8 = l[0][10]
    p4 = l[0][11]
    p5 = l[0][12]
    p6 = l[0][13]

    if ( b1 + b2 + b4) % 2 == p1 and ( b1 + b3 + b4) % 2 == p2 and ( b2 + b3 + b4) % 2 == p3 and ( b5 + b6 + b8) % 2 == p4 and ( b5 + b7 + b8) % 2 == p5 and ( b6 + b7 + b8) % 2 == p6 :
         return[b1,b2,b3,b4,p1,p2,p3,b5,b6,b7,b8,p4,p5,p6]
    else:
        if p1 != ( b1 + b2 + b4) % 2 and p2 == ( b1 + b3 + b4) % 2 and p3 == ( b2 + b3 + b4) % 2:
            p1 = ( b1 + b2 + b4) % 2
        
        if p1 == ( b1 + b2 + b4) % 2 and p2 != ( b1 + b3 + b4) % 2 and p3 == ( b2 + b3 + b4) % 2:
            p2 = ( b1 + b3 + b4) % 2
        
        if p1 == ( b1 + b2 + b4) % 2 and p2 == ( b1 + b3 + b4) % 2 and p3 != ( b2 + b3 + b4) % 2:
            p3 = ( b2 + b3 + b4) % 2


        if p1 != ( b1 + b2 + b4) % 2 and p2 != ( b1 + b3 + b4) % 2 and p3 == ( b2 + b3 + b4) % 2:
             if b1 == 0:
                 b1 = 1
             else :
                b1 = 0
        if p1 != ( b1 + b2 + b4) % 2 and p2 == ( b1 + b3 + b4) % 2 and p3 != ( b2 + b3 + b4) % 2:
             if b2 == 0:
                 b2 = 1
             else :
                b2 = 0
        
        if p1 == ( b1 + b2 + b4) % 2 and p2 != ( b1 + b3 + b4) % 2 and p3 != ( b2 + b3 + b4) % 2:
             if b3 == 0:
                 b3 = 1
             else :
                b3 = 0
        
        if p1 != ( b1 + b2 + b4) % 2 and p2 != ( b1 + b3 + b4) % 2 and p3 != ( b2 + b3 + b4) % 2:
             if b4 == 0:
                 b4 = 1
             else :
                b4 = 0
        
        
        if p4 != ( b5 + b6 + b8) % 2 and p5 == ( b5 + b7 + b8) % 2 and p6 == ( b6 + b7 + b8) % 2:
            p4 = ( b5 + b6 + b8) % 2
        
        if p4 == ( b5 + b6 + b8) % 2 and p5 != ( b5 + b7 + b8) % 2 and p6  == ( b6 + b7 + b8) % 2:
            p5 = ( b5 + b7 + b8) % 2
        
        if p4 == ( b5 + b6 + b8) % 2 and p5 == ( b5 + b7 + b8) % 2 and p6  != ( b6 + b7 + b8) % 2:
            p6 = ( b6 + b7 + b8) % 2


        if p4 != ( b5 + b6 + b8) % 2 and p5 != ( b5 + b7 + b8) % 2 and p6  == (b6 + b7 + b8) % 2:
             if b5 == 0:
                 b5 = 1
             else :
                b5 = 0
        if p4 != ( b5 + b6 + b8) % 2 and p5 == ( b5 + b7 + b8) % 2 and p6  != ( b6 + b7 + b8) % 2:
             if b6 == 0:
                 b6 = 1
             else :
                b6 = 0
        
        if p4 == ( b5 + b6 + b8) % 2 and p5 != ( b5 + b7 + b8) % 2 and p6  != ( b6 + b7 + b8) % 2:
             if b7 == 0:
                 b7 = 1
             else :
                b7 = 0
        
        if p4 != ( b5 + b6 + b8) % 2 and p5 != (b5 + b7 + b8) % 2 and p6  != (b6 + b7 + b8) % 2:
             if b8 == 0:
                 b8 = 1
             else :
                b8 = 0
        
        print("erreur corriger")
        return[b1,b2,b3,b4,p1,p2,p3,b5,b6,b7,b8,p4,p5,p6]
    

correcteur([[ 0,1,1,0,   1,1,0,    1,0,0,1, 1,0,0 ]])

