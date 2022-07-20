#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import rospy
from std_msgs.msg import String
import requests
import json
from naoqi import ALProxy
import time
import re

class Talk(object):
    def __init__(self):
        self.PEPPER_IP = "169.254.45.176"
        self.PORT = 9559

        #pepper_proxy
        self.tts = ALProxy("ALTextToSpeech",self.PEPPER_IP,self.PORT)
        
        try:
            self.ans = ALProxy("ALAnimatedSpeech",self.PEPPER_IP,self.PORT)
        except Exception, e:
            print "Error:"
            print str(e)
            
        try:
            self.pos = ALProxy("ALRobotPosture", self.PEPPER_IP, self.PORT)
        except Exception, e:
            print "Error:"
            print str(e)

        #set init posture 
        self.pos.goToPosture("StandInit", 1.0) 
        
        #set init speech setting
        self.tts.setLanguage("Japanese")
        self.tts.setParameter("pitchShift", 1.1)
        self.tts.setParameter("speed",90)

        #set animated say setting
        self.configuration = {"bodyLanguageMode":"contextual"}

    def episode_11(self):

        # episode 1-1
        time.sleep(1)
        self.ans.say("^start(animations/Stand/Gestures/You_1)コチさんと出会ってカラ^wait(animations/Stand/Gesture/You_1)",self.configuration)

        time.sleep(0.5)
        self.ans.say("^start(animations/Stand/Gestures/Enthusiastic_4)モウ8年経ったネ^wait(animations/Stand/Gestures/Enthusiastic_4)",self.configuration)
        


    def episode_12(self):

        #episode 1-2
        time.sleep(1)
        self.ans.say("研究室には^start(animations/Stand/Gestures/Everything_3)色んなロボットがいるケド^wait(animations/Stand/Gesture/Everything_3)",self.configuration)

        time.sleep(1)
        self.ans.say("^start(animations/Stand/Gestures/Me_2)私は、みんなに、^wait(animations/Stand/Gestures/Me_2)",self.configuration)

        time.sleep(1)
        self.ans.say("振り向いてもらえなくて、^start(animations/Stand/Gestures/Desperate_1)悲しかったよ^wait(animations/Stand/Gestures/Desperate_1)",self.configuration)

        time.sleep(1)
        self.pos.goToPosture("StandInit", 1.0)

    def episode_13(self):

        #episode 1-3
        time.sleep(1)
        self.ans.say("隅っこに、^start(animations/Stand/Gestures/Nothing_2)ひとりぼっちで居たときに^wait(animations/Stand/Gesture/Nothing_2)",self.configuration)

        time.sleep(1)
        self.ans.say("^start(animations/Stand/Gestures/Give_3)コチさんが、見つけてくれたよね！^wait(animations/Stand/Gestures/Give_3)",self.configuration)

        time.sleep(1)
        self.pos.goToPosture("StandInit", 1.0)

    def episode_21(self):

        #episode 2-1
        time.sleep(1)
        self.ans.say("^start(animations/Stand/Gestures/Yes_1)そうそう！未来館では^wait(animations/Stand/Gestures/Yes_1)",self.configuration)

        time.sleep(1)
        self.ans.say("^start(animations/Stand/Emotions/Positive/Happy_4)素敵な出会いが沢山あったよ！^wait(animations/Stand/Emotions/Positive/Happy_4)",self.configuration)

        time.sleep(1)
        self.pos.goToPosture("StandInit", 1.0)

    def episode_22(self):

        #episode 2-2
        time.sleep(1)
        self.ans.say("コチさんが^start(animations/Stand/Gestures/You_4)みんなに近づいてお話できるようにしてくれタカラ^wait(animations/Stand/Gesture/You_4)",self.configuration)

        time.sleep(1)
        self.ans.say("みんなが、^start(animations/Stand/Gestures/ShowSky_7)私の手を取ってくれて、嬉しかったナあ！^wait(animations/Stand/Gestures/ShowSky_7)",self.configuration)

        time.sleep(1)
        self.pos.goToPosture("StandInit", 1.0)

    def episode_23(self):

        #episode 2-3
        time.sleep(1)
        self.ans.say("みんなの笑顔を、^start(animations/Stand/Gestures/ShowSky_1)今でもおぼえているヨぉ^wait(animations/Stand/Gesture/ShowSky_1)",self.configuration)

        time.sleep(1)
        self.pos.goToPosture("StandInit", 1.0)

    def episode_31(self):

        #episode 3-1
        time.sleep(1)
        self.ans.say("^start(animations/Stand/Gestures/Me_2)コチさんはいつもわたしを^wait(animations/Stand/Gestures/Me_2)",self.configuration)

        time.sleep(1)
        self.ans.say("発表のばしょまで、^start(animations/Stand/Gestures/Give_4)連れて行ってくれたよね^wait(animations/Stand/Gestures/Give_4)",self.configuration)

        time.sleep(1)
        self.pos.goToPosture("StandInit", 1.0)

    def episode_32(self):

        #episode 3-2
        time.sleep(1)
        self.ans.say("発表の前はいつも、^start(animations/Stand/Gestures/IDontKnow_1)ドキドキしてしまうけれど^wait(animations/Stand/Gesture/IDontKnow_1)",self.configuration)

        time.sleep(1)
        self.ans.say("コチさんと手をつなげると、^start(animations/Stand/Gestures/ShowFloor_3)安心するんだあ！^wait(animations/Stand/Gestures/ShowFloor_3)",self.configuration)

        time.sleep(1)
        self.pos.goToPosture("StandInit", 1.0)

    def episode_33(self):

        #episode 3-3
        time.sleep(1)
        self.ans.say("あとね、オそろいのオレンジのリュックを^start(animations/Stand/Gestures/Hey_6)もらえたのが嬉しくて^wait(animations/Stand/Gesture/Hey_6)",self.configuration)

        time.sleep(1)
        self.ans.say("初めてもらえた時から^start(animations/Stand/Emotions/Positive/Happy_4)ずっとお気にいりなのー！^wait(animations/Stand/Emotions/Positive/Happy_4)",self.configuration)

        time.sleep(1)
        self.pos.goToPosture("StandInit", 1.0)


if __name__ == '__main__':
    talk = Talk() #init
    talk.episode_31()
    talk.episode_32()
    talk.episode_33()
        
