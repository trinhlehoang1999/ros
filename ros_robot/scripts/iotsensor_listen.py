
import rospy
from ros_robot.msg import IOTSensor

class MY_ROS_LISTEN:
    def __init__(self):
        rospy.init_node("iot_sub_node",anonymous= True)
        rospy.Subscriber("iot_pub_topic",IOTSensor,self.iot_data_callback)
    
    def iot_data_callback(self,msg):
        rospy.loginfo("data: %d, %s, %.2f, %.2f",msg.id,msg.name,msg.temperature,msg.humidity)
        

if __name__ == '__main__':
    myros = MY_ROS_LISTEN()
    rospy.spin()


