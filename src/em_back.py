#!/usr/bin/env python

import sys
import rospy
from std_msgs.msg import String
from qt_nuitrack_app.msg import Faces
from qt_robot_interface.srv import *

class callback_counter:

    def __init__(self):
        self.count = 0
        self.subscriber = rospy.Subscriber('/qt_nuitrack_app/faces', Faces, self.face_callback_angry,queue_size=1)

        self.timer = rospy.Timer(rospy.Duration(5), self.change_angry_to_surprise, oneshot=True)

    def face_callback_angry(self,msg):
        emotions = [msg.faces[0].emotion_angry, msg.faces[0].emotion_happy, msg.faces[0].emotion_surprise]
        em = max(emotions)
        em_index = emotions.index(em)
        if em_index == 0 and em >= 0.0:
            print("angry detected")
            self.count +=1
            self.timer.shutdown()
            self.subscriber.unregister()
            talkText("화난 표정을 잘 지어주셨군요!! 저도 한번 지어볼게요!")
            emotionShow("QT/angry")
            rospy.sleep(2)
            self.change_angry_to_surprise()



    def face_callback_happy(self,msg):
        emotions = [msg.faces[0].emotion_angry, msg.faces[0].emotion_happy, msg.faces[0].emotion_surprise]
        em = max(emotions)
        em_index = emotions.index(em)
        if em_index == 1 and em >= 0.5:
            
            print("happy detected")
            self.count +=1
            self.timer.shutdown()
            self.subscriber.unregister()
            talkText("행복한 표정을 잘 지어주셨군요!! 저도 한번 지어볼게요!")
            emotionShow("QT/happy")
            rospy.sleep(2)
            self.change_surprise_to_happy()


    def face_callback_surprising(self, msg):
        emotions = [msg.faces[0].emotion_angry, msg.faces[0].emotion_happy, msg.faces[0].emotion_surprise]
        em = max(emotions)
        em_index = emotions.index(em)
        if em_index == 2 and em >= 0.5:
            
            print("sur detected")
            self.count +=1
            self.timer.shutdown()
            self.subscriber.unregister()
            talkText("놀란 표정을 잘 지어주셨군요!! 저도 한번 지어볼게요!!")
            emotionShow("QT/surprise")
            rospy.sleep(2)

    def change_angry_to_surprise(self,event=None):
        if self.subscriber:
            self.subscriber.unregister

        if self.count == 0:
            talkText("화난 표정을 확인하지 못했어요..")
        
            print("not agry")
        self.count = 0
        print("change to sur")
        self.subscriber = rospy.Subscriber('/qt_nuitrack_app/faces', Faces, self.face_callback_surprising, queue_size=1)
        talkText("이번엔 한번 놀라운 표정을 지어보세요!! ")
        self.timer = rospy.Timer(rospy.Duration(5),self.change_surprise_to_happy, oneshot=True)

    def change_surprise_to_happy(self, event=None):
        if self.subscriber:
            self.subscriber.unregister

        if self.count == 0:
            talkText("놀란 표정을 확인하지 못했어요..")
        self.count = 0
        self.subscriber = rospy.Subscriber('/qt_nuitrack_app/faces', Faces, self.face_callback_happy, queue_size=1)
        talkText("제가 제일 좋아하는 표정은 행복한 표정이에요. 한번 행복한 표정을 지어보세요!! ")
        self.timer = rospy.Timer(rospy.Duration(5), self.change_exit, oneshot=True)

    def change_exit(self, event=None):
        if self.subscriber:
            self.subscriber.unregister
        if self.count == 0:
            talkText("행복한 표정을 확인하지 못했어요..")

        talkText("큐티와 행복한 시간을 보내셨나요? 우리 함께 행복한 표정을 많이 지어요!")
        rospy.loginfo("finsihed!")
        rospy.signal_shutdown("Ending Node")

if __name__ == '__main__':
    
    rospy.init_node('Face_recognition_node')
    rospy.loginfo("Face_recognition_node started!")
    #rate = rospy.Rate(10)
    emotionShow = rospy.ServiceProxy('/qt_robot/emotion/show', emotion_show)


    talkText = rospy.ServiceProxy('/qt_robot/behavior/talkText', behavior_talk_text)
    rospy.wait_for_service('/qt_robot/behavior/talkText')
    rospy.wait_for_service('/qt_robot/gesture/play')
    talkText("그러면 우리 함께 배웠던 표정들을 함께 연습하는 시간을 가져볼까요?")
    talkText("한번 화난 표정을 지어보세요!")

    #rate.sleep()
    callback_counter = callback_counter()

    try:
        rospy.spin()
    except KeyboardInterrupt:
        pass
    # define ros subscriber

    #talkText("큐티와 행복한 시간을 보내셨나요? 우리 함께 행복한 표정을 많이 지어요!")
    #rospy.loginfo("finsihed!")
