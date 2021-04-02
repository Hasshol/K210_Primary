#-----------------------初始化区---------------------------#
import utime
from Maix import GPIO
from board import board_info
from fpioa_manager import fm
ans1 = False
#LED初始化
fm.register(board_info.LED_R, fm.fpioa.GPIO0)
led_r=GPIO(GPIO.GPIO0, GPIO.OUT)
led_r.value(1)

#KEY初始化
fm.register(board_info.ENTER, fm.fpioa.GPIOHS1)
key = GPIO(GPIO.GPIOHS1, GPIO.IN, GPIO.PULL_NONE)

#中断服务程序
def Key_irq(pin_num):
    print("key", pin_num, "\n")
    global ans1 #全局变量
    ans1 = not ans1
    led_r.value(ans1)

#等待100ms进入代码区
utime.sleep_ms(100)
#-----------------------代码区----------------------------#

#中断设定
key.irq(Key_irq, GPIO.IRQ_RISING, GPIO.WAKEUP_NOT_SUPPORT,7)
#回调函数名、触发模式、默认、中断优先级

#死循环
while(True):
    utime.sleep_ms(10)

# 禁用中断代码(拓展)
#key.disirq()
#fm.unregister(board_info.ENTER,fm.fpioa.GPIOHS0)
