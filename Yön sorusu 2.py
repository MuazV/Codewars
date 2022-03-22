def dirReduc(arr):
    dictin = {"s" : 1,
              "n" : -1,
              "e" : -1,
              "w" : 1
                }


    ns = 0
    we = 0
    liste2 = ""

    for i in arr:
        if i == "s" or i == "n":
            ns += dictin[i]
        else :
            we += dictin[i]
    if we > 0:
        liste2 += "w"*we
    else:
        liste2 += "e"*abs(we)
    if ns > 0:
        liste2 += "s"*abs(ns)
    else:
        liste2 += "n" * ns
    return liste2


print(dirReduc(["s", "n", "e", "w", "w","w","s"]))