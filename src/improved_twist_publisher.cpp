#include "ros/ros.h"
#include "geometry_msgs/Twist.h"
#include "std_msgs/String.h"
#include "string.h"

float xVel;

void highLevelCmdCallback(const std_msgs::String::ConstPtr& msg)
{
  ROS_INFO("Received command: %s", msg->data.c_str());
  
  if( strcmp(msg->data.c_str(), "forward") == 0 )
  {
    xVel = 0.01;
  }
  else if( strcmp(msg->data.c_str(), "backward") == 0 )
  {
    xVel = -0.01;
  }
  else if( strcmp(msg->data.c_str(), "stop" ) == 0 )
  {
    xVel = 0.0;
  }
}

int main(int argc, char **argv)
{

  ros::init(argc, argv, "twist_publisher");
  ros::NodeHandle n;
  ros::Publisher twist_pub = n.advertise<geometry_msgs::Twist>("/riss_bot/cmd_vel", 1);
  ros::Subscriber sub = n.subscribe("/high_level_cmd", 1000, highLevelCmdCallback);

  ros::Rate loop_rate(10);
  
  // initialize xVel
  xVel = 0.0;

  while (ros::ok())
  {
    geometry_msgs::Twist msg;
    msg.linear.x = xVel;
    twist_pub.publish(msg);
    ros::spinOnce();
    loop_rate.sleep();
  }

  return 0;
}
