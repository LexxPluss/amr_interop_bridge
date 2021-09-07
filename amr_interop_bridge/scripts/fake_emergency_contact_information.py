#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from std_msgs.msg import String

if __name__ == "__main__":
    rospy.init_node("fake_emergency_contact_information")
    
    pub = rospy.Publisher("emergency_contact_information", String, queue_size=1)
    emergency_contact_information = rospy.get_param("~emergency_contact_information", "+81 XX-XXXX-XXXX")
    publish_rate = rospy.get_param("~publish_rate", 1)

    loop_rate = rospy.Rate(publish_rate)
    emergency_contact_information_msg = emergency_contact_information
    while not rospy.is_shutdown():
        pub.publish(emergency_contact_information_msg)
        loop_rate.sleep()
