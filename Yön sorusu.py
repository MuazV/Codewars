def dirReducc(arr):
    n = 0
    e = 0
    w = 0
    s = 0
    for i in arr:
        if i == "NORTH":
            n += 1
        elif i == "EAST":
            e += 1
        elif i == "WEST":
            w +=1
        elif i == "SOUTH":
            s+=1

    liste2 = [] 
    if n-s < 0 :
        liste2.append(["SOUTH"]*abs(n-s))
    elif n-s == 0:
        pass
    elif n-s > 0:
        liste2.append(["NORTH"]*abs(n-s))
    if e-w < 0 :
        liste2.append(["WEST"]*abs(e-w))
    elif e-w == 0:
        pass
    elif e-w > 0:
        liste2.append(["EAST"]*abs(e-w))


print(dirReducc(["SOUTH", "WEST"]))

