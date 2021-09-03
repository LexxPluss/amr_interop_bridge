#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from std_msgs.msg import String
import uuid

if __name__ == "__main__":
    rospy.init_node("fake_uuid")
    
    pub = rospy.Publisher("uuid", String, queue_size=1)
    publish_rate = rospy.get_param("~publish_rate", 1)

    loop_rate = rospy.Rate(publish_rate)
    uuid_msg = str(uuid.uuid4())
    while not rospy.is_shutdown():
        pub.publish(uuid_msg)
        loop_rate.sleep()
