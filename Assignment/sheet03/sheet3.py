'''
Write a function in Python that implements the forward kinematics for the differential
drive as explained in the lecture.
a) The function header should look like
def diffdrive(x, y, theta, v_l, v_r, t, l):
 return x_n, y_n, theta_n
 where x, y, and  is the pose of the robot, vl and vr are the speed of the left and 
 right wheel, t is the driving time, and l is the distance between the wheels of the 
 robot. The output of the function is the new pose of the robot xn, yn, and n

'''

import numpy as np
def diffdrive(x, y, theta, v_l, v_r, t, l):
    
    # straight line
    if (v_l == v_r):
        theta_n = theta
        x_n = x + v_l * t * np.cos(theta)
        y_n = y + v_l * t * np.sin(theta)
        # circular motion

    else:
        # Calculate the radius
        R = l/2.0 * ((v_l + v_r) / (v_r - v_l))
        # computing center of curvature
        ICC_x = x - R * np.sin(theta)
        ICC_y = y + R * np.cos(theta)
        # compute the angular velocity
        omega = (v_r - v_l) / l
        # computing angle change
        dtheta = omega * t
        # forward kinematics for differential drive
        x_n = np.cos(dtheta)*(x-ICC_x) - np.sin(dtheta)*(y-ICC_y) + ICC_x
        y_n = np.sin(dtheta)*(x-ICC_x) + np.cos(dtheta)*(y-ICC_y) + ICC_y
        theta_n = theta + dtheta
    return x_n, y_n, theta_n

'''
b) After reaching position x = 1.5m, y = 2.0m, and θ =
π
2
the robot executes the
following sequence of steering commands:
(a) c1 = (vl = 0.3m/s, vr = 0.3m/s, t = 3s)
(b) c2 = (vl = 0.1m/s, vr = −0.1m/s, t = 1s)
(c) c3 = (vl = 0.2m/s, vr = 0m/s, t = 2s)
Use the function to compute the position of the robot after the execution of each
command in the sequence (the distance l between the wheels of the robot is 0.5m).

'''

import numpy as np
import matplotlib.pyplot as plt
plt.gca().set_aspect('equal')

# set the distance between the wheels and the initial robot position
l = 0.5
x, y, theta = 1.5, 2.0, (np.pi)/2.0
# plot the starting position
plt.quiver(x, y, np.cos(theta), np.sin(theta))
print ("starting pose: x: %f, y: %f, theta: %f" % (x, y, theta))
# first motion
v_l = 0.3
v_r = 0.3
t = 3
x, y, theta = diffdrive(x, y, theta, v_l, v_r, t, l)
plt.quiver(x, y, np.cos(theta), np.sin(theta))
print ("after motion 1: x: %f, y: %f, theta: %f" % (x, y, theta))
# second motion
v_l = 0.1
v_r = -0.1
t = 1
x, y, theta = diffdrive(x, y, theta, v_l, v_r, t, l)
plt.quiver(x, y, np.cos(theta), np.sin(theta))
print ("after motion 2: x: %f, y: %f, theta: %f" % (x, y, theta))
# third motion
v_l = 0.2
v_r = 0.0
t = 2
x, y, theta = diffdrive(x, y, theta, v_l, v_r, t, l)
plt.quiver(x, y, np.cos(theta), np.sin(theta))
print ("after motion 3: x: %f, y: %f, theta: %f" % (x, y, theta))
plt.xlim([0.5, 2.5])
plt.ylim([1.5, 3.5])
plt.savefig("poses.png")
plt.show()
