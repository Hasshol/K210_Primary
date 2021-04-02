#图像基础1-辅助框添加与缩放
#By：黄荣辉
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
    #画线
    img.draw_line((20, 30, 200, 200))
    img.draw_line((80, 50, 100, 100), color=(255,0,0))
    #画正方形、圆形、十字准星、字符串
    img.draw_rectangle((20, 30, 41, 51), color=(255,0,0))
    img.draw_circle(50, 50, 30)
    img.draw_cross(160,120,size=10)
    img.draw_string(160,136, "hello world!")
    #放大图片以适应屏幕->帧率大幅度降低
    img2=img.resize(480, 320)
    lcd.display(img2)#LCD显示图片
    print(clock.fps())#输出帧率
