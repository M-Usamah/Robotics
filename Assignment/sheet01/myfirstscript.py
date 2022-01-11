'''
Exercise 1: Defining functions
Functions in Python are usually defined inside a file. Create a file named 
myfirstscript.py and implement the following function:
f(x) = cos(x)exp(x)
Next, launch your script as python myfirstscript.py in the command line. In Python 
multiple functions can be defined in the same file and the filename is independent of 
the function names used in the file.
'''

import numpy as np
from numpy.core.function_base import linspace



def function(vec):
    return np.cos(vec) * np.exp(vec)


'''
Exercise 2: Plotting data
Every python file is a script which can be evaluated later. It can contain multiple 
functions and other numerical computations all in one file. The matplotlib.pyplot 
module can be used for plotting.
a) In the same python script write commands which plot the graph of the 
function f in the interval [−2π,2π]. Hint: python’s numpy module has as a 
special variable for π: numpy.pi
b) Save the resulting plot as a PNG-file to your hard disk
'''

import matplotlib.pyplot as plt

vec_x=linspace(-2*np.pi,2*np.pi)# [−2π,2π]
vec_y= function(vec_x)
plt.plot(vec_x,vec_y)
plt.show()
plt.savefig("sheet 1.png")


