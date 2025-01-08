#!/usr/bin/env python
import sys
import rospy
from qt_robot_interface.srv import *
from qt_gesture_controller.srv import *
from synchronizer import TaskSynchronizer
# from emotion_detector import Emotion_detector
if __name__ == '__main__':
    rospy.init_node('teaching_event_node')
    rospy.loginfo("teaching_event_node started")

   # define a ros service
    talkText = rospy.ServiceProxy('/qt_robot/behavior/talkText', behavior_talk_text)
    gesturePlay = rospy.ServiceProxy('/qt_robot/gesture/play', gesture_play)
    emotionShow = rospy.ServiceProxy('/qt_robot/emotion/show', emotion_show)
    # block/wait for ros service
    rospy.wait_for_service('/qt_robot/behavior/talkText')
    rospy.wait_for_service('/qt_robot/gesture/play')
    rospy.wait_for_service('/qt_robot/emotion/show')
    # ceate an instance of TaskSynchronizer
    ts = TaskSynchronizer()

    #emotion_sub = Emotion_detector()
    # call talkText and gesturePlay at the same time
    # wait until both finish their jobs
    
    
    print('calling talkText and gesturePlay...')
    talkText("심리학과는 사람들의 심리를 공부하는 학문이에요!")
    talkText("사람들의 심리가 가장 많이 드러나는 곳 중 하나는 바로 표정이죠!")
    talkText("우리 같이 표정에 대해 공부해볼까요??") 
    
    results = ts.sync([
        (0, lambda: talkText('이건 행복한 표정이에요!')),
        (0, lambda: gesturePlay('QT/hi', 0)),
        (0, lambda: emotionShow("QT/happy"))
            ])
    results = ts.sync([
        (0, lambda: talkText('이건 화난 표정이에요!')),
        (0, lambda: gesturePlay('QT/angry', 0)),
        (0, lambda: emotionShow("QT/angry"))
            ])
    results = ts.sync([
            (0, lambda: talkText('이건 슬픈 표정이에요!')),
            (0, lambda: gesturePlay('QT/sad', 0)),
            (0, lambda: emotionShow("QT/cry"))
            ])
    results = ts.sync([
            (0, lambda: talkText('이건 두려운 표정이에요!')),
            (0, lambda: gesturePlay('QT/show_QT', 0)),
            (0, lambda: emotionShow("QT/afraid"))
            ])
    results = ts.sync([
            (0, lambda: talkText('이건 경멸스러운 표정이에요!')),
            (0, lambda: gesturePlay('QT/personal-distance', 0)),
            (0, lambda: emotionShow("QT/disgusted"))
            ])
        
    results = ts.sync([
            (0, lambda: talkText('이건 놀란 표정이에요!')),
            (0, lambda: gesturePlay('QT/surprise', 0)),
            (0, lambda: emotionShow("QT/surprise"))
            ])
    talkText('재밌게 알아보았을까요?')
        
    results = ts.sync([
            (0, lambda: talkText('다음에 더 알아보기로 해요. 안녕!')),
            (0, lambda: gesturePlay('QT/bye-bye', 0)),
            ])   
