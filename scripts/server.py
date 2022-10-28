#!/usr/bin/env python
from random import randint  # подключение библиотеки
import rospy
from std_msgs.msg import String
from roulet.srv import userInfo, userInfoResponse

class server:
    def __init__(self):
        self.mask = {0: 'g', 32: 'r', 15: 'b', 19: 'r', 4: 'b', 21: 'r', 2: 'b', 25: 'r', 17: 'b', 34: 'r', 6: 'b',
                     27: 'r', 13: 'b', 36: 'r', 11: 'b', 30: 'r', 8: 'b', 23: 'r', 10: 'b', 5: 'r', 24: 'b', 16: 'r',
                     33: 'b', 1: 'r', 20: 'b', 14: 'r', 31: 'b', 9: 'r', 22: 'b', 18: 'r', 29: 'b', 7: 'r', 28: 'b',
                     12: 'r', 35: 'b', 3: 'r', 26: 'b'}
        self.s = rospy.Service('userInfo', userInfo, self.callback)
        rospy.init_node('server')
        self.r = rospy.Rate(10)
        rospy.spin()

    def callback(self, req):
        number = randint(0, 37)
        color = self.mask[number]
        rospy.loginfo(str(number) + color)
        rospy.loginfo(req.userInput)
        try:
            user = int(req.userInput)
            if user == number:
                return userInfoResponse('win')
            else:
                return userInfoResponse('lose')
        except ValueError:
            user = req.userInput
            if user == color:
                return userInfoResponse('win')
            else:
                return userInfoResponse('lose')
            


if __name__ == '__main__':
    print('started')
    rospy.loginfo('started')
    server = server()
