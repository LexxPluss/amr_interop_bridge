#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from std_msgs.msg import String

if __name__ == "__main__":
    rospy.init_node("fake_robot_model")
    
    pub = rospy.Publisher("robot_model", String, queue_size=1)
    robot_model = rospy.get_param("~robot_model", "LexxHard")
    publish_rate = rospy.get_param("~publish_rate", 1)

    loop_rate = rospy.Rate(publish_rate)
    robot_model_msg = robot_model
    while not rospy.is_shutdown():
        pub.publish(robot_model_msg)
        loop_rate.sleep()
