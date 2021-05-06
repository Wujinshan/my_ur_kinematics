import Commonly_uesd_function as cup
from math import pi
import ur_config

a = ur_config.UR5_DH_param.a
alpha = ur_config.UR5_DH_param.alpha
d = ur_config.UR5_DH_param.d

def FK(theta):
          #theta is a list
          T01 = cup.rotz(theta[0])*cup.trans(0,0,d[0])*cup.rotx(alpha[0])*cup.trans(a[0],0,0)
          T12 = cup.rotz(theta[1])*cup.trans(0,0,d[1])*cup.rotx(alpha[1])*cup.trans(a[1],0,0)
          T23 = cup.rotz(theta[2])*cup.trans(0,0,d[2])*cup.rotx(alpha[2])*cup.trans(a[2],0,0)
          T34 = cup.rotz(theta[3])*cup.trans(0,0,d[3])*cup.rotx(alpha[3])*cup.trans(a[3],0,0)
          T45 = cup.rotz(theta[4])*cup.trans(0,0,d[4])*cup.rotx(alpha[4])*cup.trans(a[4],0,0)
          T56 = cup.rotz(theta[5])*cup.trans(0,0,d[5])*cup.rotx(alpha[5])*cup.trans(a[5],0,0)
          T = T01*T12*T23*T34*T45*T56

          #计算cos和sin时有误差，将小于1e-10的数设为0
          for i in range(len(T)):
                    for j in range(len(T)):
                              if abs(T[i,j]) < 1e-10:
                                        T[i,j] = 0
                              else:
                                        pass
                              
          return T.tolist()

if __name__ == "__main__":
          theta = [0,0,0,0,0,0]
          FK(theta)

