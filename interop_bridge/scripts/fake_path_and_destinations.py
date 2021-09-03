#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Quaternion
from interop_msgs.msg import PredictedLocation
from interop_msgs.msg import PredictedLocations
import random
import uuid
from datetime import datetime, timedelta
import pytz

if __name__ == "__main__":
    rospy.init_node("fake_path_and_destinations")
    
    path_pub = rospy.Publisher("path", PredictedLocations, queue_size=1)
    destinations_pub = rospy.Publisher("destinations", PredictedLocations, queue_size=1)
    path_lower = rospy.get_param("~path_lower", 0)
    path_upper = rospy.get_param("~path_lower", 10)
    max_seconds = rospy.get_param("~max_minites", 15*60)
    publish_rate = rospy.get_param("~publish_rate", 1)

    loop_rate = rospy.Rate(publish_rate)

    path_msg = PredictedLocations()
    destinations_msg = PredictedLocations()

    x = 0
    y = 0
    while not rospy.is_shutdown():
        # make path
        path_count = random.randint(path_lower, path_upper)
        time_deltas = [random.randint(1, max_seconds/path_count) for i in range(path_count)]

        # path_msg.data.clear()
        path_msg = PredictedLocations()
        nowDt = datetime.now(pytz.utc)
        past_seconds = 0
        for i in range(path_count):
            predicted_location = PredictedLocation()
            predicted_location.timestamp = (nowDt+timedelta(seconds=(time_deltas[i]+past_seconds))).strftime("%Y-%m-%dT%H:%M:%S%z")
            predicted_location.x = x
            predicted_location.y = y
            predicted_location.z = float("nan")
            predicted_location.angle = Quaternion()
            predicted_location.angle.x = random.random()
            predicted_location.angle.y = random.random()
            predicted_location.angle.z = random.random()
            predicted_location.angle.w = random.random()
            predicted_location.planar_datum_uuid = str(uuid.uuid4())
            
            path_msg.data.append(predicted_location)
            
            x = x + random.random()
            y = y + random.random()
            past_seconds = past_seconds + time_deltas[i]

        # choice dest
        destinations_count = random.randint(0, path_count)
        destinations_indexes = random.sample(range(path_count), destinations_count)
        destinations_msg = PredictedLocations()
        for i in range(destinations_count):
            destinations_msg.data.append(path_msg.data[destinations_indexes[i]])

        path_pub.publish(path_msg)
        destinations_pub.publish(destinations_msg)
        loop_rate.sleep()
