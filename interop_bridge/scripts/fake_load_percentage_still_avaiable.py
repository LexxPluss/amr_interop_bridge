#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from std_msgs.msg import Float64
import random

if __name__ == "__main__":
    rospy.init_node("fake_load_percentage_still_avaiable")
    
    pub = rospy.Publisher("load_percentage_still_avaiable", Float64, queue_size=1)
    lower = rospy.get_param("~lower", 0)
    upper = rospy.get_param("~upper", 100)
    publish_rate = rospy.get_param("~publish_rate", 1)

    loop_rate = rospy.Rate(publish_rate)
    while not rospy.is_shutdown():
        load_percentage_still_avaiable_msg = random.uniform(lower, upper)
        pub.publish(load_percentage_still_avaiable_msg)
        loop_rate.sleep()
