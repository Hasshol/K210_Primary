#图像基础2-边缘查找，锐化，浮雕化（来源于官方例程）
#By：黄荣辉
#-----------------------初始化区---------------------------#
import lcd, image ,time, sensor
#-----------------------代码区---------------------------#
sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.run(1)

#阈值设置
origin = (0,0,0, 0,1,0, 0,0,0)
edge = (-1,-1,-1,-1,8,-1,-1,-1,-1)
sharp = (-1,-1,-1,-1,9,-1,-1,-1,-1)
relievo = (2,0,0,0,-1,0,0,0,-1)

#镜像与水平翻转
sensor.set_hmirror(1)
sensor.set_vflip(1)

lcd.init()
tim = time.time()
while True:
    img=sensor.snapshot()
    img.conv3(edge)
    lcd.display(img)
    if time.time() -tim >10:
        break
tim = time.time()

while True:
    img=sensor.snapshot()
    img.conv3(sharp)
    lcd.display(img)
    if time.time() -tim >10:
        break
tim = time.time()

while True:
    img=sensor.snapshot()
    img.conv3(relievo)
    lcd.display(img)
    if time.time() -tim >10:
        break

lcd.clear()
