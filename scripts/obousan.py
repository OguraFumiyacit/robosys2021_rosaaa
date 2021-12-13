#!/usr/bin/env python3
import rospy
#from std_msgs.msg import String
from std_msgs.msg import Int16
def cb(message):
    #rospy.loginfo(message.data)
    f = open('kyoten.txt', 'r')
    if message.data == 0:
        str = f.readlines()[0]
        print(str)
    elif message.data == 1:
        str = f.readlines()[1]
        print(str)


if __name__ == '__main__':
    rospy.init_node('obousan')
    #sub = rospy.Subscriber('input_data', String, cb)
    sub = rospy.Subscriber('input_data', Int16, cb)
    rospy.spin()
