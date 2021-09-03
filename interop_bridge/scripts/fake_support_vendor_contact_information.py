#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from std_msgs.msg import String

if __name__ == "__main__":
    rospy.init_node("fake_support_vendor_contact_information")
    
    pub = rospy.Publisher("support_vendor_contact_information", String, queue_size=1)
    support_vendor_contact_information = rospy.get_param("~support_vendor_contact_information", "https://forms.gle/WZVdtsBv3Teg3QnD8")
    publish_rate = rospy.get_param("~publish_rate", 1)

    loop_rate = rospy.Rate(publish_rate)
    support_vendor_contact_information_msg = support_vendor_contact_information
    while not rospy.is_shutdown():
        pub.publish(support_vendor_contact_information_msg)
        loop_rate.sleep()
