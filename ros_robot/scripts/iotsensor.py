import rospy
from ros_robot.msg import IOTSensor

class MY_ROS:
    
    def __init__(self):
        self.pub = rospy.Publisher("iot_pub_topic",IOTSensor,queue_size=10)
        rospy.init_node("iot_pub_node",anonymous= True)

        self.rate = rospy.Rate(1)

        self.iot_data = IOTSensor()
        self.iot_data.id = 1
        self.iot_data.name = "hoang_house_iot"


    def pub_data_process(self):
        i = 0
        while not rospy.is_shutdown():
            self.iot_data.humidity = 20 + i
            self.iot_data.temperature = 35 + 2*i
            rospy.loginfo("processing_publish")
            rospy.loginfo(self.iot_data)
            self.pub.publish(self.iot_data)
            self.rate.sleep()
            i = i + 1

if __name__ == '__main__':
    myros = MY_ROS()
    myros.pub_data_process()




