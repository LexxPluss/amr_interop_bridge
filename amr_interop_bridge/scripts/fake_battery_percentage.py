#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from std_msgs.msg import Float64

if __name__ == "__main__":
    rospy.init_node("fake_battery_percentage")
    
    pub = rospy.Publisher("battery_percentage", Float64, queue_size=1)
    battery_percentage = rospy.get_param("~battery_percentage", 100)
    publish_rate = rospy.get_param("~publish_rate", 1)

    loop_rate = rospy.Rate(publish_rate)
    while not rospy.is_shutdown():
        battery_percentage -= 0.1
        if battery_percentage < 0:
            battery_percentage = 0
        battery_percentage_msg = battery_percentage
        pub.publish(battery_percentage_msg)
        loop_rate.sleep()
