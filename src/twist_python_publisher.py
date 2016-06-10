#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
    
def twistPublisher():

    twist_pub = rospy.Publisher('/riss_bot/cmd_vel', Twist, queue_size=10)
    rospy.init_node('twist_publisher', anonymous=False)
    rate = rospy.Rate(1) # 1Hz
    msg = Twist()
    msg.angular.z = 0.02
    while not rospy.is_shutdown():
        twist_pub.publish(msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        twistPublisher()
    except rospy.ROSInterruptException:
        pass
