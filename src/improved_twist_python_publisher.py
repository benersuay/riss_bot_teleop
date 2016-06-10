#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import String

xVel = 0.0
twist_pub = rospy.Publisher('/riss_bot/cmd_vel', Twist, queue_size=10)
twistMsg = Twist()

def highLevelCmdCallback(stringMsg):

    rospy.loginfo("Received command %s", stringMsg.data)

    if(stringMsg.data == "forward"):
        xVel = 0.01;
    elif(stringMsg.data == "backward"):
        xVel = -0.01;
    elif(stringMsg.data == "stop"):
        xVel = 0.0;

    twistMsg.linear.x = xVel
    twist_pub.publish(twistMsg)
    
def highLevelCmdSubscriber():
    rospy.init_node('twist_publisher', anonymous=False)
    rospy.Subscriber("/high_level_cmd", String, highLevelCmdCallback)
    rospy.spin()

if __name__ == '__main__':
    highLevelCmdSubscriber()
