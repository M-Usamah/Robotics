'''
Exercise 3: Generating random numbers

a) Create a vector with 100000 random variables which are normally distributed 
with a mean of 5.0 and a standard deviation of 2.0.
b) Create a vector with 100000 uniformly distributed random variables between 
0 and 10.
c) Compute the mean and standard deviation of the two vectors with random 
variables. Are the results what you would expect?
d) Modify your script so that the generated distributions are exactly the same 
each time you call it.
'''

import numpy as np
import matplotlib.pyplot as plt

uni_Dist =np.random.uniform(0,10,1000000) #b) Create a vector with 100000 uniformly distributed random variables between 
print(uni_Dist)
plt.plot(uni_Dist)
plt.show()



print("*************************************************")


dist =np.random.normal(5,2,10000)
plt.plot(dist)
plt.show()

print("The mean is ")
print(np.mean(dist))
print("The std is ")
print(np.std(dist))


