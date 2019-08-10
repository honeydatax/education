def string ( toadd , toadds ):
    tadd=""
    for n in range (0,toadd):
        tadd=tadd + toadds
    return tadd


def space ( toadd ):
    tadd=""
    for n in range (0,toadd):
        tadd=tadd + " "
    return tadd


def center ( size , toadds ):
    tadd=""
    ssize=(size-len(toadds))/2
    tadd=space(ssize)+toadds
    return tadd

def code (size , toadds ):
    tadd=""
    ssize=(size-len(toadds))
    tadd=space(ssize)+toadds
    return tadd


# main program
print code (9,"id"),
print code (2,"|"),
print code (17,"name"),
print code (2,"|"),
print code (9,"value")
for n in range (0,15):
    print code (9,str(n)),
    print code (2,"|"),
    print code (17,"client " + str(n)),
    print code (2,"|"),
    print code (9,str(n))
    



