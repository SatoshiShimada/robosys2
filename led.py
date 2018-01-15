#!/usr/bin/env python

import rospy
from std_msgs.msg import Int32
from std_msgs.msg import Int8
import subprocess
import wiringpi

subprocess.check_call('gpio export 16 out', shell=True)
wiringpi.wiringPiSetupSys()

led_pin = 16
OUTPUT = 1
LOW, HIGH = 0, 1
wiringpi.pinMode(led_pin, OUTPUT)
wiringpi.digitalWrite(led_pin, LOW)

def cb(message):
    if message.data != 0:
        rospy.loginfo("detected object: " + str(message.data))
        wiringpi.digitalWrite(led_pin, HIGH)
    else:
        rospy.loginfo("detected object: " + str(message.data) + "LOW")
        wiringpi.digitalWrite(led_pin, LOW)

if __name__ == '__main__':
    rospy.init_node('yolo_led')
    sub = rospy.Subscriber('/darknet_ros/found_object', Int8, cb)
    rospy.spin()

