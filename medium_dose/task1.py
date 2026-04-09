#importing necessary libraries for working with matrices and trignometric functions
import numpy as np
import math

#getting inputs
coc=list(map(int, input("Enter the Object Coordinates:").split(",")))
rp=list(map(int, input("Enter the Rover Position:").split(",")))
rr=list(map(int, input("Enter the Rover Rotation:").split(",")))

#converting the object coords and rover position to a 1x3 matrix
coc=np.array([[coc[0]], [coc[1]] , [coc[2]]])
rp=np.array([[rp[0]], [rp[1]] , [rp[2]]])

#converting the angles given in input to radians as sin and cos function in math library accepts radians as input
xang=math.radians(rr[0])
yang=math.radians(rr[1])
zang=math.radians(rr[2])

#creating the rotation matrix about each axis
X=np.array([[1, 0, 0], [0, math.cos(xang), (-1)*math.sin(xang)], [0, math.sin(xang), math.cos(xang)]])
 
Y=np.array([[math.cos(yang), 0, math.sin(yang)], [0, 1, 0], [(-1)*math.sin(yang), 0, math.cos(yang)]])

Z=np.array([[math.cos(zang), (-1)*math.sin(zang), 0], [math.sin(zang), math.cos(zang), 0], [0, 0, 1]])

#computing the rotated coords
rm=Z@Y@X@coc
#computing the translated coords and the rotated coords
woc=rm+rp

#displaying output
print("Object Coordinates (World Frame):\n", (woc[0][0], woc[1][0], woc[2][0]))