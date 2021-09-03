#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from std_msgs.msg import Float64

if __name__ == "__main__":
    rospy.init_node("fake_max_run_time")
    
    pub = rospy.Publisher("max_run_time", Float64, queue_size=1)
    max_run_time = rospy.get_param("~max_run_time", 8.0)
    publish_rate = rospy.get_param("~publish_rate", 1)

    loop_rate = rospy.Rate(publish_rate)
    max_run_time_msg = max_run_time
    while not rospy.is_shutdown():
        pub.publish(max_run_time_msg)
        loop_rate.sleep()
