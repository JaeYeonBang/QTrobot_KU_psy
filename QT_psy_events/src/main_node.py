#!/usr/bin/env python
import sys
import rospy
from qt_robot_interface.srv import *
from qt_gesture_controller.srv import *
from synchronizer import TaskSynchronizer
# from emotion_detector import Emotion_detector
if __name__ == '__main__':
    rospy.init_node('psy_event_node')
    rospy.loginfo("psy_event_node started")

   # define a ros service
    talkText = rospy.ServiceProxy('/qt_robot/behavior/talkText', behavior_talk_text)
    gesturePlay = rospy.ServiceProxy('/qt_robot/gesture/play', gesture_play)
    
    # block/wait for ros service
    rospy.wait_for_service('/qt_robot/behavior/talkText')
    rospy.wait_for_service('/qt_robot/gesture/play')

    # ceate an instance of TaskSynchronizer
    ts = TaskSynchronizer()

    #emotion_sub = Emotion_detector()
    # call talkText and gesturePlay at the same time
    # wait until both finish their jobs
    
    
    print('calling talkText and gesturePlay...')
    
    talkText('안녕하세요 제 이름은 큐티에요!')
    gesturePlay('QT/hi', 0)
    
     
    results = ts.sync([
        (0, lambda: talkText('저는 심리학부 소속의 귀염둥이랍니다!')),
        (0, lambda: gesturePlay('QT/happy', 0))
    ])
    talkText("제가 심리학부를 대표해서 심리학부를 소개해 볼게요!")

    results = ts.sync([
        (0, lambda: talkText("국내 최초, 유일 단독의 심리학부 고려대학교 심리학부!")),
        (0, lambda: gesturePlay('QT/one-arm-up', 0))
    ])

    talkText("창의적으로 유연하게 접근할 수 있는 인재 양성을 목표로 하고 있어요")
    talkText("저희 심리학부는 임상 및 상담심리, 행동인지 신경과학, 소비자 및 광고 심리, 문화사회성격심리, 심리데이터과학 등 6개의 세부 전공을 기반으로 하고 있어요.")

    results = ts.sync([
        (0, lambda: talkText('정말 다양하죠?')),
        (0, lambda: gesturePlay('QT/surprise', 0))
    ])
    

    talkText('우수하고 멋진 교수님들과, 문이과를 아우르는 학문을 공부하는 학생들과 함께') 
    results = ts.sync([
        (0, lambda: talkText('저 큐티가 생활하고 있답니다!')),
        (0, lambda: gesturePlay('QT/show_QT', 0))
    ])




