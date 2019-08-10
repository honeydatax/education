import time;
import sys;


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

def printf (toadds ):
    sys.stdout.write(toadds)
    sys.stdout.flush()
    return


# main program
for n in range (0,100):
    printf (center(19,str(n))+" % task done\r")
    time.sleep(0.09)
    
print "\ndone"


