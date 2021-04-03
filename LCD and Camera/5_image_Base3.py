#图像基础3-滤波
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
    #一些备用处理方法
    #img.lens_corr(strength=1)#软件消除畸变，会降低帧率，看情况使用
    #img.chrominvar()#删除照明效果，快速，受阴影影响大
    #img.illuminvar()#删除照明效果，较慢，受阴影影响小
    #img.remove_shadows()#删除阴影部分，目前没啥用，极慢

    #滤波选项
    #img.mean(1)#盒式滤波器
    #img.histeq()#直方图均衡算法
    #img.midpoint(1)#众数滤波
    #img.gaussian(1)#平滑高斯
    #img.laplacian(1, sharpen=False, threshold=False)#边缘检测拉普拉斯核
    lcd.display(img)#LCD显示图片
    print(clock.fps())#输出帧率
