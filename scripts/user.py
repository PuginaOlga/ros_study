#!/usr/bin/env python
from random import randint    #подключение библиотеки
import rospy
from std_msgs.msg import String
from roulet.srv import userInfo
class roulete:
    def __init__(self):       #задаем соотношение цвета и числа

        self.userInput = ''   #ввод пользователя
        self.publisher = rospy.Publisher('roulet', String, queue_size = 10)
        rospy.init_node('user')
        self.r = rospy.Rate(10)
        rospy.wait_for_service('userInfo')
        try:
            self.s = rospy.ServiceProxy('userInfo', userInfo)

        except rospy.ServiceException:
            print('failed to connect to to service')

    def start(self):
        while True:
            self.Input()

    def Input(self):
        userInput = input()
        try:
            buf = int(userInput)
            if buf < 0 or buf > 36: #выявление ошибки
                raise Exception("Число не удовлетворяет условию задачи")
            self.userInput = str(userInput)
        except ValueError:          #
            userInput = userInput.lower() #выявление ввода пользователем числа
            letter = userInput[0]
            mask = ['r','b', 'g', 'z']  #z = zero
            if letter not in mask:
                raise Exception("Неправильный цвет")
            self.userInput = letter
        response = self.s(self.userInput)
        if response.response == 'win':
            rospy.loginfo('Congratulations')
        else:
            rospy.loginfo('Next time will be better')
        self.r.sleep()





def main():
    roulet = roulete()
    roulet.start()


if __name__ == '__main__':
    print('started')
    rospy.loginfo('started')
    main()
