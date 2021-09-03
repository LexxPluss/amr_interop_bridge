#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from std_msgs.msg import String
import random

OPERATIONAL_STATES = [
    "navigating",
    "idle",
    "disabled",
    "offline",
    "charging",
    "waitingHumanEvent",
    "waitingExternalEvent",
    "waitingInternalEvent",
    "manualOverride"
]

if __name__ == "__main__":
    rospy.init_node("fake_operational_state")
    
    pub = rospy.Publisher("operational_state", String, queue_size=1)
    publish_rate = rospy.get_param("~publish_rate", 1)

    loop_rate = rospy.Rate(publish_rate)
    while not rospy.is_shutdown():
        operational_state_msg = random.choice(OPERATIONAL_STATES)
        pub.publish(operational_state_msg)
        loop_rate.sleep()
