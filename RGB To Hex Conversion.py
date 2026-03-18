def rgb(r, g, b):
    l=[]
    l.append(decToHex(r))
    l.append(decToHex(g))
    l.append(decToHex(b))
    return "".join(l)



def decToHex(num):
    if num>255:
        result = "FF"
    elif num < 0:
        result = "00"
    elif num <16:
        prefix = "0"
        result= prefix+hex(num)[2:].upper()
    else:
        result =hex(num)[2:].upper()
    return result



print(rgb(15 ,-60 ,114))

print(decToHex(16))