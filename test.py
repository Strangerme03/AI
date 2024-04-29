
for  i in range(100):
  if(i%3==0):
    print(i,'\n')
  
import numpy as np
x=np.array([1,2,3,4])
print (x)

from math import exp
def sigmoid(x):
  return (1/(1+exp(-x)))