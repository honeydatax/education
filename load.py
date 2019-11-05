import numpy as np
from sklearn import svm
import pandas as pd

x=np.loadtxt ( "loto.cvs" ,delimiter ="," , dtype = { "names" : ( "number" , "loto" ) , "formats" : ( "i4" , "i4" ) } );
print("[0;31;46m");
print("array x");
print(x);
