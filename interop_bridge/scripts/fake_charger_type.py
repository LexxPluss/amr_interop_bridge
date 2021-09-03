#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from std_msgs.msg import String

if __name__ == "__main__":
    rospy.init_node("fake_charger_type")
    
    pub = rospy.Publisher("charger_type", String, queue_size=1)
    charger_type = rospy.get_param("~charger_type", "LexxHard Charger")
    publish_rate = rospy.get_param("~publish_rate", 1)

    loop_rate = rospy.Rate(publish_rate)
    charger_type_msg = charger_type
    while not rospy.is_shutdown():
        pub.publish(charger_type_msg)
        loop_rate.sleep()
