# K210_Primary  
k210基础硬件驱动程序  
1.开发语言：Python  
2.测试硬件：Maix AMIGO  
	CPU:			双核 64bit RISC-V / 400MHz* (双精度FPU集成)  
	内存:			8MiB 64bit 片上 SRAM  
	存储:			16MiB Flash, 支持 micro SDXC 拓展存储 (最大128GB**)  
	屏幕:			3.5寸 TFT 显示屏, 分辨率: 320*480, 支持电容触摸(FT6X36)  
	摄像头:			OV7740 (后摄)与GC0328(前摄) 各 30W 像素(最大分辨率 VGA:640*480)  
	电池:			板载可充电锂聚合物电池 (容量520mAh )  
	板载扬声器与麦克风		集成单音频控制器 ES8374 1W 8Ω 扬声器  
	三轴加速度传感器:		MSA301  
	电池:			520mAh 锂电池  
3.开发平台：MaixPy IDE  
4.固件版本：maixpy_v0.6.0_2_g9720594_amigo_minimum.bin  
5.更新时间：2020.12.28  
6.注意事项：烧录固件需要自行前往https://bbs.sipeed.com 进行更新，选择minimum才可以运行AI。烧录地址写在mask.kfpkg中的flash-list.json，请自行修改至合适flash位置。  
7.更新日志：  
目前仅包含基础驱动类，AI部分由于机器码限制，暂未进行例程化，目前仅测试成功口罩识别，预计下次更新会补全AI部署方面的例程  
8.参考文档：MaixPy开发手册、OpenMV中文参考手册、MicroPython、Machine Vision with Python  
