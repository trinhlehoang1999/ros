#!/usr/bin/env python

import rospy
from std_msgs.msg import Int16MultiArray
import math
import tf

# from nav_msgs.msg import Odometry

class My_ros:
    def __init__(self):
        rospy.init_node('listener', anonymous=False)
        
        
    def sub(self):
        rospy.Subscriber("IMU_data", Int16MultiArray, self.callback_sub,3)

    def pub(self):
        pass

    def callback_sub(self,data):
        
        self._data_yaw = data.data[0]
        self._data_roll = data.data[1]
        self._data_pitch = data.data[2]
        print("{} : {} : {}".format(self._data_yaw,self._data_pitch,self._data_roll))
        # yaw = math.radians(_data_yaw)
        # quaternion = tf.transformations.quaternion_from_euler(_data_roll,_data_pitch,yaw)
        # for i in range(4):
	    #     print(quaternion[i])
        #rospy.loginfo("get data yaw completely: %d" %quaternion[2])
        


if __name__ == '__main__':
    myros=My_ros()
    myros.sub()
    rospy.spin()