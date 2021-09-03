#!/usr/bin/env python
# -*- coding: utf-8 -*-

import websocket
try:
    import thread
except ImportError:
    import _thread as thread
import time
import json
import hashlib
import uuid
from datetime import datetime, timedelta
import random
import math
import time
import pytz

import rospy
from std_msgs.msg import String
from std_msgs.msg import Float64
from geometry_msgs.msg import Point
from geometry_msgs.msg import Quaternion
from interop_msgs.msg import Location
from interop_msgs.msg import Velocity
from interop_msgs.msg import ErrorCodes
from interop_msgs.msg import PredictedLocation
from interop_msgs.msg import PredictedLocations


def on_message(ws, message):
    rospy.loginfo(message)

def on_error(ws, error):
    rospy.loginfo(error)

def on_close(ws, close_status_code, close_msg):
    rospy.loginfo("### closed ###")

def on_open(ws):
    def run(*args):
        identity["timestamp"] = datetime.now(pytz.utc).strftime("%Y-%m-%dT%H:%M:%S%z")
        ws.send(json.dumps(identity))
        identity.clear()

        while True:
            status["timestamp"] = datetime.now(pytz.utc).strftime("%Y-%m-%dT%H:%M:%S%z")
            ws.send(json.dumps(status))
            status.clear()
            time.sleep(2)
        ws.close()
    thread.start_new_thread(run, ())

def uuid_callback(msg):
    identity["uuid"] = msg.data
    status["uuid"] = msg.data

def manufacture_name_callback(msg):
    identity["manufacturerName"] = msg.data

def robot_model_callback(msg):
    identity["robotModel"] = msg.data

def robot_serial_number_callback(msg):
    identity["robotSerialNumber"] = msg.data

def base_robot_envelope_callback(msg):
    if "baseRobotEnvelope" not in identity:
        identity["baseRobotEnvelope"] = {}
    
    identity["baseRobotEnvelope"]["x"] = msg.x
    identity["baseRobotEnvelope"]["y"] = msg.y
    if not math.isnan(msg.z):
        identity["baseRobotEnvelope"]["z"] = msg.z

def max_speed_callback(msg):
    identity["maxSpeed"] = msg.data

def max_run_time_callback(msg):
    identity["maxRunTime"] = msg.data

def emergency_contact_information_callback(msg):
    identity["emergencyContactInformation"] = msg.data

def charger_type_callback(msg):
    identity["chargerType"] = msg.data

def support_vendor_name_callback(msg):
    identity["supportVendorName"] = msg.data

def support_vendor_contact_information_callback(msg):
    identity["supportVendorContactInformation"] = msg.data

def product_documentation_callback(msg):
    identity["productDocumentation"] = msg.data

def thumnail_image_callback(msg):
    identity["thumnailImage"] = msg.data

def cargo_type_callback(msg):
    identity["cargoType"] = msg.data

def cargo_max_volume_callback(msg):
    if "cargoMaxVolume" not in identity:
        identity["cargoMaxVolume"] = {}
    
    identity["cargoMaxVolume"]["x"] = msg.x
    identity["cargoMaxVolume"]["y"] = msg.y
    if not math.isnan(msg.z):
        identity["cargoMaxVolume"]["z"] = msg.z

def cargo_max_weight_callback(msg):
    identity["cargoMaxWeight"] = msg.data

def operational_state_callback(msg):
    status["operationalState"] = msg.data

def location_callback(msg):
    if "location" not in identity:
        status["location"] = {}
    
    status["location"]["x"] = msg.x
    status["location"]["y"] = msg.y
    if math.isnan(msg.z):
        status["location"].pop("z", None)
    else:
        status["location"]["z"] = msg.z
    status["location"]["angle"] = {}
    status["location"]["angle"]["x"] = msg.angle.x
    status["location"]["angle"]["y"] = msg.angle.y
    status["location"]["angle"]["z"] = msg.angle.z
    status["location"]["angle"]["w"] = msg.angle.w

    status["location"]["planarDatum"] = msg.planar_datum

def velocity_callback(msg):
    if "velocity" not in identity:
        status["velocity"] = {}
    
    status["velocity"]["linear"] = msg.linear

    if math.isnan(msg.angular.x) or \
       math.isnan(msg.angular.y) or \
       math.isnan(msg.angular.z) or \
       math.isnan(msg.angular.w):
        status["velocity"].pop("angular", None)
    else:
        status["velocity"]["angular"] = {}
        status["velocity"]["angular"]["x"] = msg.angular.x
        status["velocity"]["angular"]["y"] = msg.angular.y
        status["velocity"]["angular"]["z"] = msg.angular.z
        status["velocity"]["angular"]["w"] = msg.angular.w

