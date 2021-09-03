#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from std_msgs.msg import String

if __name__ == "__main__":
    rospy.init_node("fake_product_documentation")
    
    pub = rospy.Publisher("product_documentation", String, queue_size=1)
    product_documentation = rospy.get_param("~product_documentation", "https://lexxpluss.com/")
    publish_rate = rospy.get_param("~publish_rate", 1)

    loop_rate = rospy.Rate(publish_rate)
    product_documentation_msg = product_documentation
    while not rospy.is_shutdown():
        pub.publish(product_documentation_msg)
        loop_rate.sleep()
