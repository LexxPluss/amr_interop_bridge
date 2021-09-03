#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from std_msgs.msg import String

if __name__ == "__main__":
    rospy.init_node("fake_manufacture_name")
    
    pub = rospy.Publisher("manufacture_name", String, queue_size=1)
    manufacture_name = rospy.get_param("~manufacture_name", "LexxPluss, Inc.")
    publish_rate = rospy.get_param("~publish_rate", 1)

    loop_rate = rospy.Rate(publish_rate)
    manufacture_name_msg = manufacture_name
    while not rospy.is_shutdown():
        pub.publish(manufacture_name_msg)
        loop_rate.sleep()
