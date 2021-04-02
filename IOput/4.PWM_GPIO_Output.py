#呼吸灯程序
#By：黄荣辉
#-----------------------初始化区---------------------------#
from machine import Timer,PWM #定时器与PWM特定方法
import time
from board import board_info
from fpioa_manager import fm

#-----------------------代码区----------------------------#
tim = Timer(Timer.TIMER0, Timer.CHANNEL0, mode=Timer.MODE_PWM)
#共有三个定时器，每个定时器有四个通道
channe = PWM(tim, freq=500000, duty=50, pin=board_info.LED_R)
duty=0  #占空比
dir = True

while True:
    if dir:
        duty += 10
    else:
        duty -= 10
    if duty>100:
        duty = 100
        dir = False
    elif duty<0:
        duty = 0
        dir = True
    time.sleep(0.05)
    channe.duty(duty)
