#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from geometry_msgs.msg import Quaternion
from interop_msgs.msg import Location
import uuid

if __name__ == "__main__":
    rospy.init_node("fake_location")
    
    pub = rospy.Publisher("location", Location, queue_size=1)
    x = rospy.get_param("~x", 0.0)
    y = rospy.get_param("~y", 0.0)
    z = rospy.get_param("~z", float("nan"))
    angle_x = rospy.get_param("~angle_x", 0.0)
    angle_y = rospy.get_param("~angle_y", 0.0)
    angle_z = rospy.get_param("~angle_z", 0.0)
    angle_w = rospy.get_param("~angle_w", 1.0)
    publish_rate = rospy.get_param("~publish_rate", 1)
    planar_datum = str(uuid.uuid4())
    
    loop_rate = rospy.Rate(publish_rate)
    location_msg = Location()
    location_msg.x = float(x)
    location_msg.y = float(y)
    location_msg.z = float(z)
    location_msg.angle.x = float(angle_x)
    location_msg.angle.y = float(angle_y)
    location_msg.angle.z = float(angle_z)
    location_msg.angle.w = float(angle_w)
    location_msg.planar_datum = planar_datum
    while not rospy.is_shutdown():
        pub.publish(location_msg)
        loop_rate.sleep()
