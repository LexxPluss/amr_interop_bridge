#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from std_msgs.msg import Float64

if __name__ == "__main__":
    rospy.init_node("fake_max_speed")
    
    pub = rospy.Publisher("max_speed", Float64, queue_size=1)
    max_speed = rospy.get_param("~max_speed", 2.0)
    publish_rate = rospy.get_param("~publish_rate", 1)

    loop_rate = rospy.Rate(publish_rate)
    max_speed_msg = max_speed
    while not rospy.is_shutdown():
        pub.publish(max_speed_msg)
        loop_rate.sleep()
