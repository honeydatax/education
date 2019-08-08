import random;
import sys;

def numbers(nn):
        n=eval(raw_input("a number 0 < 100 ?"))
        
        if n > 100:
            print "number not valid"
    
        if n < 0:
            print "number not valid"
            
        if n > nn:
            print "number to big"
    
        if n < nn:
            print "number to lower"

        return n


h=random.randrange (0,100,1)

for n in range (0,10):
    
    print "try many times:",n
    t=numbers(h)

    if t == h:
            print "you win"
            break
    
