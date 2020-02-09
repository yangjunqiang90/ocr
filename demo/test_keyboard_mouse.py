#-*- coding: UTF-8 -*-
import sys
import optparse
import time

from pymouse import PyMouse
from pykeyboard import PyKeyboard

if __name__ == '__main__':
    m = PyMouse()
    k = PyKeyboard()
    x,y=m.position()#获取当前坐标的位置
    print 'x=',x,'y=',y
   # m.move(812,58+10)#鼠标移动到xy位置
    m.click(477,345,1,1)#移动并且在xy位置点击
    #time.sleep(5)
    k.type_string('600004')#键盘输入字符串
   # k.tap_key(k.enter_key)#按下回车键
#    k.press_keys([k.alt_key, 'a']) 


#m.click(x,y,1|2,2)#移动并且在xy位置点击，左右键点击(1代表左键，2代表右键),点击次数
#k.tap_key(k.right_key)#按下方向键右键
