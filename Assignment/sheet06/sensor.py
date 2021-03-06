import math
import numpy as np
import scipy.stats
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
def likelihood(m):
    x_0 = np.array([12,4])
    x_1 = np.array([5,7])
    d_0 = 3.9
    d_1 = 4.5
    var_0 = 1
    var_1 = 1.5
    d_0_hat = math.sqrt(np.sum(np.square(m-x_0)))
    d_1_hat = math.sqrt(np.sum(np.square(m-x_1)))
    pdf_0 = scipy.stats.norm.pdf(d_0, d_0_hat,math.sqrt(var_0))
    pdf_1 = scipy.stats.norm.pdf(d_1, d_1_hat,math.sqrt(var_1))
    return pdf_0 * pdf_1
m_0 = np.array([10,8])
m_1 = np.array([6,3])
x_0 = np.array([12,4])
x_1 = np.array([5,7])
x = np.arange(3.0,15.0,0.5)
y = np.arange(-5.0,15.0,0.5)
X,Y = np.meshgrid(x,y)
z = np.array([likelihood(np.array([x,y])) for x,y in zip(X.flatten(), Y.flatten())])
Z = z.reshape(X.shape)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X,Y,Z,rstride=1,cstride=1,cmap=cm.coolwarm,alpha=0.5)
ax.scatter(m_0[0],m_0[1],likelihood(m_0),c='g',marker='o',s=100)
ax.scatter(m_1[0],m_1[1],likelihood(m_1),c='r',marker='o',s=100)
ax.scatter(x_0[0],x_0[1],likelihood(x_0),c='g',marker='^',s=100)
ax.scatter(x_1[0],x_1[1],likelihood(x_1),c='r',marker='^',s=100)
ax.set_xlabel('m_x')
ax.set_ylabel('m_y')
ax.set_zlabel('likelihood')
plt.show()