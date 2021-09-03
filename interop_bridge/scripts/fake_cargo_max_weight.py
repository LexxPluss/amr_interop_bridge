#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from std_msgs.msg import String

if __name__ == "__main__":
    rospy.init_node("fake_cargo_max_weight")
    
    pub = rospy.Publisher("cargo_max_weight", String, queue_size=1)
    cargo_max_weight = rospy.get_param("~cargo_max_weight", "500")
    publish_rate = rospy.get_param("~publish_rate", 1)

    loop_rate = rospy.Rate(publish_rate)
    cargo_max_weight_msg = str(cargo_max_weight)
    while not rospy.is_shutdown():
        pub.publish(cargo_max_weight_msg)
        loop_rate.sleep()
