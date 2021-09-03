#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from std_msgs.msg import String

if __name__ == "__main__":
    rospy.init_node("fake_thumnail_image")
    
    pub = rospy.Publisher("thumnail_image", String, queue_size=1)
    thumnail_image = rospy.get_param("~thumnail_image", "https://storage.googleapis.com/production-os-assets/assets/c776796f-4edf-414a-b518-b3fda6cb6405")

    loop_rate = rospy.Rate(1)
    thumnail_image_msg = thumnail_image
    while not rospy.is_shutdown():
        pub.publish(thumnail_image_msg)
        loop_rate.sleep()
