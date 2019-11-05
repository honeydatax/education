import numpy as np
from sklearn import preprocessing

x=np.arange(10,-10,-1);
print("[0;31;46m");
print("array");
print(x);

y=preprocessing.Binarizer(threshold = 0.5).transform(x.reshape(20,1));
print("binary array");
print(y);
