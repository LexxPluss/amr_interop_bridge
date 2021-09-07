#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from geometry_msgs.msg import Point

if __name__ == "__main__":
    rospy.init_node("fake_base_robot_envelope")
    
    pub = rospy.Publisher("base_robot_envelope", Point, queue_size=1)
    x = rospy.get_param("~x", 0.6)
    y = rospy.get_param("~y", 0.6)
    z = rospy.get_param("~z", float("nan"))
    publish_rate = rospy.get_param("~publish_rate", 1)

    loop_rate = rospy.Rate(publish_rate)
    base_robot_envelope_msg = Point()
    base_robot_envelope_msg.x = float(x)
    base_robot_envelope_msg.y = float(y)
    base_robot_envelope_msg.z = float(z)
    while not rospy.is_shutdown():
        pub.publish(base_robot_envelope_msg)
        loop_rate.sleep()
