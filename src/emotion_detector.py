#!/usr/bin/env python
import sys
import rospy
from std_msgs.msg import String
from qt_nuitrack_app.msg import Faces
from qt_robot_interface.srv import *


def face_callback(msg):
    emotions = [msg.faces[0].emotion_angry, msg.faces[0].emotion_happy, msg.faces[0].emotion_surprise]
    em = max(emotions)
    em_index = emotions.index(em)
    if em_index == 0 and em >= 0.8:
        speech_pub.publish("화난 표정을 잘 지어주셨군요!! 저도 한번 지어볼게요!")
        emotionShow("QT/angry")
        rospy.sleep(2)
    elif em_index == 1 and em >= 0.8:
        speech_pub.publish("행복한 표정을 잘 지어주셨군요!! 저도 한번 지어볼게요!")
        emotionShow("QT/happy")
        rospy.sleep(2)
    elif em_index == 2 and em >= 0.8:
        speech_pub.publish("놀란 표정을 잘 지어주셨군요!! 저도 한번 지어볼게요!!")
        emotionShow("QT/surprise")
        rospy.sleep(2)
    
    
if __name__ == '__main__':
    rospy.init_node('my_tutorial_node')
    rospy.loginfo("my_tutorial_node started!")
    
    talkText = rospy.ServiceProxy('/qt_robot/behavior/talkText', behavior_talk_text)
    emotionShow = rospy.ServiceProxy('/qt_robot/emotion/show', emotion_show)
    
    rospy.wait_for_service('/qt_robot/behavior/talkText')
    speech_pub = rospy.Publisher('/qt_robot/speech/say', String, queue_size=1)
    talkText("그러면 우리 함께 배웠던 표정들을 함께 연습하는 시간을 가져볼까요?")
    
    talkText("다양한 표정을 지어주세요!")
    # define ros subscriber
    rospy.Subscriber('/qt_nuitrack_app/faces', Faces, face_callback)
   
    try:
        rospy.sleep(40)

    except KeyboardInterrupt:
        pass
    
    speech_pub.publish("큐티와 행복한 시간을 보내셨나요? 우리 함께 행복한 표정을 많이 지어요!")
    rospy.loginfo("finsihed!")
