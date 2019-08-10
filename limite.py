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

def zero (size , toadds ):
    tadd=""
    ssize=(size-len(toadds))
    tadd=string(ssize,"0")+toadds
    return tadd

def txts (size , toadds ):
    tadd=""
    ssize=(size-len(toadds))
    tadd=toadds+space(ssize)
    return tadd

def limete (size , toadds ):
    tadd=""
    ssize=(size-len(toadds))
    tadd=toadds+space(ssize)
    tadd=tadd[1:size]
    return tadd

# main program
l="012345678901234567890123456789012345678901234567890123456789"
for n in range (1,19):
    print limete (n,l)
    



