#找色块-(官方例程修改)
#-----------------------初始化区---------------------------#
import lcd, image ,time, sensor

green_threshold = (0,80,-70,-10,-0,30)
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
    blobs = img.find_blobs([green_threshold])
    if blobs:
        for b in blobs:
            tmp=img.draw_rectangle(b[0:4])
            tmp=img.draw_cross(b[5], b[6])
            c=img.get_pixel(b[5], b[6])
#blob.x() 返回色块的外框的x坐标（int），也可以通过blob[0]来获取。
#blob.y() 返回色块的外框的y坐标（int），也可以通过blob[1]来获取。
#blob.w() 返回色块的外框的宽度w（int），也可以通过blob[2]来获取。
#blob.h() 返回色块的外框的高度h（int），也可以通过blob[3]来获取。
#blob.pixels() 返回色块的像素数量（int），也可以通过blob[4]来获取。
#blob.cx() 返回色块的外框的中心x坐标（int），也可以通过blob[5]来获取。
#blob.cy() 返回色块的外框的中心y坐标（int），也可以通过blob[6]来获取。
    lcd.display(img)#LCD显示图片
    print(clock.fps())#输出帧率
