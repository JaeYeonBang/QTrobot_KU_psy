#!/usr/bin/env python
import sys
import rospy

if __name__ == '__main__':
    rospy.init_node('psy_event_node')
    rospy.loginfo("psy_event_node started!")

    try:
        rospy.spin()
    except KeyboardInterrupt:
        pass

    rospy.loginfo("finsihed!")
