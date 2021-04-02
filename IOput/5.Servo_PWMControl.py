#按键PWM调整程序
#By：黄荣辉
#-----------------------初始化区---------------------------#
from machine import Timer,PWM #定时器与PWM特定方法
import utime
from board import board_info
from fpioa_manager import fm
from Maix import GPIO

#KEY初始化
fm.register(board_info.NEXT, fm.fpioa.GPIOHS1)
up = GPIO(GPIO.GPIOHS1, GPIO.IN, GPIO.PULL_NONE)

fm.register(board_info.BACK, fm.fpioa.GPIOHS2)
down = GPIO(GPIO.GPIOHS2, GPIO.IN, GPIO.PULL_NONE)
duty = 0
#中断服务程序
def Up_irq(pin_num):
    print("key", pin_num, "\n")
    global duty #全局变量
    duty += 10
    if duty>100:
        duty = 100

def Down_irq(pin_num):
    print("key", pin_num, "\n")
    global duty #全局变量
    duty -= 10
    if duty<0:
        duty = 0
#等待100ms进入代码区
utime.sleep_ms(100)
#-----------------------代码区----------------------------#
tim = Timer(Timer.TIMER0, Timer.CHANNEL0, mode=Timer.MODE_PWM)
#共有三个定时器，每个定时器有四个通道
ch = PWM(tim, freq=500000, duty=50, pin=14)
#中断设定
up.irq(Up_irq, GPIO.IRQ_RISING, GPIO.WAKEUP_NOT_SUPPORT,6)
down.irq(Down_irq, GPIO.IRQ_RISING, GPIO.WAKEUP_NOT_SUPPORT,7)

while(True):
    utime.sleep_ms(10)
    ch.duty(duty)
    print(duty)
