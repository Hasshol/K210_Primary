#串口自收发程序（来源于官方资源库）
#-----------------------初始化区---------------------------#
from fpioa_manager import fm
from machine import UART
import time
#-----------------------代码区----------------------------#
# 硬件连接22、8引脚，（硬件引脚，只要是空闲的都可以用，随便改）
fm.register(22, fm.fpioa.UART1_TX, force=True)
fm.register(8, fm.fpioa.UART1_RX, force=True)

uart = UART(UART.UART1, 115200, 8, 1, 0, timeout=1000, read_buf_len=4096)
uart.write('hello world')

while True:
    read_data = uart.read()
    if read_data:
        print("recv:", read_data)
        uart.write(read_data)  # send data back
        print("wait data: ")

#解初始化
uart.deinit()
#注销串口
del uart

