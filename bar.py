import numpy as np
from matplotlib import pyplot

x=[1,2,3,4,5,6];
y=[100,90,70,50,100,50];
print("[0;31;46m");
print("array x");
print(x);
print("array y");
print(y);
pyplot.title("plot demo");
pyplot.xlabel("x");
pyplot.ylabel("y");
pyplot.bar(x,y,color = "c");
pyplot.show()
