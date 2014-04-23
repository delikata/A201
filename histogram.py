import string

def histogram(L): 
    d = {} 
    for x in L:
        if x in string.ascii_letters:
            x = x.lower()
            if x in d:
                d[x] += 1 
            else: d[x] = 1 
        else:
            continue
    return d 


