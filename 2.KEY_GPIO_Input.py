#-----------------------初始化区---------------------------#
import utime
from Maix import GPIO
from board import board_info
from fpioa_manager import fm

#LED初始化
fm.register(board_info.LED_R, fm.fpioa.GPIO0)
led_r=GPIO(GPIO.GPIO0, GPIO.OUT)
led_r.value(1)

#KEY初始化
fm.register(board_info.ENTER, fm.fpioa.GPIOHS1)
key = GPIO(GPIO.GPIOHS1, GPIO.IN)

#等待100ms进入代码区
utime.sleep_ms(100)
#-----------------------代码区----------------------------#
#进行键值判断
while(True):
    if key.value() == 0: # 等待按键按下
        led_r.value(0)
        utime.sleep_ms(1000) #亮灯1s
        led_r.value(1)

    utime.sleep_ms(10) #10ms判断一次

