#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from geometry_msgs.msg import Point

if __name__ == "__main__":
    rospy.init_node("fake_cargo_max_volume")
    
    pub = rospy.Publisher("cargo_max_volume", Point, queue_size=1)
    x = rospy.get_param("~x", 0.1)
    y = rospy.get_param("~y", 0.2)
    z = rospy.get_param("~z", float("nan"))
    publish_rate = rospy.get_param("~publish_rate", 1)

    loop_rate = rospy.Rate(publish_rate)
    cargo_max_volume_msg = Point()
    cargo_max_volume_msg.x = float(x)
    cargo_max_volume_msg.y = float(y)
    cargo_max_volume_msg.z = float(z)
    while not rospy.is_shutdown():
        pub.publish(cargo_max_volume_msg)
        loop_rate.sleep()
