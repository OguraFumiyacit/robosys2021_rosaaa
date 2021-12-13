#!/usr/bin/env python3
import rospy
#from std_msgs.msg import String
from std_msgs.msg import Int16


rospy.init_node('okyou')
#pub = rospy.Publisher('input_data', String, queue_size=1)
pub = rospy.Publisher('input_data',Int16, queue_size=10)
rate = rospy.Rate(1)
n = 0

while not rospy.is_shutdown():
    #f = open('kyoten.txt', 'r')
    #str = f.readline()
    #if str == '':
    #    break
    #pub.publish(str.rstrip('\n'))
    #f.close()
    msg = Int16()
    msg.data = n
    pub.publish(n)
    n += 1
    if n >= 10:
        n = 0
