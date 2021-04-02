#AI口罩识别-(网络模型修改)
#By：黄荣辉
#-----------------------初始化区---------------------------#
import sensor, image, lcd, time
import KPU as kpu
#常量设定，包括标准RGB三原、及类型判断列表及预设边框
color_R = (255, 0, 0)
color_G = (0, 255, 0)
color_B = (0, 0, 255)
class_IDs = ['no_mask', 'mask']
anchor = (0.1606, 0.3562, 0.4712, 0.9568, 0.9877, 1.9108, 1.8761, 3.5310, 3.4423, 5.6823)
#自定义函数，显示输出结果至img
def drawConfidenceText(image, rol, classid, value):
    text = ""
    _confidence = int(value * 100)

    if classid == 1:
        text = 'mask: ' + str(_confidence) + '%'
    else:
        text = 'no_mask: ' + str(_confidence) + '%'

    image.draw_string(rol[0], rol[1], text, color=color_R, scale=2.5)

lcd.init()
sensor.reset(dual_buff=True)
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.set_hmirror(1)
sensor.run(1)
sensor.set_vflip(1)

#加载模型
task = kpu.load(5767168)
#-----------------------代码区---------------------------#
#模型yolo初始化
_ = kpu.init_yolo2(task, 0.5, 0.3, 5, anchor)
#创建空相片
img_lcd = image.Image()
#创建计时器
clock = time.clock()
while (True):
    clock.tick()
    img = sensor.snapshot()
    #将照片置入模型中处理，返回code
    code = kpu.run_yolo2(task, img)
    #逻辑判断
    if code:
        totalRes = len(code)
        #遍历所有的可能区域，进行框选
        for item in code:
            confidence = float(item.value())
            itemROL = item.rect()
            classID = int(item.classid())

            if confidence < 0.52:
                _ = img.draw_rectangle(itemROL, color=color_B, tickness=5)
                continue

            if classID == 1 and confidence > 0.65:
                _ = img.draw_rectangle(itemROL, color_G, tickness=5)
                if totalRes == 1:
                    drawConfidenceText(img, (0, 0), 1, confidence)
            else:
                _ = img.draw_rectangle(itemROL, color=color_R, tickness=5)
                if totalRes == 1:
                    drawConfidenceText(img, (0, 0), 0, confidence)
    _ = lcd.display(img)
    print(clock.fps())

#解初始化
_ = kpu.deinit(task)
