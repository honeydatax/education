import numpy as np
from matplotlib import pyplot

x=np.arange(10,-10,-1);
y=x*5;
print("[0;31;46m");
print("array x");
print(x);
print("array y");
print(y);
pyplot.title("plot demo");
pyplot.xlabel("x");
pyplot.ylabel("y");
pyplot.plot(x,y,"oc");
pyplot.show()
