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


for nn in range (2,39,2):
    print (center(79,string(nn,"*")))



