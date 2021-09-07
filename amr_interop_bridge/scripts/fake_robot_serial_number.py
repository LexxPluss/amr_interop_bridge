#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from std_msgs.msg import String

if __name__ == "__main__":
    rospy.init_node("fake_robot_serial_number")
    
    pub = rospy.Publisher("robot_serial_number", String, queue_size=1)
    robot_serial_number = rospy.get_param("~robot_serial_number", "0000001")
    publish_rate = rospy.get_param("~publish_rate", 1)

    loop_rate = rospy.Rate(publish_rate)
    robot_serial_number_msg = str(robot_serial_number)
    while not rospy.is_shutdown():
        pub.publish(robot_serial_number_msg)
        loop_rate.sleep()
