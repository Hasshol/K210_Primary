#摄像头基础
#-----------------------初始化区---------------------------#
import lcd, image ,time, sensor
#-----------------------代码区---------------------------#
sensor.reset()#重置并初始化单目摄像头
sensor.set_pixformat(sensor.YUV422)#等同于RGB565，还有GRAYSCALE、BAYER可选
sensor.set_framesize(sensor.QVGA)#设置分辨率
sensor.skip_frames(time = 2000)#跳帧2s

#镜像与水平翻转
sensor.set_hmirror(1)
sensor.set_vflip(1)

#LCD初始化
lcd.init()

#添加一个计时器
clock = time.clock()

while(True):
    clock.tick()#开始计时
    img = sensor.snapshot()#拍照，数据存入img中
    lcd.display(img)#LCD显示图片
    print(clock.fps())#输出帧率
