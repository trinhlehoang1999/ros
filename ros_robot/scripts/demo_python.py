# from xmlrpc.client import MultiCall
import rospy 
from std_msgs.msg import String
from turtlesim.msg import Pose
from visualization_msgs.msg import Marker

# from geometry_msgs.msg import PoseStamped

class MY_ROS:

    def __init__(self):

        # self.msg = msgs
        rospy.init_node('demo1',anonymous=False)
        self.turtle_Marker = Marker()
        self.turtle_Marker.header.frame_id = "map"
        self.turtle_Marker.header.stamp = rospy.Time.now()
        self.turtle_Marker.ns = "my_namespace"
        self.turtle_Marker.id = 0
        self.turtle_Marker.type = Marker.CYLINDER
        self.turtle_Marker.action = Marker.ADD
        self.turtle_Marker.scale.x = 1.0
        self.turtle_Marker.scale.y = 1.0
        self.turtle_Marker.scale.z = 1.0
        self.turtle_Marker.color.a = 1.0
        self.turtle_Marker.color.r = 1.0
        self.turtle_Marker.color.g = 0.0
        self.turtle_Marker.color.b = 0.0
        self.turtle_Marker.pose.orientation.x = 0.0
        self.turtle_Marker.pose.orientation.y = 0.0
        self.turtle_Marker.pose.orientation.z = 0.0
        self.turtle_Marker.pose.orientation.w = 1.0
        self.turtle_Marker.pose.position.x = 0.0
        self.turtle_Marker.pose.position.y = 0.0
        self.turtle_Marker.pose.position.z = 0.0
       



    def ros_sub_turtleSim_callback(self,data):
        self.turtle_Marker.pose.position.x = data.x
        self.turtle_Marker.pose.position.y = data.y     
        self.ros_pub_turtleSim_Pose.publish(self.turtle_Marker) 
        print("timer ros : {}".format(rospy.Time.now()))

    def ros_publish_turtleSim(self):
        self.ros_pub_turtleSim_Pose = rospy.Publisher('my_turtleSim_Pose',Marker,queue_size=100)

    def ros_sub_turtleSim(self):
        rospy.Subscriber('/turtle1/pose',Pose,self.ros_sub_turtleSim_callback)

    
my_ros = MY_ROS()
my_ros.ros_publish_turtleSim()
my_ros.ros_sub_turtleSim()
rospy.spin()

