#!/usr/bin/env python
import rospy

from nav_msgs.msg import Path
from nav_msgs.msg import Odometry
from geometry_msgs.msg import PoseStamped
from geometry_msgs.msg import Pose

path = Path()
path.header.frame_id = "map"
seq = 0

def cartesian_to_path(x, y):
    global seq
    path.header.stamp = rospy.Time.now()

    for i, xi in enumerate(x):
        pose = PoseStamped()
        pose.header.stamp = rospy.Time.now()
        pose.header.frame_id = "map"
        pose.header.seq = seq
        pose.pose.position.x = xi
        pose.pose.position.y = y[i]
        pose.pose.position.z = 0
        path.poses.append(pose)
    seq += 1

    # print(path)
    path_pub.publish(path)

rospy.init_node('path_node')
path_pub = rospy.Publisher('path', Path, queue_size=10)
r = rospy.Rate(0.5)

if __name__ == '__main__':
    x = [ 3.86600947,  3.80181702,  3.72560205,  3.6376916 ,  3.53846288,
        3.42834168,  3.30780053,  3.17735667,  3.03756983,  2.88903983,
        2.73240402,  2.5683345 ,  2.3975353 ,  2.22073931,  2.03870516,
        1.85221396,  1.66206593,  1.46907699,  1.27407525,  1.07789747,
        0.88138542,  0.68538235,  0.4907293 ,  0.29826151,  0.10880487,
       -0.07682768, -0.25783959, -0.43345415, -0.60291779, -0.76550335]

    y = [3.88656062, 4.07229724, 4.25343267, 4.42918964, 4.598814  ,
       4.7615779 , 4.91678291, 5.06376305, 5.20188764, 5.33056399,
       5.44923995, 5.55740628, 5.65459886, 5.74040062, 5.81444339,
       5.87640946, 5.92603293, 5.96310087, 5.98745423, 5.99898849,
       5.99765418, 5.98345701, 5.95645791, 5.91677272, 5.86457174,
       5.80007895, 5.7235711 , 5.63537648, 5.53587353, 5.42548921]
    while not rospy.is_shutdown():
        cartesian_to_path(x,y)
        r.sleep()