#LCD基础
#-----------------------初始化区---------------------------#
import lcd
import image
#-----------------------代码区---------------------------#
#初始化，内部参数默认为type=1, freq=15000000, color=lcd.BLACK
lcd.init()
#清屏，可指定清除后的颜色
lcd.clear()
#LCD分辨率为320*480，KPU上限支持320*240，实际为资源浪费
print(lcd.height(),lcd.width())

#字符大小为16*16
lcd.draw_string(0, 0, "H", lcd.RED, lcd.BLACK)
lcd.draw_string(464, 304, "H", lcd.RED, lcd.BLACK)

#旋转与镜像，函数入口处为可选参数
#lcd.rotation(0~3)
#lcd.mirror(0 or 1)

#显示图片（核心功能）
img = image.Image()
img.draw_string(0, 0, "hello maixpy", scale=2)
#img为图片，通常使用LCD为在帧缓存中修改数据，一次性进行显示，以节约时间，提高帧率
lcd.display(img)
