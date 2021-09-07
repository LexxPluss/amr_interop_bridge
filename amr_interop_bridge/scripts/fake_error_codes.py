#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from std_msgs.msg import String
from amr_interop_msgs.msg import ErrorCodes
import random

ERROR_CODES = [
    "Robot safety stop based on sensors",
    "Robot stopped",
    "Battery Low",
    "Robot Lost",
    "Robot Stuck",
]

if __name__ == "__main__":
    rospy.init_node("fake_error_codes")
    
    pub = rospy.Publisher("error_codes", ErrorCodes, queue_size=1)
    publish_rate = rospy.get_param("~publish_rate", 1)

    loop_rate = rospy.Rate(publish_rate)
    error_codes_msg = ErrorCodes()
    while not rospy.is_shutdown():
        error_count = random.randint(0, len(ERROR_CODES))
        error_codes_msg.data = random.sample(ERROR_CODES, error_count)
        pub.publish(error_codes_msg)
        loop_rate.sleep()
