ur_kinematics不是ros功能包!!!!!

文件说明：
1.ur_config.py:
          ur机械臂的相关参数，包含UR5的DH参数等，可自行添加不同的UR机械臂的DH参数，当DH参数改变时注意在正运动学和逆运动学求解时进行改变

2.Commonly_used_function.py:
          包括运动学齐次坐标变换的常用函数，如rotx,trans等，用于正运动学调用

3.Foward_Kinematics.py:
          其中FK()为正运动学求解函数，调用ur_config.py中的DH参数和Commonly_used_function.py中的齐次坐标变换函数求运动学正解

4.Inverse_Kinematics.py:
          其中IK()为逆运动学求解函数

5.control_abs_angles_in_pi.py:
          角度控制函数，在逆运动学模块中调用，使得求解的角度值在-pi—pi之间

6.test_kinematics.py:
          测试文件，测试正运动学和逆运动学是否正确
