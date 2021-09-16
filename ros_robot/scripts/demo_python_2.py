
import rospy 

from turtlesim.msg import Pose
from visualization_msgs.msg import Marker
from geometry_msgs.msg import PoseStamped
from nav_msgs.msg import Path
ii = 0
class MY_ROS:

    def __init__(self):
        #####################3 maker for cube rviz
        # self.msg = msgs
        rospy.init_node('demo1',anonymous=False)
        self.turtle_Marker = Marker()
        self.turtle_Marker.header.frame_id = "map"
        self.turtle_Marker.header.stamp = rospy.Time.now()
        self.turtle_Marker.ns = "my_namespace"
        self.turtle_Marker.id = 0
        self.turtle_Marker.type = Marker.CYLINDER
        self.turtle_Marker.action = Marker.ADD
        self.turtle_Marker.scale.x = 0.1
        self.turtle_Marker.scale.y = 0.1
        self.turtle_Marker.scale.z = 0.1
        self.turtle_Marker.color.a = 1.0
        self.turtle_Marker.color.r = 1.0
        self.turtle_Marker.color.g = 0.0
        self.turtle_Marker.color.b = 0.0
        self.turtle_Marker.pose.orientation.x = 0.0
        self.turtle_Marker.pose.orientation.y = 0.0
        self.turtle_Marker.pose.orientation.z = 0.0
        self.turtle_Marker.pose.orientation.w = 1.0
        self.turtle_Marker.pose.position.x = 0
        self.turtle_Marker.pose.position.y = 0
        self.turtle_Marker.pose.position.z = 0.0
       ######################### POSE rviz
        self.turtle_pose = PoseStamped()
        self.turtle_pose.header.frame_id = "map"
        self.turtle_pose.header.stamp = rospy.Time.now()
        self.turtle_pose.pose.orientation.w = 1
        # self.turtle_pose.pose.orientation.z = 2
        ######################### Path rviz
        self.turtle_path = Path()
        self.turtle_path.header.frame_id = "map"
        self.turtle_path.header.stamp = rospy.Time.now()

    def ros_sub_turtleSim_callback(self,data):#callback for marker
        self.turtle_Marker.pose.position.x = data.x
        self.turtle_Marker.pose.position.y = data.y     
        self.ros_pub_turtleSim_Pose.publish(self.turtle_Marker)

    def ros_sub_turtlesim_callback_2(self,data):#callback for pose
        self.turtle_pose.pose.position.x = data.x
        self.turtle_pose.pose.position.y = data.y
        self.turtle_pose.pose.orientation.z = data.theta
        self.ros_pub_posestamp.publish(self.turtle_pose)

    def ros_sub_turtlesim_callback_3(self,data):#callback for path

        self.turtle_path_pose = PoseStamped()
        self.turtle_path_pose.pose.position.z = 0.1 
        self.turtle_path_pose.pose.position.x = data.x
        self.turtle_path_pose.pose.position.y = data.y
        self.turtle_path_pose.header.seq = self.turtle_path_pose.header.seq + 1
        self.turtle_path_pose.header.frame_id = "map"
        self.turtle_path_pose.header.stamp = rospy.Time.now()
        self.turtle_path.poses.append(self.turtle_path_pose)
        self.ros_pub_path.publish(self.turtle_path)


    def ros_publish_pose_init(self):#pub data to control pose rviz
        self.ros_pub_posestamp = rospy.Publisher('turtleSim_PoseStamp',PoseStamped,queue_size=100)

    def ros_publish_turtleSim(self): #publish data to control cube in rviz
        self.ros_pub_turtleSim_Pose = rospy.Publisher('my_turtleSim_Pose',Marker,queue_size=100)

    def ros_publish_path(self): #publish data to control cube in rviz
        self.ros_pub_path = rospy.Publisher('my_turtleSim_Path',Path,queue_size=1)

    def ros_sub_turtleSim(self): #sub data from topic form /turtle1/pose and callback in ros_sub_turtleSim_callback
        rospy.Subscriber('/turtle1/pose',Pose,self.ros_sub_turtleSim_callback)

    def ros_sub_turtleSim_2(self):#sub data from topic form /turtle1/pose and callback in ros_sub_turtleSim_callback_2
        rospy.Subscriber('/turtle1/pose',Pose,self.ros_sub_turtlesim_callback_2)
    
    def ros_sub_turtleSim_3(self):#sub data from topic form /turtle1/pose and callback in ros_sub_turtleSim_callback_3
        rospy.Subscriber('/turtle1/pose',Pose,self.ros_sub_turtlesim_callback_3)

if __name__ == '__main__':    
    my_ros = MY_ROS()#define my_ros is class MY_ROS()
    my_ros.ros_publish_turtleSim()#publish cube data to rivz
    my_ros.ros_publish_pose_init()#publish pose data to rivz
    my_ros.ros_publish_path()
    # my_ros.ros_sub_turtleSim_3()
    my_ros.ros_sub_turtleSim_2()#sub data from topic /turtle1/pose
    my_ros.ros_sub_turtleSim()#sub data from topic /turtle1/pose
    my_ros.ros_sub_turtleSim_3()
    rospy.spin()

