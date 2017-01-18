#!/usr/bin/env python
import roslib, rospy
from std_msgs.msg import String

def start():
	rospy.init_node("motion_analysis_conf")
	keypress_topic = rospy.get_param("motion_analysis/configuration_keypress_topic", "motion_analysis/configuration/keypress")
	publisher = rospy.Publisher(keypress_topic, String, queue_size=10)
	while not rospy.is_shutdown():
		print " 'q' for STANDING_PERSON_HEIGHT upwards "
		print" 'a' for STANDING_PERSON_HEIGHT downwards "
		print " 'w' for OUTOFBED_LEFT to the left "
	        print " 'e' for OUTOFBED_LEFT to the right "
        	print " 'o' for OUTOFBED_RIGHT to the left "
        	print " 'p' for OUTOFBED_RIGHT to the right"
        	print " 'x' for CUPX to the left "
        	print " 'v' for CUPX to the right "
        	print " 'd' for CUPY upwards "
        	print " 'c' for CUPY downwards "
        	print " 'g' for CUPR increase "
        	print " 'b' for CUPR decrease "

		com = raw_input()
		publisher.publish(str(com))


if __name__ == '__main__':
	start()
