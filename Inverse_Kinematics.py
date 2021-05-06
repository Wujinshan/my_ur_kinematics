from math import pi, atan2, sqrt, acos, sin, cos
import numpy as np
import ur_config
from control_abs_angles_in_pi import control_angles

a = ur_config.UR5_DH_param.a
alpha = ur_config.UR5_DH_param.alpha
d = ur_config.UR5_DH_param.d

def IK(T):
          nx = T[0][0]
          ny = T[1][0]
          nz = T[2][0]
          ox = T[0][1]
          oy = T[1][1]
          oz = T[2][1]
          ax = T[0][2]
          ay = T[1][2]
          az = T[2][2]
          px = T[0][3]
          py = T[1][3]
          pz = T[2][3]

          #求解theta1
          m=d[5]*ay-py
          n=ax*d[5]-px
          theta1 = [0]*8
          for i in range(4):
                    theta1[i] = atan2(m,n)-atan2(d[3],sqrt(m**2+n**2-d[3]**2))
                    theta1[i+4] = atan2(m,n)-atan2(d[3],-1*sqrt(m**2+n**2-d[3]**2))

          #求解theta5
          theta5 = [0]*8
          theta5[0] = acos(ax*sin(theta1[0])-ay*cos(theta1[0]))
          theta5[1] = theta5[0]
          theta5[2] = -1*theta5[0]
          theta5[3] = theta5[2]
          theta5[4] = acos(ax*sin(theta1[4])-ay*cos(theta1[4]))
          theta5[5] = theta5[4]
          theta5[6] = -1*theta5[4]
          theta5[7] = theta5[6]

          #求解theta6
          theta6 = [0]*8
          for i in range(8):
                    m = nx*sin(theta1[i])-ny*cos(theta1[i])
                    n = ox*sin(theta1[i])-oy*cos(theta1[i])
                    theta6[i] = atan2(m,n)-atan2(sin(theta5[i]),0)
          
          #求解theta3
          theta3 = [0]*8
          m = [0]*8
          n = [0]*8
          for i in range(8):
                    m[i] = d[4]*(sin(theta6[i])*(nx*cos(theta1[i])+ny*sin(theta1[i]))+cos(theta6[i])*(ox*cos(theta1[i])+oy*sin(theta1[i])))-d[5]*(ax*cos(theta1[i])+ay*sin(theta1[i]))+px*cos(theta1[i])+py*sin(theta1[i])
                    n[i] = pz-d[0]-az*d[5]+d[4]*(oz*cos(theta6[i])+nz*sin(theta6[i]))
                    if (i%2) == 0:
                              theta3[i] = acos((m[i]**2+n[i]**2-a[1]**2-a[2]**2)/(2*a[1]*a[2]))
                    else:
                              theta3[i] = -1*acos((m[i]**2+n[i]**2-a[1]**2-a[2]**2)/(2*a[1]*a[2]))

          #求解theta2    
          theta2 = [0]*8
          s2 = [0]*8
          c2 = [0]*8
          for i in range(8):
                    s2[i] = ((a[2]*cos(theta3[i])+a[1])*n[i]-a[2]*sin(theta3[i])*m[i])/(a[1]**2+a[2]**2+2*a[1]*a[2]*cos(theta3[i]))
                    c2[i] = (m[i]+a[2]*sin(theta3[i])*s2[i])/(a[2]*cos(theta3[i])+a[1])
                    theta2[i] = atan2(s2[i],c2[i])

          #求解theta4
          theta4 = [0]*8
          for i in range(8):
                    theta4[i] = atan2(-1*sin(theta6[i])*(nx*cos(theta1[i])+ny*sin(theta1[i]))-cos(theta6[i])*(ox*cos(theta1[i])+oy*sin(theta1[i])),oz*cos(theta6[i])+nz*sin(theta6[i]))-theta2[i]-theta3[i]        

          solution = [0]*8
          for i in range(8):
                    solution[i] = control_angles([theta1[i],theta2[i],theta3[i],theta4[i],theta5[i],theta6[i]])

          return solution

if __name__ == "__main__":
          T = np.matrix([[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]])
          IK(T)