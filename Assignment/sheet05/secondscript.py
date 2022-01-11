'''
Exercise 2: Odometry-based Motion Model

A working motion model is a requirement for all Bayes Filter implementations. In the 
following, you will implement the simple odometry-based motion model.
a) Implement the odometry-based motion model in Python. Your function should
take the following three arguments
𝑥𝑡 = (
𝑥
𝑦
𝜃
) 𝑢𝑡 = (
𝛿𝑟1
𝛿𝑟2
𝛿𝑡
) 𝛼 = (
𝛼1
𝛼2
𝛼3
𝛼4
)
 where 𝑥𝑡
is the pose of the robot before moving, 𝑢𝑡
is the odometry reading 
obtained from the robot, and α are the noise parameters of the motion model. The 
return value of the function should be the new pose 𝑥𝑡+1 of the robot predicted by 
the model.
 As we do not expect the odometry measurements to be perfect, you will have to 
 take the measurement error into account when implementing your function. Use 
 the sampling methods you implemented in Exercise 1 to draw normally 
 distributed random numbers for the noise in the motion model (or use
 numpy.random.normal).
b) If you evaluate your motion model over and over again with the same starting
position, odometry reading, and noise values what is the result you would expect?
c) Evaluate your motion model 5000 times for the following values
𝑥𝑡 = (
2.0
4.0
0.0
) 𝑢𝑡 = (
𝜋
2
0.0
1.0
) 𝛼 = (
0.1
0.1
0.01
0.01
)
 Plot the resulting (x, y) positions for each of the 5000 evaluations in a single plot

'''

import myfirstscript as snd
import numpy as np
import math
import matplotlib.pyplot as plt
def sample_normal(mu, sigma):
    return snd.sample_normal_twelve(mu,sigma)

def sample_odometry_motion_model(x, u, a):
    delta_hat_r1 = u[0] + sample_normal(0, a[0]*abs(u[0]) + a[1]*u[2])
    delta_hat_t = u[2] + sample_normal(0, a[2]*u[2] + a[3]*(abs(u[0])+abs(u[1])))
    delta_hat_r2 = u[1] + sample_normal(0, a[0]*abs(u[1]) + a[1]*u[2])
    x_prime = x[0] + delta_hat_t * math.cos(x[2] + delta_hat_r1)
    y_prime = x[1] + delta_hat_t * math.sin(x[2] + delta_hat_r1)
    theta_prime = x[2] + delta_hat_r1 + delta_hat_r2
    return np.array([x_prime, y_prime, theta_prime])

def main():
    x = [2, 4, 0]
    u = [np.pi/2, 0, 1]
    a = [0.1, 0.1, 0.01, 0.01]
    num_samples = 5000
    x_prime = np.zeros([num_samples, 3])
    for i in range(0, num_samples):
        x_prime[i,:] = sample_odometry_motion_model(x,u,a)
    plt.plot(x[0], x[1], "bo")
    plt.plot(x_prime[:,0], x_prime[:,1], "r,")
    plt.xlim([1, 3])
    plt.axes().set_aspect('equal')
    plt.xlabel("x-position [m]")
    plt.ylabel("y-position [m]")
    plt.savefig("odometry_samples.pdf")
    plt.show()
if __name__ == "__main__":
    main()

