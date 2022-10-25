#!/usr/bin/env python
from random import randint    #подключение библиотеки
import rospy
from std_msgs.msg import String,Bool
class roulete:
    def __init__(self):       #задаем соотношение цвета и числа

        self.userInput = ''   #ввод пользователя
        self.publisher = rospy.Publisher('roulet', String, queue_size = 10)
        rospy.init_node('user')
        self.r = rospy.Rate(10)
        self.subsriber = rospy.Subscriber('roulet', Bool, self.callback)

    def start(self):          #добавление вступления
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
        self.publisher.publish(self.userInput)
        self.r.sleep()

    def callback(self, data):
        if data.data:
            rospy.loginfo('Congratulations')
        else:
            rospy.loginfo('Next time will be better')



def main():
    roulet = roulete()
    roulet.start()


if __name__ == '__main__':
    main()


