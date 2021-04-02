#-----------------------初始化区--------------------------#

import utime
#utime模块提供获取当前时间和日期，测量时间间隔和延迟的功能
from Maix import GPIO
from board import board_info
#board_info用于指定具体的硬件上的引脚分配，如此处LED_R对应14脚
#具体映射关系见//:> 2_初始化程序 > Board_info.py
from fpioa_manager import fm
#fm模块用于注册芯片内部功能和引脚，帮助用户管理内部功能和引脚映射关系的功能模块。

#-----------------------代码区---------------------------#
print(fm.fpioa.get_Pin_num(fm.fpioa.GPIO0))
#显示外设原功能对应
fm.register(board_info.LED_R,fm.fpioa.GPIO0)
#GPIO0与LED_G形成映射
print(fm.fpioa.get_Pin_num(fm.fpioa.GPIO0))
#显示外设设定后功能
led_r=GPIO(GPIO.GPIO0,GPIO.OUT)
#输出信号，点亮灯泡
utime.sleep_ms(1000)
#持续1s
fm.unregister(board_info.LED_R)
#解除映射关系
