文件说明：

1.ur_config.py:
          ur机械臂的相关参数，包含UR5的DH参数等，可自行添加不同的UR机械臂的DH参数，当DH参数改变时注意在正运动学和逆运动学求解时进行改变

2.Commonly_used_function.py:
          包括运动学齐次坐标变换的常用函数，如rotx,trans等，用于正运动学调用
          
3.Foward_Kinematics.py:
          其中FK()为正运动学求解函数，调用ur_config.py中的DH参数和Commonly_used_function.py中的齐次坐标变换函数求运动学正解
          
4.Inverse_Kinematics.py:
          其中IK()为逆运动学求解函数，需要输入末端的其次矩阵，输出为求解得到的8组关节角度结果
          
5.control_abs_angles_in_pi.py:
          角度控制函数，在逆运动学模块中调用，使得求解的角度值在-pi—pi之间
          
6.test_kinematics.py:
          测试文件，测试正运动学和逆运动学是否正确
          
7.select_ik_solution.py:
          逆运动学求解结果选择文件，需要输入参考角度和逆运动学求解的8组结果，输出为与参考角度最接近的逆运动学解
          
File description:

1.ur_config.py:
          Related parameters of ur manipulator, including DH parameters of UR5, etc., you can add different DH parameters of UR manipulator by yourself. When the DH parameters are changed, pay          attention to the change in the solution of forward kinematics and inverse kinematics.
          
2.Commonly_used_function.py:
          Including common functions of kinematics homogeneous coordinate transformation, such as rotx, trans, etc., used for positive kinematics calls

3.Foward_Kinematics.py:
          Where FK() is the positive kinematics solution function, call the DH parameter in ur_config.py and the homogeneous coordinate transformation function in Commonly_used_function.py to find the positive kinematics solution

4.Inverse_Kinematics.py:
          Among them, IK() is the inverse kinematics solving function, which requires the input of the secondary matrix at the end, and the output of the 8 sets of joint angle results

5.control_abs_angles_in_pi.py:
          Angle control function, which is called in the inverse kinematics module, so that the solved angle value is between -pi-pi

6.test_kinematics.py:
          Test file to test whether the forward kinematics and inverse kinematics are correct

7.select_ik_solution.py:
          Inverse kinematics solution result selection file, you need to input 8 sets of results of the reference angle and inverse kinematics solution, and the output is the inverse kinematics solution closest to the reference angle          
