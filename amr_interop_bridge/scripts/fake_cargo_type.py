#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from std_msgs.msg import String

if __name__ == "__main__":
    rospy.init_node("fake_cargo_type")
    
    pub = rospy.Publisher("cargo_type", String, queue_size=1)
    cargo_type = rospy.get_param("~cargo_type", "basket cart")
    publish_rate = rospy.get_param("~publish_rate", 1)

    loop_rate = rospy.Rate(publish_rate)
    cargo_type_msg = cargo_type
    while not rospy.is_shutdown():
        pub.publish(cargo_type_msg)
        loop_rate.sleep()