def battery_percentage_callback(msg):
    status["batteryPercentage"] = msg.data

def remaining_run_time_callback(msg):
    status["remainingRunTime"] = msg.data

def load_percentage_still_avaiable_callback(msg):
    status["loadPercentageStillAvailable"] = msg.data

def error_codes_callback(msg):
    if len(msg.data) > 0:
        status["errorCodes"] = msg.data

def path_callback(msg):
    if len(msg.data) > 0:
        status["path"] = []

        for i in range(len(msg.data)):
            path = {}
            path["timestamp"] = msg.data[i].timestamp
            path["x"] = msg.data[i].x
            path["y"] = msg.data[i].y
            if not math.isnan(msg.data[i].z):
                path["z"] = msg.data[i].z
            path["angle"] = {}
            path["angle"]["x"] = msg.data[i].angle.x
            path["angle"]["y"] = msg.data[i].angle.y
            path["angle"]["z"] = msg.data[i].angle.z
            path["angle"]["w"] = msg.data[i].angle.w
            path["planarDatumUUID"] = msg.data[i].planar_datum_uuid

            status["path"].append(path)

def destinations_callback(msg):
    if len(msg.data) > 0:
        status["destinations"] = []

        for i in range(len(msg.data)):
            path = {}
            path["timestamp"] = msg.data[i].timestamp
            path["x"] = msg.data[i].x
            path["y"] = msg.data[i].y
            if not math.isnan(msg.data[i].z):
                path["z"] = msg.data[i].z
            path["angle"] = {}
            path["angle"]["x"] = msg.data[i].angle.x
            path["angle"]["y"] = msg.data[i].angle.y
            path["angle"]["z"] = msg.data[i].angle.z
            path["angle"]["w"] = msg.data[i].angle.w
            path["planarDatumUUID"] = msg.data[i].planar_datum_uuid

            status["destinations"].append(path)

if __name__ == "__main__":
    rospy.init_node("interop_bridge")

    url = rospy.get_param("~url", "ws://localhost/")

    identity = {}
    status = {}

    rospy.Subscriber("uuid", String, uuid_callback)
    rospy.Subscriber("manufacture_name", String, manufacture_name_callback)
    rospy.Subscriber("robot_model", String, robot_model_callback)
    rospy.Subscriber("robot_serial_number", String, robot_serial_number_callback)
    rospy.Subscriber("base_robot_envelope", Point, base_robot_envelope_callback)
    rospy.Subscriber("max_speed", Float64, max_speed_callback)
    rospy.Subscriber("max_run_time", Float64, max_run_time_callback)
    rospy.Subscriber("emergency_contact_information", String, emergency_contact_information_callback)
    rospy.Subscriber("charger_type", String, charger_type_callback)
    rospy.Subscriber("support_vendor_name", String, support_vendor_name_callback)
    rospy.Subscriber("support_vendor_contact_information", String, support_vendor_contact_information_callback)
    rospy.Subscriber("product_documentation", String, product_documentation_callback)
    rospy.Subscriber("thumnail_image", String, thumnail_image_callback)
    rospy.Subscriber("cargo_type", String, cargo_type_callback)
    rospy.Subscriber("cargo_max_volume", Point, cargo_max_volume_callback)
    rospy.Subscriber("cargo_max_weight", String, cargo_max_weight_callback)

    rospy.Subscriber("operational_state", String, operational_state_callback)
    rospy.Subscriber("location", Location, location_callback)
    rospy.Subscriber("velocity", Velocity, velocity_callback)
    rospy.Subscriber("battery_percentage", Float64, battery_percentage_callback)
    rospy.Subscriber("remaining_run_time", Float64, remaining_run_time_callback)
    rospy.Subscriber("load_percentage_still_avaiable", Float64, load_percentage_still_avaiable_callback)
    rospy.Subscriber("error_codes", ErrorCodes, error_codes_callback)
    rospy.Subscriber("path", PredictedLocations, path_callback)
    rospy.Subscriber("destinations", PredictedLocations, destinations_callback)

    time.sleep(5) # wait subscribe

    ws = websocket.WebSocketApp(url,
                              on_open=on_open,
                              on_message=on_message,
                              on_error=on_error,
                              on_close=on_close)

    ws.run_forever()
