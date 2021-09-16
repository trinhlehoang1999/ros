#!/usr/bin/env python
#rosrun ros_robot turtle_go_straight.py 0.8 5 2

from __future__ import print_function
import sys

import math
import time
from rosgraph.roslogging import renew_latest_logdir
import rospy 
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist
x = 0
y = 0
yaw = 0
class MY_ROS:
    global x, y ,x0, y0

    x0 = x
    y0 = y
    def __init__(self):
        rospy.loginfo("start")
        rospy.init_node('demo',anonymous=False)
        self.velocity_message = Twist()
#########################
    def move(self,speed,distance,is_forward):
        
        if is_forward == 1:
            self.velocity_message .linear.x = abs(speed)
        else:
            self.velocity_message.linear.x = -abs(speed)
        
        self.distance_move = 0
        self.loop_rate = rospy.Rate(1)

        while True:
            rospy.loginfo("turtle moves forward")
            self.velocity_publisher.publish(self.velocity_message)
            self.loop_rate.sleep()
            self.distance_move = abs(math.sqrt(((x - x0)**2) + ((y - y0)**2)))
            print("value_distance = {}".format(self.distance_move))
            if not self.distance_move < distance:
                rospy.loginfo("reached")
                break
        self.velocity_message.linear.x = 0
        self.velocity_publisher.publish(self.velocity_message)
 ###########################################   
    def rotate(self,angular_speed_degree, ref_angle_degree,clockwise):
        angular_speed = math.radians(abs(angular_speed_degree))

        if clockwise == 1 :
            self.velocity_message.angular.z = -abs(angular_speed)
        else:
            self.velocity_message.angular.z = abs(angular_speed)
        
        self.loop_rate = rospy.Rate(10)
        self.t0 = rospy.Time.now().to_sec()

        while True:
            rospy.loginfo("turtle_sim_rotates")
            self.velocity_publisher.publish(self.velocity_message)
            
            self.t1 = rospy.Time.now().to_sec()
            print("angular_speed : {} and time :{}".format(angular_speed,(self.t1 - self.t0)))
            self.current_angle_degree = ((self.t1 - self.t0)*angular_speed_degree)
            print("value_rotate : {}".format(self.current_angle_degree))
            self.loop_rate.sleep()

            if self.current_angle_degree > ref_angle_degree:
                rospy.loginfo("reached")
                break
        self.velocity_message.angular.z = 0
        self.velocity_publisher.publish(self.velocity_message)
#################################################
    def set_desire_orientation(self,speed_in_degree,desired_angle_degree):

        self.relatile_angle_radians = math.radians(desired_angle_degree) - yaw
        self.clockwise = 0
        if self.relatile_angle_radians < 0:
            self.clockwise = 1
        else:
            self.clockwise = 0

        print("relatile_angle_degree:{}".format(self.relatile_angle_radians))
        print("desired_angle_degree:{}".format(desired_angle_degree))
        myros.rotate(speed_in_degree,math.degrees(abs(self.relatile_angle_radians)),self.clockwise)
#####################################################
    def go_to_goal(self,Kp_linear,Kp_angular,x_goal,y_goal):

        while True :
            self.Kp_linear = Kp_linear
            self.Kp_angular = Kp_angular

            self.distance = abs(math.sqrt(((x_goal - x)**2) + ((y_goal - y)**2)))
            self.linear_speed = self.distance * self.Kp_linear
        
            self.desired_angular_goal = math.atan2(y_goal - y,x_goal - x)
            self.angular_speed = (self.desired_angular_goal - yaw)*self.Kp_angular

            self.velocity_message.linear.x = self.linear_speed
            self.velocity_message.angular.z = self.angular_speed

            self.velocity_publisher.publish(self.velocity_message)
            print("x= {}, y= {}, distance to goal= {}".format(x,y,self.distance))
            if self.distance < 0.02:
                break
            
            self.velocity_message.angular.z = 0
            self.velocity_message.linear.x  = 0
            self.velocity_publisher.publish(self.velocity_message)       
    ######################################   
    def ros_pub_turtle(self):
        self.velocity_publisher = rospy.Publisher('turtle1/cmd_vel',Twist,queue_size=10)
        
    def ros_sub_turtle(self):
        rospy.Subscriber('turtle1/pose',Pose,self.calback)
        
    def calback(self,msg):
        global x,y,yaw
        x = msg.x
        y = msg.y
        yaw = msg.theta     
        ####################################



def function_go_to_goal():

    if len(sys.argv) == 5:
        KP_linear_ref = float(sys.argv[1])
        KP_angular_ref = float(sys.argv[2])
        X_ref = float(sys.argv[3])
        Y_ref = float(sys.argv[4])
    else:
        print("%s [x y string]"%sys.argv[0])
        sys.exit(1)
    myros.go_to_goal(KP_linear_ref,KP_angular_ref,X_ref,Y_ref)
    # time.sleep(1)

def function_go_to_straigh():
    if len(sys.argv) == 4:
        speed_ref = float(sys.argv[1])
        distance_ref = float(sys.argv[2])
        is_forward = float(sys.argv[3])
    else:
        print("%s [x y string]"%sys.argv[0])
        sys.exit(1)
    
    myros.move(speed_ref,distance_ref,is_forward)

def function_go_to_rotate():
    if len(sys.argv) == 4:
        speed_ref = float(sys.argv[1])
        distance_ref = float(sys.argv[2])
        is_forward = float(sys.argv[3])
    else:
        print("%s [x y string]"%sys.argv[0])
        sys.exit(1)
    
    myros.rotate(speed_ref,distance_ref,is_forward)

def function_set_desired_angle():
    if len(sys.argv) == 3:
        speed_ref = float(sys.argv[1])
        distance_ref = float(sys.argv[2])

    else:
        print("%s [x y ]"%sys.argv[0])
        sys.exit(1)
    myros.set_desire_orientation(speed_ref,distance_ref)


if __name__ == '__main__':
    # if len(sys.argv) == 4:
    #     x = float(sys.argv[1])
    #     y = float(sys.argv[2])
    #     String = float(sys.argv[3])
    # else:
    #     print("%s [x y string]"%sys.argv[0])
    #     sys.exit(1)

    myros = MY_ROS()
    myros.ros_pub_turtle()
    myros.ros_sub_turtle()
    # function_go_to_goal()
    #function_set_desired_angle()
    #function_go_to_rotate()
    # function_go_to_straigh()

    x_goal = rospy.get_param("x_goal")
    y_goal = rospy.get_param("y_goal")

    myros.go_to_goal(0.8,5,x_goal,y_goal)
    # myros.rotate(x,y,String)
    # myros.move(x,y,String)
    
    
    
    
    

    



    


