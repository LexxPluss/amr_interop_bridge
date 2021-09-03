#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from geometry_msgs.msg import Quaternion
from interop_msgs.msg import Velocity

if __name__ == "__main__":
    rospy.init_node("fake_velocity")
    
    pub = rospy.Publisher("velocity", Velocity, queue_size=1)
    linear = rospy.get_param("~linear", 0.0)
    angular_x = rospy.get_param("~angular_x", float("nan"))
    angular_y = rospy.get_param("~angular_y", float("nan"))
    angular_z = rospy.get_param("~angular_z", float("nan"))
    angular_w = rospy.get_param("~angular_w", float("nan"))
    publish_rate = rospy.get_param("~publish_rate", 1)

    loop_rate = rospy.Rate(publish_rate)
    velocity_msg = Velocity()
    velocity_msg.linear = linear
    velocity_msg.angular = Quaternion()
    velocity_msg.angular.x = angular_x
    velocity_msg.angular.y = angular_y
    velocity_msg.angular.z = angular_z
    velocity_msg.angular.w = angular_w
    while not rospy.is_shutdown():
        pub.publish(velocity_msg)
        loop_rate.sleep()
