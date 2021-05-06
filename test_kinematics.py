from Foward_Kinematics import FK
from Inverse_Kinematics import IK
from math import pi, cos

theta = [0]*3+[pi/2]*3
T = FK(theta)
print(T)
T = IK(T)
print(T)







